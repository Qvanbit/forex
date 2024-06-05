from sqlalchemy.orm import Session
from typing import List

from core.domain.entities.currency_rate import CurrencyRate
from core.domain.entities.country_currency import CountryCurrency
from core.domain.entities.relative_change import RelativeChange
from core.domain.entities.settings import Setting
from core.infra.repositories import CurrencyRateRepository, CountryCurrencyRepository, RelativeChangeRepository, SettingRepository

class CurrencyService:
    def __init__(self, db: Session):
        self.currency_rate_repo = CurrencyRateRepository(db)
        self.country_currency_repo = CountryCurrencyRepository(db)
        self.relative_change_repo = RelativeChangeRepository(db)
        self.setting_repo = SettingRepository(db)

    def sync_currency_rate(self, currency_rate: CurrencyRate):
        existing_rate = self.currency_rate_repo.get_by_date_and_code(currency_rate.date, currency_rate.currency_code)
        if existing_rate:
            return existing_rate
        return self.currency_rate_repo.create(currency_rate)

    def sync_country_currency(self, country_currency: CountryCurrency):
        existing_currency = self.country_currency_repo.get_by_code(country_currency.currency_code)
        if existing_currency:
            return existing_currency
        return self.country_currency_repo.create(country_currency)

    def sync_relative_change(self, relative_change: RelativeChange):
        existing_change = self.relative_change_repo.get_by_date_and_code(relative_change.date, relative_change.currency_code)
        if existing_change:
            return existing_change
        return self.relative_change_repo.create(relative_change)

    def sync_setting(self, setting: Setting):
        existing_setting = self.setting_repo.get()
        if existing_setting:
            return existing_setting
        return self.setting_repo.create(setting)

    def get_currency_rates(self, start_date: str, end_date: str) -> List[CurrencyRate]:
        return self.currency_rate_repo.get_by_date_range(start_date, end_date)
