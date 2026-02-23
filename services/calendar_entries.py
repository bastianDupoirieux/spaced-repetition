from googleapiclient.discovery import build

from services.auth import load_or_create_token_file

from utils.calendar_events import create_all_day_event_body

class CalendarSpacedRepetition:

    def __init__(self, credentials):
        self.credentials = credentials

        service = build('calendar', 'v3', credentials=credentials)

    def list_calendars(self):
        return self.service.calendarList().list().execute()

    def create_all_day_event(self, calendar_id, event):
        self.service.events().insert(calendarId=calendar_id, body=event).execute()
    
    