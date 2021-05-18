import requests
import time

# global variables
API_Key = ""     # Enter the API Key
Bot_token = ""   # Enter the Bot token
chat_id =        # Enter your chat id
btc_limit = 50000
eth_limit = 25000
time_interval = 5 * 60


def get_price():
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
    parameters = {
        'start': '1',
        'limit': '200',
        'convert': 'USD'
    }
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': API_Key,
    }
    response = requests.get(url, headers=headers, params=parameters).json()
    btc_price = response["data"][0]["quote"]["USD"]["price"]
    eth_price = response["data"][1]["quote"]["USD"]["price"]
    return btc_price, eth_price


def message(msg):
    url = f"https://api.telegram.org/bot{Bot_token}/sendMessage?chat_id={chat_id}&text={msg}"
    requests.get(url)


def main():
    while True:
        btc_price = get_price()[0]
        eth_price = get_price()[1]
        print(f"Bitcoin Price = {btc_price} $")
        print(f"Ethereum Price = {eth_price} $")
        if btc_price < btc_limit:
            message(f" يسطا سعر البيتكوين بقى:  {btc_price} $")
        if eth_price < eth_limit:
            message(f"يسطا سعر الإيثيريوم بقى :  {eth_price} $")
        time.sleep(time_interval)


main()
