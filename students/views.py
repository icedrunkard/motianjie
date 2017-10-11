from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
import pymongo
import os
import re
# Create your views here.
from .textfilter import Filter

client = pymongo.MongoClient('localhost:27009')
paramDB=client['schools']
parmCOL=paramDB['985_codes']




def students(request,short,dpt,tutor):
    #print(short,'===',dpt,'===',tutor)
    db = client[short]
    collection_papers=dpt+'_papers'
    col_authors=db[collection_papers]
    
    collection_students=dpt+'_studentsProfile'
    col_students=db[collection_students]

    result=[]
    result_set=set()
    for j in col_authors.find({'tutor':tutor}):#包含此老师的文献
        str_year=j['pub_date'][:4]
        year=int(str_year)
        university=j['school']
        for author in j['author']:#文献中的作者
            

            if col_students.find_one({'_name_':author['name']}):
                #print(author['name'])

                for piece in col_students.find({'_name_':author['name']}):#
                    
                    result_d ={}
                    if piece['url'] not in result_set:
                        result_set.add(piece['url'])
                        result_d['name']=piece['_name_'][:1]+"*"
                        
                        if 'education' in piece.keys():
                            
                            result_d['edu']=piece['education']
                        else:
                            result_d['edu']=''
                        if 'experience' in piece.keys():
                            
                            result_d['exp']=piece['experience']
                        else:
                            result_d['exp']=''
                        print(piece['_name_'],university,year,result_d['name'])


                        if Filter.is_valid(university,result_d,year):
                            
                            
                            result.append(result_d)


                        #if not result_d.get('name')==tutor:
                            #result.append(result_d)

                              
    #PROJECT_ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    #return render(request,os.path.join(PROJECT_ROOT,'stu/templates','tiaozhuan.html'),locals())
    return render(request,'students/tiaozhuan.html',locals())
