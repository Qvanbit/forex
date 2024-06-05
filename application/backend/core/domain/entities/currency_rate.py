from dataclasses import dataclass
from datetime import date

@dataclass
class CurrencyRate:
    date: date
    currency_code: str
    rate: float
    