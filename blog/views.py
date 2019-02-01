# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse,HttpResponseRedirect

from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request)