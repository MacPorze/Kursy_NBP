from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy_declarative import Base, RatesA, RatesB, Dates
import datetime
import requests

def read():
    session = create_session()

    query = session.query(Dates).get(len(session.query(Dates).all()))
    if query is None:
        new_data = []
    else:
        i = 0
        while True:
            i += 1
            if query.ratesA != []:
                dataA = merge_json_data_2(query,"A")
                break
            else:
                query = session.query(Dates).get(len(session.query(Dates).all())-i)

        query = session.query(Dates).get(len(session.query(Dates).all()))
        i = 0
        while True:
            i += 1
            if query.ratesB != []:
                dataB = merge_json_data_2(query,"B")
                break
            else:
                query = session.query(Dates).get(len(session.query(Dates).all()) - i)

        new_data = {'A': dataA, 'B': dataB}
    session.close()
    return new_data

def write():
    session = create_session()

    time = datetime.datetime.now()

    new_date = Dates(date=time)

    query = session.query(Dates).get(len(session.query(Dates).all()))
    if query is None or query.ratesA == [] or query.ratesB == []:
        [data2, dateA] = get_request("a")

        new_date.ratesA = merge_json_data(data2,dateA,"A")

        [data2, dateB]= get_request("b")

        new_date.ratesB = merge_json_data(data2,dateB,"B")

        session.add_all([new_date, ])
        session.commit()
    else:
        [data2, dateA] = get_request("a")

        if dateA != (query.ratesA[0]).rate_date:
            new_date.ratesA = merge_json_data(data2)

        [data2, dateB] = get_request("b")

        if dateB != (query.ratesB[0]).rate_date:
            new_date.ratesB = merge_json_data(data2)

        if dateA != (query.ratesA[0]).rate_date or dateB != (query.ratesB[0]).rate_date:
            session.add_all([new_date, ])
            session.commit()
            
    session.close()

def get_request(id):
    response = requests.get("http://api.nbp.pl/api/exchangerates/tables/"+id+"/")
    data = response.json()
    data2 = data[0]['rates']
    date = data[0]['effectiveDate']
    return [data2, date]

def merge_json_data(data2,date,id):
    new_rates = []
    for i in data2:
        if id == "A":
            new_rate = RatesA(name=i['currency'], code=i['code'], rate=i['mid'], rate_date=date)
        elif id == "B":
            new_rate = RatesB(name=i['currency'], code=i['code'], rate=i['mid'], rate_date=date)
        new_rates.append(new_rate)
    return new_rates

def merge_json_data_2(query,id):
    data = []
    for i in range(len(query.ratesA)):
        if id == "A":
            d = query.ratesA[i]
        elif id == "B":
            d = query.ratesB[i]
        data.append({'name': d.name, 'code': d.code, 'rate': d.rate, 'date': d.rate_date})
    return data

def create_session():
    engine = create_engine("sqlite:///sqlalchemy_rates.db")
    Base.metadata.create_all(engine)

    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    return session