from app import db
import requests
from model.forex import Forex

my_api_key = 'OBSQOG0772UWM221'

def alpha_request(from_, to_):
    r = requests.get(f'https://www.alphavantage.co/query?function=FX_INTRADAY&from_symbol={from_}&to_symbol={to_}&interval=1min&apikey={my_api_key}')
    k= list(dict(r.json()[ 'Time Series FX (1min)']).keys())[0]
    l = r.json()['Time Series FX (1min)'][k]

    data = {
        "from":from_,
        "to":to_,
        "intraday": l,
        "date":k
    }
    return data

def alpha_save(from_, to_):
    ''' call this function to save auto_save dta to Forex table'''
    data = alpha_request(from_,to_)
    forex =Forex(to=data['to'], from_=data['from'], high=data['intraday']['2. high'], low=data['intraday']['3. low'],
                close=data['intraday']['4. close'],datetime=data['date'])

    db.session.add(forex)
    db.session.commit()

alpha_save('GBP', 'KES')
