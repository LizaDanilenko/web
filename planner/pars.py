import requests
import json

BASE_URL = "https://timetable.tspu.ru/group/get-timetable-for-group?n=433&start=2026-02-16T00%3A00%3A00%2B07%3A00&end=2026-02-22T00%3A00%3A00%2B07%3A00"

def get_schedule(group_number, start_date):
    params = {
        "n": group_number,
        "start": start_date
    }

    response = requests.get(BASE_URL, params=params, timeout=10)
    response.raise_for_status()

    return response.json()


if __name__ == "__main__":
    schedule = get_schedule(433, "2026-02-17")

    with open("schedule_433.json", "w", encoding="utf-8") as f:
        json.dump(schedule, f, ensure_ascii=False, indent=2)

    print("Done")
