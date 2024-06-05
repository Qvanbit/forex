from sqlalchemy.orm import Session
from typing import List
from core.domain.entities.currency_rate import CurrencyRate
from core.domain.entities.country_currency import CountryCurrency
from core.domain.entities.relative_change import RelativeChange
from core.domain.entities.settings import Setting
from core.infra.db.models import DBCurrencyRate, DBCountryCurrency, DBRelativeChange, DBSetting

class CurrencyRateRepository:
    def __init__(self, db: Session):
        self.db = db
        
    def get_by_date_and_code(self, date, currency_code):
        return self.db.query(DBCurrencyRate).filter(DBCurrencyRate.date == date, DBCurrencyRate.currency_code == currency_code).first()
    
    def create(self, currency_rate: CurrencyRate):
        db_currency_rate = DBCurrencyRate(
            date=currency_rate.date,
            currency_code=currency_rate.currency_code,
            rate=currency_rate.rate
        )
        self.db.add(db_currency_rate)
        self.db.commit()
        self.db.refresh(db_currency_rate)
        return db_currency_rate
    
    def get_by_date_range(self, start_date: str, end_date: str) -> List[CurrencyRate]:
        return self.db.query(DBCurrencyRate).filter(DBCurrencyRate.date.between(start_date, end_date)).all()
    
    
class CountryCurrencyRepository:
    def __init__(self, db: Session):
        self.db = db
        
    def get_by_code(self, currency_code):
        return self.db.query(DBCountryCurrency).filter(DBCountryCurrency.currency_code == currency_code).first()
    
    def create(self, country_currency: CountryCurrency):
        db_country_currency = DBCountryCurrency(
            currency_code=country_currency.currency_code,
            country_name=country_currency.country_name,
            currency_name=country_currency.currency_name
        )
        self.db.add(db_country_currency)
        self.db.commit()
        self.db.refresh(db_country_currency)
        return db_country_currency
    
class RelativeChangeRepository:
    def __init__(self, db: Session):
        self.db = db
    
    def get_by_date_and_code(self, date, currency_code):
        return self.db.query(DBRelativeChange).filter(DBRelativeChange.date == date, DBRelativeChange.currency_code == currency_code).first()
    
    def create(self, relative_change: RelativeChange):
        db_relative_change = DBRelativeChange(
            date=relative_change.date,
            currency_code=relative_change.currency_code,
            relative_change=relative_change.relative_change
        )
        self.db.add(db_relative_change)
        self.db.commit()
        self.db.refresh(db_relative_change)
        return db_relative_change
    
class SettingRepository:
    def __init__(self, db: Session):
        self.db = db
        
    def get(self):
        return self.db.query(DBSetting).first()
    
    def create(self, setting: Setting):
        db_setting = DBSetting(
            base_date=setting.base_date
        )
        self.db.add(db_setting)
        self.db.commit()
        self.db.refresh(db_setting)
        return db_setting
        