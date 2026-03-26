from fastapi import FastAPI, Query, HTTPException
from tspu_api import get_groups, build_faculty_tree, get_schedule_cached

app = FastAPI(title="TSU Planner API")

@app.get("/api/groups")
def api_groups():
    return build_faculty_tree(get_groups())

@app.get("/api/schedule")
def api_schedule(
    group: str = Query(..., description="Номер группы, например 433"),
    start: str = Query(..., description="Дата начала YYYY-MM-DD, например 2026-02-16"),
    end: str = Query(..., description="Дата конца YYYY-MM-DD, например 2026-02-22"),
):
    try:
        return get_schedule_cached(group, start, end)
    except Exception as e:
        raise HTTPException(status_code=500, detail=repr(e))
