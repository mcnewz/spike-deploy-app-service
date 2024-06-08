from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

import json
from rest_framework.decorators import api_view, throttle_classes, schema
from rest_framework.schemas import AutoSchema
from rest_framework.response import Response
from rest_framework.throttling import UserRateThrottle
from rest_framework.schemas import AutoSchema
from django.http import JsonResponse


def index(request):
    print('Request for index page received')
    return render(request, 'hello_azure/index.html')

@csrf_exempt
def hello(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        
        if name is None or name == '':
            print("Request for hello page received with no name or blank name -- redirecting")
            return redirect('index')
        else:
            print("Request for hello page received with name=%s" % name)
            context = {'name': name }
            return render(request, 'hello_azure/hello.html', context)
    else:
        return redirect('index')



@api_view(http_method_names=['GET', 'POST'])
def hello_world(request):
    # body_unicode = request.body.decode('utf-8')
    # header = request.headers
    # body = json.loads(body_unicode)
    # print(body)
    # print(header)
    print("hello_world ------------ ")
    # if request.method == 'POST':
    #     return Response({"message": "Hello, world! POST"})
    
    return JsonResponse({"message": "Hello, world!"})
