from enum import Enum
from urllib import request
from core.errors import TradeException
import conf
import json


class OrderTypes(Enum):
    Limit = "limit"
    FOK = "fill-or-kill"
    IOC = "immediate-or-cancel"
    Market = "market"


class TradeMaker(object):

    def __init__(self, account):
        self.account = account

    def buy(self, symbol, venue, price, qty, order_type=OrderTypes.Limit):
        query_dict = {
            "account": self.account,
            "symbol": symbol,
            "venue": venue,
            "price": price,
            "qty": qty,
            "direction": "buy",
            "orderType": order_type.value

        }

        return self._execute_trade(query_dict)

    def sell(self, symbol, venue, price, qty, order_type=OrderTypes.Limit):
        query_dict = {
            "account": self.account,
            "symbol": symbol,
            "venue": venue,
            "price": price,
            "qty": qty,
            "direction": "sell",
            "orderType": order_type.value
        }

        return self._execute_trade(query_dict)

    def _execute_trade(self, query_dict):
        endpoint = "/venues/{venue}/stocks/{symbol}/orders".format(
            venue=query_dict["venue"],
            symbol=query_dict["symbol"]
        )

        return self.request(endpoint, data=query_dict)

    def request(self, endpoint, data={}):
        headers = {
            "X-Starfighter-Authorization": conf.API_KEY
        }

        url = "%s%s" % (conf.API_URL, endpoint)

        payload = json.dumps(data).encode("utf-8") if data else None

        req = request.Request(url, headers=headers, data=payload)
        resp = request.urlopen(req)
        return self._parse_response(resp)

    def check_api_status(self):
        self.request('/heartbeat')
        return "Online"

    def _parse_response(self, response):
        return json.loads(response.read().decode('utf-8'))

    def _check_response(self, response_dict):
        if not response_dict["ok"]:
            raise TradeException(response_dict["error"])
