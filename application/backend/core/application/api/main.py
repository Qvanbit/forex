

from fastapi import APIRouter, FastAPI,  Depends
from sqlalchemy.orm import Session
from typing import List

from core.domain.entities.currency_rate import CurrencyRate
from core.domain.entities.country_currency import CountryCurrency
from core.domain.entities.relative_change import RelativeChange
from core.domain.entities.settings import Setting
from core.logic.currency_service import CurrencyService
from core.infra.db.session import get_db

from core.infra.db.models import Base
from core.infra.db.session import engine


def create_app():
    
    def create_tables():
        Base.metadata.create_all(bind=engine)
        
    create_tables()
    
    app = FastAPI(
         title='Forex Monitor',
         docs_url='/api/docs',
         description='Simple project for Forex Monitor'
    )
    
    @app.post("/sync/currency_rate")
    def sync_currency_rate(currency_rate: CurrencyRate, db: Session = Depends(get_db)):
        service = CurrencyService(db)
        return service.sync_currency_rate(currency_rate)

    @app.post("/sync/country_currency")
    def sync_country_currency(country_currency: CountryCurrency, db: Session = Depends(get_db)):
        service = CurrencyService(db)
        return service.sync_country_currency(country_currency)

    @app.post("/sync/relative_change")
    def sync_relative_change(relative_change: RelativeChange, db: Session = Depends(get_db)):
        service = CurrencyService(db)
        return service.sync_relative_change(relative_change)

    @app.post("/sync/setting")
    def sync_setting(setting: Setting, db: Session = Depends(get_db)):
        service = CurrencyService(db)
        return service.sync_setting(setting)

    @app.get("/currency_rates", response_model=List[CurrencyRate])
    def get_currency_rates(start_date: str, end_date: str, db: Session = Depends(get_db)):
        service = CurrencyService(db)
        currency_rates = service.get_currency_rates(start_date, end_date)
        
        # Преобразование экземпляров DBCurrencyRate в экземпляры CurrencyRate
        currency_rates_response = [CurrencyRate(date=rate.date, currency_code=rate.currency_code, rate=rate.rate) for rate in currency_rates]
        
        return currency_rates_response
    
    return app




