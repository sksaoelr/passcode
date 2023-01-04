import datetime
import requests
import json

url = 'https://min-api.cryptocompare.com/data/v2/histoday?fsym=BTC&tsym=KRW&limit=10'
api_key = '05770f67db120460076177af39481e38fe5b46a77563fa33dce00f7c8c469e4d'

headers = {
    'API KEY ': api_key,
}
response = requests.get(url, headers)
dict_data = json.loads(response.content)
print(dict_data['Data']['Data'])

#
for row in dict_data['Data']['Data']:
    print(row)
    print(type(json.loads(row)))
    d = datetime.date.fromtimestamp(row['Data']['time'])
    # print(d)