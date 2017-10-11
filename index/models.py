#_*_ coding:utf-8 _*_

#每次变更完此文件需要python manage.py makemigrations

#这里变更后，后续在forms.py中变更，在views.py中变更

from __future__ import unicode_literals
from django.db import models
import pymongo
from mongoengine import *

connect('schools',host='mongodb://localhost/schools',port=27009)


client = pymongo.MongoClient('localhost:27009')
db = client['schools']
col= db['dpts_985']

def getSchool():
    SCHOOL_CHOICES=set()
    for item in col.find():
        SCHOOL_CHOICES.add((item['short'],item['university']))
    return SCHOOL_CHOICES

def getDpt(short):
    DPT_CHOICES=set()

    result=col.find_one({'short':short})
    for item in result['dpts']:
        DPT_CHOICES.add((item,item))
    return DPT_CHOICES    

SCHOOL_CHOICES=(
    #后面是显示在页面上的，手书进去，前面是缩写，作为后续传入的Database的名称
    ('THU','清华大学'),

    )
DPT_CHOICES=(
    #后面是显示在页面上的，前面的数据作为后续传入的Collection的名称前缀
    ('材料学院','材料学院'),

    )

class School(models.Model):
    school=models.CharField(max_length=300,choices= getSchool(),default=None)
class Dpts_985(Document):
    university=StringField(max_length=120, required=True)
    short=StringField(max_length=120)
    dpts=ListField(StringField())
