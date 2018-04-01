# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.core.cache import cache

def index(request):
	cache.clear()
	print 'wtf b'
	return render(request,'index.html')
