import datetime

def add_days(start_date: datetime.date, days: int) -> datetime.date:
    return start_date + datetime.timedelta(days=days)
