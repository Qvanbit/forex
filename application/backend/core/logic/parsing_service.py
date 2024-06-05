import requests
from bs4 import BeautifulSoup
from datetime import datetime
from typing import List

from core.domain.entities.currency_rate import CurrencyRate
from core.domain.entities.country_currency import CountryCurrency

class ParsingService:
    @staticmethod
    def parse_currency_rates(start_date: str, end_date: str) -> List[CurrencyRate]:
        url = f"https://www.finmarket.ru/currency/rates/?id=10148&pv=1&cur=52170&bd={start_date.day}&bm={start_date.month}&by={start_date.year}&ed={end_date.day}&em={end_date.month}&ey={end_date.year}&x=48&y=13#archive"
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        
        currency_rates = []

        return currency_rates

    @staticmethod
    def parse_country_currencies() -> List[CountryCurrency]:
        url = "https://www.iban.ru/currency-codes"
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        country_currencies = []

        return country_currencies
