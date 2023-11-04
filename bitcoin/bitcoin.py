import requests
import sys
import json

# check sys.argv index 2 in terminal if a int or str or empty
if len(sys.argv) == 2:
    try:
        number_of_bitcoin = float(sys.argv[1]) #get float number in sys.argv index 2 and store in var

        # get bitcoin price in json
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        bitcoin_json = response.json()
        bitcoin_price = bitcoin_json["bpi"]["USD"]["rate_float"]

        # bitcoin price in json multiply by number_of_bitcoin
        price = bitcoin_price * number_of_bitcoin
        print(f"${price:,.4f}")

    except:
        sys.exit("Commad-Line argument is not a number") #is not a int
else:
    sys.exit("Missing command-line argument") #is empty