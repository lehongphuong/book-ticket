from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
# from .models import User
from django.template import loader
from django.http import Http404
from django.urls import reverse
from django.views import generic
import requests
from rest_framework.decorators import api_view
from rest_framework.decorators import parser_classes
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from django.http import JsonResponse

from django.core import serializers

import json

# from models import User
from . import models

from django.db import connection


def index(request):
    return render(request, "index.html", {"users": 1})

# *********************************************
# begin common


# convert cursor to json data
def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]


# execute query sql with cursor
def executeQuery(sql):
    with connection.cursor() as cursor:
        cursor.execute(sql)
        data = dictfetchall(cursor)
    return data
# end common
# *********************************************

# *********************************************	
# begin customer	
@api_view(['POST'])	
@parser_classes((JSONParser,))	
# get all data from customer	
def createDatacustomer(request, format=None):	
    data = json.loads(json.dumps(request.data))	
    obj = models.customer(**data)	
    obj.save()	
    return Response({"id": obj.id, "result": "ok"})
	
	
@api_view(['POST'])	
@parser_classes((JSONParser,))	
# get all data from customer	
def readDatacustomer(request, format=None):	
    return Response(serializers.serialize("json", models.customer.objects.all()))	
	
	
@api_view(['POST'])	
@parser_classes((JSONParser,))	
# get update data from customer	
def updateDatacustomer(request, format=None):	
    data = json.loads(json.dumps(request.data))	
    models.customer(**data).save()	
    return Response({"result": "ok"})	
	
	
@api_view(['POST'])	
@parser_classes((JSONParser,))	
# get delete data from customer	
def deleteDatacustomer(request, format=None):	
    data = json.loads(json.dumps(request.data))	
    models.customer(**data).delete()	
    return Response({"result": "ok"})	
	
	
@api_view(['POST'])	
@parser_classes((JSONParser,))	
# get delete data from customer	
def findDatacustomer(request, format=None):	
    return Response(serializers.serialize("json", models.customer.objects.filter(pk=request.data['pk'])))	
	
# end customer	
# *********************************************