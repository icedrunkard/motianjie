from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
import pymongo
import os
import json
from django.shortcuts import render,render_to_response
# Create your views here.
# 
client = pymongo.MongoClient('localhost:27009')
db=client['schools']
col=db['dpts_985']


#short是学校缩写，dpt是学院汉字
def teachers(request):

    short=request.GET.get('short')

    dpt=request.GET.get('dpt')
    #print(short,dpt,'----------------------------------')
    university=col.find_one({'short':short})['university']
    db2=client[short]
    collection_name=dpt+'_teachers'
    col2=db2[collection_name]
    results=[]

    for i in col.find():
        results.append(i)    

    tutors=[]
    for item in col2.find():#{'school':post['school']},limit=20
        tutors.append(item)
    #data=
    if not len(tutors)==0:
        #return HttpResponse(json.dumps(data), content_type="application/json")
        return render_to_response('tutors/table.html',{'university':university,
                                                       'dpt':dpt,
                                                       'tutors':tutors,
                                                       'short':short,
                                                       'results':results
                                                       })
        #return render('tutors/table.html',locals())



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



