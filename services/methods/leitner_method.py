import datetime
from typing import Dict, List

from utils.date import add_days

class LeitnerMethod:
    def __init__(self, params: Dict[List[int]], start_date:datetime.date):
        self.intervals = params["intervals"]
        self.start_date = start_date

    def define_intervals(self):
        result_days = []
        for interval in self.intervals:
            result_days.append(add_days(self.start_date, interval))
        return result_days
