from enums.methods import SpacedRepetitionMethod
from typing import Dict, Any

from constants import leitner_method

def load_parameters(method: SpacedRepetitionMethod) -> Dict[str, Any]:
    match method:
        case SpacedRepetitionMethod.LEITNER_METHOD.value:
            return load_leitner_method_parameters()

def load_leitner_method_parameters() -> Dict[str, Any]:
    return {
        "intervals": leitner_method.intervals
    }
