import requests
import json

api_key = "-"

search_url = 'https://www.alphavantage.co/query?function=SYMBOL_SEARCH&keywords=microsoft&apikey='+api_key
url = 'https://www.alphavantage.co/query?function=TIME_SERIES_MONTHLY&symbol=TSLA&apikey='+api_key
r = requests.get(url)
data = r.json()

# with open('tsla_monthly.json', 'w') as f:
#     json.dump(data, f)