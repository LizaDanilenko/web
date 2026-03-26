import time
import requests
from datetime import date, datetime, timedelta
from typing import Dict, List, Any, Tuple

BASE = "https://timetable.tspu.ru"
GROUPS_URL = f"{BASE}/group/get-data-by-group"
SCHEDULE_URL = f"{BASE}/group/get-timetable-for-group"

_cache: Dict[Tuple[str, str, str], Dict[str, Any]] = {}
CACHE_TTL_SECONDS = 30 * 60  # 30 минут


def get_groups() -> List[dict]:
    r = requests.get(GROUPS_URL, timeout=15)
    r.raise_for_status()
    return r.json()


def build_faculty_tree(groups: List[dict]) -> Dict[str, Dict[str, List[str]]]:
    tree: Dict[str, Dict[str, List[str]]] = {}
    for g in groups:
        faculty = g["faculty"]
        course = str(g["course"])
        gruppa = g["gruppa"]
        tree.setdefault(faculty, {}).setdefault(course, []).append(gruppa)

    for f in tree:
        for c in tree[f]:
            tree[f][c].sort()

    return tree


def _to_iso_ksk(d: date) -> str:
    # 00:00:00+07:00 (как в твоём URL)
    return f"{d.isoformat()}T00:00:00+07:00"


def fetch_schedule(group_number: str, start_date: str, end_date: str) -> Any:
    """
    start_date, end_date в формате YYYY-MM-DD
    """
    params = {
        "n": group_number,
        "start": _to_iso_ksk(date.fromisoformat(start_date)),
        "end": _to_iso_ksk(date.fromisoformat(end_date)),
    }
    r = requests.get(SCHEDULE_URL, params=params, timeout=15)
    r.raise_for_status()
    return r.json()


def get_schedule_cached(group_number: str, start_date: str, end_date: str) -> Any:
    key = (group_number, start_date, end_date)
    now = time.time()

    if key in _cache and (now - _cache[key]["ts"]) < CACHE_TTL_SECONDS:
        return _cache[key]["data"]

    data = fetch_schedule(group_number, start_date, end_date)
    _cache[key] = {"ts": now, "data": data}
    return data
