import pandas_datareader as pdr
import pandas as pd
from pandas_datareader._utils import RemoteDataError
import datetime
import talib

import mailchimp_marketing as MailchimpMarketing
from mailchimp_marketing.api_client import ApiClientError

from django.shortcuts import get_object_or_404
from django.conf import settings
from django.utils import timezone

from .models import Bitcoin


def get_data():
    end_d = datetime.datetime.now()
    diff = datetime.timedelta(days = 600)
    start_d = end_d - diff
    period = 252
    try:
        data = pdr.get_data_yahoo('BTC-USD', start=start_d, end=end_d)
        close = data['Adj Close']
        high = data['High']
        low = data['Low']
        last_close = data['Adj Close'][-1]
        results = [
            talib.DEMA(close, period)[-1], 
            talib.EMA(close, period)[-1],
            talib.HT_TRENDLINE(close)[-1],
            talib.KAMA(close, period)[-1],
            talib.SAR(high, low, acceleration=0.020, maximum=0.2)[-1],
            talib.SMA(close, period)[-1],
            talib.TRIMA(close, period)[-1],
            talib.WMA(close, period)[-1]
            ]
        fields = []
        for result in results:
            if result > last_close:
                fields.append('sell')
            else:
                fields.append('buy')
        btc = get_object_or_404(Bitcoin, title='btc-usd')
        btc.dema = fields[0]
        btc.ema = fields[1]
        btc.ht = fields[2]
        btc.kama = fields[3]
        btc.sar = fields[4]
        btc.sma = fields[5]
        btc.trima = fields[6]
        btc.wma = fields[7]
        btc.date_added = datetime.datetime.now(tz=timezone.utc)
        btc.save()
    except RemoteDataError:
        print('connection error')


api_key = settings.MAILCHIMP_API_KEY
server = settings.MAILCHIMP_DATA_CENTER
list_id = settings.MAILCHIMP_EMAIL_LIST_ID

def subscribe(email):

    client = MailchimpMarketing.Client()
    client.set_config({
        "api_key": api_key,
        "server": server,
    })

    member_info = {
        "email_address": email,
        "status": "subscribed",
    }

    try:
        response = client.lists.add_list_member(list_id, member_info)
        print("response: {}".format(response))
    except ApiClientError as error:
        print("An exception occurred: {}".format(error.text))


    









'''end_d = datetime.datetime.now()
diff = datetime.timedelta(days = 600)
start_d = end_d - diff

def get_trend_data(start=start_d, end=end_d, symbol='BTC-USD'):
    items = {}
    try:
        data = pdr.get_data_yahoo(symbol, start, end)
        items['close'] = data['Adj Close']
        items['last_close'] = data['Adj Close'][-1]
        items['error'] = None
    except RemoteDataError:
        items['error'] = 'Fetching data failed due to an error on the yahoo finance server. Please come back later.'
        
    return items

data = get_trend_data()

# Creating indicators class which inherits from YahooData
class Indis:
    def __init__(self):
        self.last_close = data['last_close']
        self.close = data['close']
        self.error = data['error']
        self.period = 252
        
        # Using Technical Analysis Library to create an extensive list of trading indicators
        self.dema = talib.DEMA(self.close, self.period)
        self.ema = talib.EMA(self.close, self.period)
        self.ht = talib.HT_TRENDLINE(self.close)
        self.kama = talib.KAMA(self.close, self.period)
        self.mama, self.fama = talib.MAMA(self.close, fastlimit=0.5, slowlimit=0.05)
        self.sma = talib.SMA(self.close, self.period)
        self.t3 = talib.T3(self.close, self.period, vfactor=0.7)
        self.wma = talib.WMA(self.close, self.period)
        self.trima = talib.TRIMA(self.close, self.period)

        self.scores = [self.dema, self.ema, self.ht, self.kama, self.fama, 
               self.sma, self.t3, self.trima, self.wma]

        # List of indicators last readings
        self.results = [ score[-1] for score in self.scores ]
        
        self.values = [ self.last_close for _ in range(len(self.results)) ]

        # List of indicators names
        self.names = ['Double Exponential Moving Average', 'Exponential Moving Average','Hilbert Transform - Instantaneous Trendline', 'Kaufman Adaptive Moving Average',
            'MESA Adaptive Moving Average', 'Simple Moving Average', 'Triple Exponential Moving Average', 'Triangular Moving Average', 'Weighted Moving Average']

indis = Indis()'''

