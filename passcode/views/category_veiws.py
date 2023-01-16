from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from requests import Request, Session
from django.core.paginator import Paginator
import random
import requests
import json
import sys, os
import logging
import datetime
logger = logging.getLogger('category')

def company_info(request):

    return render(request, 'passcode/company_info.html')

def service_info(request):

    return render(request, 'passcode/service_info.html')

def partners_info(request):

    return render(request, 'passcode/partners_info.html')

# def cryptocurrency_info(request):
#     url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
#     parameters = {
#         'start': '1',
#         'limit': '5',
#         'convert': 'KRW'
#     }
#     headers = {
#         'Accepts': 'application/json',
#         'X-CMC_PRO_API_KEY': '12581344-be5c-4c0e-8dca-a4198ab29dfe',
#     }
#
#     session = Session()
#     session.headers.update(headers)
#
#     response = session.get(url, params=parameters)
#     data = json.loads(response.text)
#     market_list = []
#     for in_data in data['data']:
#         temp_data = {
#             'name': in_data['name'],
#             'symbol': in_data['symbol'],
#             'KRW': format(round(in_data['quote']['KRW']['price']), ',d'),
#             'volume_change_24h': in_data['quote']['KRW']['volume_change_24h'],
#             'market_cap': format(round(in_data['quote']['KRW']['market_cap']), ',d')
#         }
#         market_list.append(temp_data)
#     context = {'market_list': market_list}
#     # print(context)
#     return render(request, 'passcode/cryptocurrency_info.html', context)

def nft_info(request):

    return render(request, 'passcode/nft_info.html')

def temp(request):
    context = {'test': "test"}
    return render(request, 'passcode/temp.html', context)

def cryptocurrency_info(request):
    #
    # if request.method == 'GET':
    #     symbol = request.GET['symbol']
    #     print(symbol)
    url = 'https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC&tsyms=USD'
    headers = {
        'Apikey': '05770f67db120460076177af39481e38fe5b46a77563fa33dce00f7c8c469e4d'
    }

    session = Session()
    session.headers.update(headers)

    response = session.get(url)
    data = json.loads(response.text)
    # print(data['DISPLAY']['BTC']['USD']['PRICE'])
    # market_info = []
    # print(data['DISPLAY']['BTC']['USD'])
    # for in_data in data['DISPLAY']['BTC']['USD']:
    #     print(in_data)
    in_data = data['DISPLAY']['BTC']['USD']
    market_info = {
        'price': in_data['PRICE'],
        'volume_change_24h': in_data['VOLUME24HOURTO'],
        'market_cap': in_data['MKTCAP']
    }
    # market_info.append(temp_data)
    context = {'market_info': market_info}
    # print(context)
    # if request.method == 'GET':
    #     symbol = request.GET.get('symbol')
    #     context['symbol'] = symbol
    #     print(context)
    # context = {
    #     'symbol' : 'BTC',
    #     'symbol_code': 'BINANCE:BTCUSDT|12M'
    # }
    return render(request, 'passcode/cryptocurrency_info.html', context)

def notice_board(request):

    return render(request, 'passcode/notice_board.html')

def news_board(request):
    page = request.GET.get('page', '1')  # 페이지
    param = {
        'token' : '$2y$10$z0PDxiNJeRYH6u32sCbkT.ZgdyVsp/VvHHjYsruMwPs8CYXfOAgSW',
        'limit' : 20
    }
    url = f"https://www.cryptohub.or.kr/api/v1/news"
    # headers = {"Authorization": "Bearer m4om9xjkcb1u0dyqkdgcqolsfdbcgu7yygfxhl6vcqwmd5imeh"}
    response = requests.post(url, param)
    in_data = json.loads(response.content.decode('utf-8'))
    result = []
    for row in in_data['data']:
        update_date = row['pubdate'][5:10].replace('0', '').replace('-','/')
        temp_data = {
            'id' : row['id'],
            'title' : row['title'],
            'sub_title' : row['sub_title'],
            'pubdate' : row['pubdate'][:10],
            'updated_at' : row['updated_at'],
            'thumbnail' : row['thumbnail'],
            'update_date' : update_date
        }
        result.append(temp_data)

    paginator = Paginator(result, 9)  # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)
    context = {'news_list': page_obj}

    return render(request, 'passcode/news_board.html', context)

def contact_us(request):

    return render(request, 'passcode/contact_us.html')