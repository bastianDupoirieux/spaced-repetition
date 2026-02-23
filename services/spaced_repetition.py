import datetime
from typing import List

from enums.methods import SpacedRepetitionMethod

from services.methods.leitner_method import LeitnerMethod

from utils.parameter_loaders import load_parameters

class SpacedRepetition:
    def __init__(self, method, start_date:datetime.date):
        self.method = method
        self.start_date = start_date
        self._ensure_method_is_valid()

    def get_review_dates(self)->List[datetime.date]:
        params= self._load_parameters()
        method = self.instantiate_method(params)
        intervals = method.define_intervals()
        return intervals

    def instantiate_method(self, params):
        match self.method:
            case SpacedRepetitionMethod.LEITNER_METHOD:
                return LeitnerMethod(params, self.start_date)

    def _load_parameters(self):
        params = load_parameters(self.method)
        return params
    
    def _ensure_method_is_valid(self):
        if self.method not in SpacedRepetitionMethod:
            raise ValueError(f"Method: {self.method} is not implemented")
