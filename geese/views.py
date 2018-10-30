# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect
import json
import requests

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






def run_query(query): # A simple function to use requests.post to make the API call. Note the json= section.
    headers = {"Authorization": "u51sAc8x0w2Dq0BEJnTdG3YD"}
    request = requests.post('http://localhost:9091/graph/', json={'query': query}, headers=headers)
    if request.status_code == 200:
        return json.loads(request.content)
    else:
        raise Exception("Query failed to run by returning code of {}. {}".format(request.status_code, query))

        
# The GraphQL query (with a few aditional bits included) itself defined as a multi-line string.       
@csrf_exempt
def forward(request, id):
    query = """query {
		urls(id: "%s") {
			edges {
				node {
					url
				}
			}
		}
	}""" %id

    result = run_query(query) # Execute the query

    try:
    	return redirect(result['data']['urls']['edges'][0]['node']['url'])
    except IndexError as e:
        response = {'status' : 'failed', 'error': str(e)} 
        return JsonResponse(response);
