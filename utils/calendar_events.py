import datetime

def create_all_day_event_body(subject: str, description: str, start_date: datetime.date, end_date: datetime.date) -> dict:
    return {
        "summary": f"Review: {subject}",
        "description": description,
        "start": {
            "date": start_date.isoformat()
        },
        "end": {
            "date": end_date.isoformat()
        }
    }
