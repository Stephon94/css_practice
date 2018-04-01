# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.core.cache import cache

def services(request):
    cache.clear()
    return render(request, 'services.html')
