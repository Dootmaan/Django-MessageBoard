from django.shortcuts import render
import json
from django.http import HttpResponse
import datetime

# Create your views here.

def response(request):
    content=request.POST.get('content','')

    f=open('messages.txt','a')
    f.write(str(datetime.datetime.now().__format__('%Y/%m/%d %H:%M:%S'))+'\t'+content+'\n')
    f.close()
    
    res={}
    res['content']=content
    return HttpResponse(json.dumps(res,ensure_ascii=False),content_type='application/json')

def loadMessages(request):
    f=open('messages.txt','r')
    content=f.readlines()
    f.close()
    table="<table><tr><th>Time</th><th></th><th>Message</th></tr>"
    for eachline in content:
        eachline=eachline.split('\n')[0]
        table+="<tr>"
        for eachcell in eachline.split('\t'):
            table+="<td align='center'>"+eachcell+"</td><td></td>"
        table+="</tr>"
    table+="</table>"
    return HttpResponse(table)