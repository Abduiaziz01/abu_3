import schedule
import time
import requests

def test():
    print("Hello World!")
    print(time.ctime())

def get_btc_price():
    print("====BTC====")
    url = 'https://www.binance.com/api/v3/ticker/price?symbol=BTCUSDT'
    response = requests.get(url=url).json()
    print(response)
    a = response['price']
    print(f"Стоимость биткоина на {time.ctime()} - {a}$") 
    
    

# schedule.every(2).seconds.do(test)
# schedule.every().day.at("18:23").do(test)
# schedule.every().thursday.at("18:26").do(test)
# schedule.every().hour.at(":31").do(test)
schedule.every(2).seconds.do(get_btc_price)

while True:
    schedule.run_pending()