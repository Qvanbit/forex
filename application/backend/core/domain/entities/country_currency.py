from dataclasses import dataclass

@dataclass
class CountryCurrency:
    country_name: str
    currency_code: str
    currency_name: str