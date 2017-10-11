import json
import copy
from django.shortcuts import render,render_to_response
from django.http import HttpResponseRedirect,HttpResponse
from .forms import SchoolForm
from django.core.urlresolvers import reverse
import re
import pymongo
from mongoengine import connect
from django.core import serializers
client = pymongo.MongoClient('localhost:27009')
db=client['schools']
col= db['dpts_985']
connect('schools',host='mongodb://localhost/schools',port=27009)


def welcome(request):
    return HttpResponse("<h1>Welcome!</h1>")



def getdptsof(request):

    dpts=[]

    short=request.GET.get('short')  #post是字典格式

    result=col.find({'short':short})

    for item in result:#{'school':post['school']},limit=20

        dpts=item['dpts']

    data={'short':dpts}
    if not len(dpts)==0:
            #data = serializers.serialize('json', dpts)
        return HttpResponse(json.dumps(data), content_type="application/json")



    
def index(request):
    results=[]
    for i in col.find():
        del i['_id']
        results.append(i)
        
    
    return render(request,'index/index.html',{'results':json.dumps(results)})
    

    
    
    
