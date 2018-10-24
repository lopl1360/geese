# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.
@csrf_exempt
def index(request):
    if request.method == 'POST':
	return handlePost(request)
    else:
	return handleGet(request)



def handlePost(request):
	response = {}
	try:
		url = request.POST['URL']
		short = makeItShort(url)
		response = {'status': 'ok', 'short': short}
	except Exception as e:
		response = {'status' : 'failed', 'error': str(e)}

	return JsonResponse(response);

def handleGet(request):
	return HttpResponse("hello world...........")

def makeItShort(url):
	return "abcdefghi"
