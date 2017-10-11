# -*- coding: utf-8 -*-
import re
import pymongo
client = pymongo.MongoClient('localhost:27009')
paramDB=client['schools']
parmCOL=paramDB['985_codes']




def is_chem(part):
    s=0
    chem_words=['化学','化工','chem','molecu','poly','medic','分子']
    if 'degree_name' in part.keys():
        for i in chem_words:
            if re.search(i,part['degree_name'],re.IGNORECASE):
                print(part['degree_name'])
                s+=1
    return s
def is_master(part):
    s=0
    degree_words=['master','m.s','ms','硕','phd','ph.d','博士','doctor']
    if 'degree_name' in part.keys():
        for i in degree_words:
            if re.search(i,part['degree_name'],re.IGNORECASE):
                print(part['degree_name'])
                s+=1
    return s
def is_date(part,year):

    s=0
    if 'date_range' in part.keys():
        date=[]
        regexObj=re.compile('\d+')

	 #date.append(part['date_range'].replace(' ','').replace('年','').replace('년','')[:4])
        start=regexObj.search(part['date_range'].replace(' ',''))
        date.append(start.group())
	#date.append(part['date_range'].replace(' ','').replace('年','').replace('년','')[-4:])
        end=regexObj.search(part['date_range'].split('–')[-1])
        if end:
            date.append(end.group())
        else:
            date.append(start.group())
	#print(date)
        m=int(date[1])+3
        if int(date[0])<= year <= m:
            s+=1

        else:
            s+=0
    else:
        s+=0
    return s


class Filter():
        def __init__(self,university,result_d,year):
            self.university=university
            self.result_d=result_d
            self.year=year




        @classmethod
        def is_valid(self,university,result_d,year):
            code=parmCOL.find_one({'school_name':university})['linkedinCode']
            ch=parmCOL.find_one({'school_name':university}).get('ch')
            en=parmCOL.find_one({'school_name':university}).get('en')

            s=0
            for part in result_d['edu']:

                #print(len(result_d['edu']))
                #第一个学历不满足条件后，直接筛掉了；即使第二个学历满足条件，也不能被显示出来
                if 'school_url' in part.keys():

                    b=re.search(code,part['school_url'])

                    if b and is_chem(part):
                        s+= is_master(part)
                    else:
                        s+=0

                elif 'school_url_ly' in part.keys():
                    b=re.search(code,part['school_url_ly'])
                    if b and is_chem(part):
                        #s+= self.is_date(part,year)
                        s+= is_master(part)
                    else:
                        s+=0
                elif 'school_name' in part.keys():
                    allin_ch=0
                    allin_en=0
                    for i in range(len(ch)):
                        if re.search(ch[i], part['school_name']):
                            if re.search(ch[i], part['school_name']).group():
                                allin_ch+=1
                    for i in range(len(en)):#北航/南航/...等有多个英文名字的学校还需再精确
                        if re.search(en[i], part['school_name']):
                            if re.search(en[i], part['school_name']).group():
                                allin_en+=1
                    if allin_ch==len(ch) or allin_en == len(en):
                        if is_chem(part):
                        #s+= self.is_date(part,year)
                            s+= is_master(part)
                    else:
                        s+=0
                elif 'school_name_ly' in part.keys():
                    allin_ch_ly=0
                    allin_en_ly=0
                    for i in range(len(ch)):
                        if re.search(ch[i], part['school_name_ly']):
                            if re.search(ch[i], part['school_name_ly']).group():
                                allin_ch+=1
                    for i in range(len(en)):
                        if re.search(en[i], part['school_name_ly']):
                            if re.search(en[i], part['school_name_ly']).group():
                                allin_en+=1
                    if allin_ch_ly ==len(ch) or allin_en_ly == len(en):
                        if is_chem(part):
                        #s+= self.is_date(part,year)
                            s+= is_master(part)
                    else:
                        s+=0

                else:
                    s+=0

                print(result_d['name'],s,'---------------')
            return s

