from django.shortcuts import render
import datetime

# Create your views here.
def webPage(request):
    visitors=open('visitors.txt','a')
    visitors.write(str(datetime.datetime.now().__format__('%Y/%m/%d %H:%M:%S'))+'\t'+request.META.get("REMOTE_ADDR")+'\t'+request.META.get('HTTP_USER_AGENT')+'\n')
    return render(request,'webPage.html')

def messagePage(request):
    # f=open('messages.txt','r')
    # content=f.readlines()
    # f.close()
    # table=r"<table><tr><th>Time</th><th>Message</th></tr>"
    # for eachline in content:
    #     eachline=eachline.split('\n')[0]
    #     table+=r"<tr>"
    #     for eachcell in eachline.split('\t'):
    #         table+="<td>"+eachcell+r"</td>"
    #     table+=r"</tr>"
    # table+=r"</table>"
    return render(request,'allMessages.html')