from dataclasses import dataclass
from datetime import date

@dataclass
class RelativeChange:
    date: date
    currency_code: str
    relative_change: float