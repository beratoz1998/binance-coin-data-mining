from binance.client import Client
import json
import datetime
api_key = 'XXXXXXXXXXXXXXX'
api_secret = 'XXXXXXXXXXXXXX'
client = Client(api_key, api_secret)

from binance.websockets import BinanceSocketManager

class Trade(object):
    def __init__(self, **kwargs):
# {'e': 'trade', 'E': 1613678970817, 's': 'LTCBUSD', 't': 6377947, 'p': '224.70000000', 'q': '0.12000000',
# 'b': 171816378, 'a': 171816463, 'T': 1613678970816, 'm': True, 'M': True}
        self.e = None
        self.E = None
        self.s = None
        self.t = None
        self.p = None
        self.q = None
        self.b = None
        self.a = None
        self.T = None
        self.m = None
        self.M = None
        self.__dict__.update(kwargs)
        self.IslemTarihi = datetime.datetime.fromtimestamp(self.T/1000)

"""class Kline(object):
    def __init__(self,**kwargs):
        self.__dict__.update(kwargs)"""

latestPrice: Trade = None

def process_message(msg):
    global latestPrice
    #print(msg)
    if msg['e'] == 'trade':
        newPrice = Trade(**msg)
        if latestPrice != None:
            if newPrice.p > latestPrice.p:
                print("+ UP {} - {} - {}".format(newPrice.p, latestPrice.p, newPrice.IslemTarihi))
            elif newPrice.p == latestPrice.p:
                print("= EQ {} - {} - {}".format(newPrice.p, latestPrice.p, newPrice.IslemTarihi))
            else:
                print("- DOWN {} - {} - {}".format(newPrice.p, latestPrice.p, newPrice.IslemTarihi))
        latestPrice = newPrice

"""    if msg['e'] == 'kline':
        klineObj = kline(**msg)"""


bm = BinanceSocketManager(client, user_timeout=60)
conn_key = bm.start_trade_socket('LTCBUSD',process_message)
bm.start()





