from sqlalchemy import Column, String, Float, Date
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class DBCurrencyRate(Base):
    __tablename__ = 'currency_rate'
    date = Column(Date, primary_key=True)
    currency_code = Column(String, primary_key=True)
    rate = Column(Float)
    
class DBCountryCurrency(Base):
    __tablename__ = 'country_currency'
    currency_code = Column(String, primary_key=True)
    country_name = Column(String)
    currency_name = Column(String)
    
class DBRelativeChange(Base):
    __tablename__ ='relative_changes'
    date = Column(Date, primary_key=True)
    currency_code = Column(String, primary_key=True)
    relative_change = Column(Float)
    
class DBSetting(Base):
    __tablename__ = 'settings'
    id = Column(String, primary_key=True, default='base_date')
    base_date = Column(Date)
