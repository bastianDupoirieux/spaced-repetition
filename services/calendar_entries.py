from googleapiclient.discovery import build

from constants.api import google_calendar_api_name, google_calendar_api_version

class CalendarSpacedRepetition:

    def __init__(self, credentials):
        self.credentials = credentials

        self.service = build(google_calendar_api_name, google_calendar_api_version, credentials=credentials)

    def list_calendars(self):
        return self.service.calendarList().list().execute()

    def create_all_day_event(self, calendar_id, event):
        self.service.events().insert(calendarId=calendar_id, body=event).execute()
    
