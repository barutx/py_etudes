import sys
import requests

def main():
    r = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    o = r.json()
    price_usd = float(o["bpi"]["USD"]["rate_float"])

    if len(sys.argv) >= 1:
        n_coin = float(sys.argv[1])
        if type(n_coin) == float:
            total = price_usd * n_coin
            print(f"${total:,.4f}")
        else:
            sys.exit()
if __name__ == '__main__':
    main()


     
