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
from django.shortcuts import render
from ..models import Notice
logger = logging.getLogger('category')

def notice_list(request):
    notice_list = Notice.objects.order_by('-create_date')
    context = {'notice_list': notice_list}

    return render(request, 'passcode/notice_list.html', context)

def notice_detail(request, notice_id):
    notice_detail = get_object_or_404(Notice, pk=notice_id)
    context = {'notice_detail': notice_detail}

    return render(request, 'passcode/notice_detail.html', context)
