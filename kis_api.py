import mojito
import requests
import json

def medo(app_key, app_secret, acc_no, stock_code, quantity):
    broker = mojito.KoreaInvestment(
        api_key= app_key,
        api_secret=app_secret,
        acc_no=acc_no,
        exchange='나스닥',
        mock=True
    )

    resp = broker.create_market_sell_order(
        symbol=stock_code,
        quantity=quantity
    )
    return resp

def mesoo(app_key, app_secret, acc_no, stock_code, quantity):
    broker = mojito.KoreaInvestment(
        api_key=app_key,
        api_secret=app_secret, 
        acc_no=acc_no,
        exchange='나스닥',
        mock=True
    )

    resp = broker.create_market_buy_order(
        symbol=stock_code,
        quantity=quantity
    )
    return resp


def get_token(app_key, app_secret):
    padata = {
        "grant_type": "client_credentials",
        "appkey" : app_key,
        "appsecret": app_secret
    }

    res = requests.post('https://openapivts.koreainvestment.com:29443/oauth2/tokenP', data=json.dumps(padata))

    if res.status_code == 200:
        jsondata = res.json()
        return jsondata['access_token']
    else:
        return "FAIL"