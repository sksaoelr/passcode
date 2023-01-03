import datetime
import requests
import json

url = 'https://min-api.cryptocompare.com/data/v2/histoday?fsym=BTC&tsym=KRW&limit=10'
api_key = '05770f67db120460076177af39481e38fe5b46a77563fa33dce00f7c8c469e4d'

headers = {
    'API KEY ': api_key,
}
response = requests.get(url, headers)

in_data = json.loads(response.text)

for row in in_data:
    print(row)
    print(type(json.loads(row)))
    # d = datetime.date.fromtimestamp(row['Data']['time'])
    # print(d)