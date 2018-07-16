from sqlalchemy import Column, Integer, String, Float, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, backref

Base = declarative_base()

class Dates(Base):
    __tablename__ = "dates"
    id = Column(Integer,primary_key=True)
    date = Column(Date, nullable=False)


class RatesA(Base):
    __tablename__ = "ratesA"
    id = Column(Integer,primary_key=True)
    name = Column(String, nullable=False)
    code = Column(String, nullable=False)
    rate = Column(Float, nullable=False)
    rate_date = Column(String)
    date_id = Column(Integer, ForeignKey('dates.id'))
    date = relationship("Dates", backref=backref('ratesA', order_by=id))

class RatesB(Base):
    __tablename__ = "ratesB"
    id = Column(Integer,primary_key=True)
    name = Column(String, nullable=False)
    code = Column(String, nullable=False)
    rate = Column(Float, nullable=False)
    rate_date = Column(String)
    date_id = Column(Integer, ForeignKey('dates.id'))
    date = relationship("Dates", backref=backref('ratesB', order_by=id))


engine = create_engine('sqlite:///sqlalchemy_rates.db')
Base.metadata.create_all(engine)