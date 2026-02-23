import datetime

def create_all_day_event_body(subject: str, start_date: datetime.date, description=None) -> dict:
    return {
        "summary": f"Review: {subject}",
        "description": description,
        "start": {
            "date": start_date.isoformat()
        },
        "end": {
            "date": start_date.isoformat()
        }
    }
