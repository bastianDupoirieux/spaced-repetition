import datetime

from services.calendar_entries import Calendar
from services.auth import load_or_create_token_file
from services.spaced_repetition import SpacedRepetition

from utils.calendar_events import create_all_day_event_body

def main(subject, start_date, method, calendar_id):

    creds = load_or_create_token_file()

    spaced_repetition = SpacedRepetition(method)
    review_dates = spaced_repetition.get_review_dates(start_date)
    calendar_entries = Calendar(creds)

    for date_val in review_dates:
        event_body = create_all_day_event_body(subject, date_val)
        calendar_entries.create_all_day_event(calendar_id, event_body)

if __name__ == "__main__":
    main("physics", datetime.date.today(), "leitner_method", "anonymsozialemedien@gmail.com")
