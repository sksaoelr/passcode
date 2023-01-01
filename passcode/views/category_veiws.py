from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from requests import Request, Session
import json
import sys, os
import logging
logger = logging.getLogger('category')

def company_info(request):

    return render(request, 'passcode/company_info.html')

def service_info(request):

    return render(request, 'passcode/service_info.html')

def partners_info(request):

    return render(request, 'passcode/partners_info.html')

def cryptocurrency_info(request):
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
    parameters = {
        'start': '1',
        'limit': '5',
        'convert': 'KRW'
    }
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': '12581344-be5c-4c0e-8dca-a4198ab29dfe',
    }

    session = Session()
    session.headers.update(headers)

    response = session.get(url, params=parameters)
    data = json.loads(response.text)
    market_list = []
    for in_data in data['data']:
        temp_data = {
            'name': in_data['name'],
            'symbol': in_data['symbol'],
            'KRW': format(round(in_data['quote']['KRW']['price']), ',d'),
            'volume_change_24h': in_data['quote']['KRW']['volume_change_24h'],
            'market_cap': format(round(in_data['quote']['KRW']['market_cap']), ',d')
        }
        market_list.append(temp_data)
    context = {'market_list': market_list}
    print(context)
    return render(request, 'passcode/cryptocurrency_info.html', context)

def nft_info(request):

    return render(request, 'passcode/nft_info.html')

def notice_board(request):

    return render(request, 'passcode/notice_board.html')

def news_board(request):

    return render(request, 'passcode/news_board.html')

def contact_us(request):

    return render(request, 'passcode/contact_us.html')