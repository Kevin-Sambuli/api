from app import db
import requests
from model.forex import Forex

def alpha_request():
   r= requests.get('http://tech-feedbacks-api.herokuapp.com/feedback')
   print(r)

alpha_request()

def alpha_save(to, from_, high, low,close,date_):
    ''' call this function to save auto_save dta to Forex table'''

    data_from_api=Forex(to=to,from_=from_, high=high, low=low, close=close, datetime=date_)

    db.session.add(data_from_api)
    db.session.commit()

#
# alpha_save(to="KES", from_="USD", high=158.9500, low=158.9500,close=158.9500, date_="2020-03-13 16:00:00")



