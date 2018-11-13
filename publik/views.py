# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import os
from django.shortcuts import render

from django.http import HttpResponse

def index(request):
 return render(request, 'index.html')
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# return HttpResponse(BASE_DIR)
 