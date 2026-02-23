import datetime
from typing import List

from enums.methods import SpacedRepetitionMethod

from services.methods.leitner_method import LeitnerMethod

from utils.parameter_loaders import load_parameters

class SpacedRepetition:
    def __init__(self, method):
        self.method = method
        self._ensure_method_is_valid()

    def get_review_dates(self, start_date)->List[datetime.date]:
        params= self._load_parameters()
        method = self.instantiate_method(params, start_date)
        intervals = method.define_intervals()
        return intervals

    def instantiate_method(self, params, start_date:datetime.date):
        match self.method:
            case SpacedRepetitionMethod.LEITNER_METHOD.value:
                return LeitnerMethod(params, start_date)

    def _load_parameters(self):
        params = load_parameters(self.method)
        return params
    
    def _ensure_method_is_valid(self):
        if self.method not in SpacedRepetitionMethod:
            raise ValueError(f"Method: {self.method} is not implemented")
