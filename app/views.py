from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from app.models import*
def insert_topic(request):
    tn=input('enter topic_name')
    TO=Topic.objects.get_or_create(topic_name=tn)[0]
    TO.save()
    return HttpResponse('Topic is inserted successfully')

def insert_webpage(register):
    tn=input('enter tn')
    n=input('enter name')
    url=input('enter url')
    TO=Topic.objects.get_or_create(topic_name=tn)[0]
    TO.save()
    WO=Webpage.objects.get_or_create(topic_name=TO,name=n,url=url)[0]
    WO.save()
    return HttpResponse('Webpage data is inserted')
def insert_AR(register):
    tn=input('enter topic_name')
    TO=Topic.objects.get_or_create(topic_name=tn)[0]
    TO.save()
    n=input('enter name')
    u=input('enter url')
    WO=Webpage.objects.get_or_create(topic_name=TO,name=n,url=u)[0]
    WO.save()
    a=input('enter author')
    d=input('enter date')
    AO=AccessRecord.objects.get_or_create(name=WO,author=a,date=d)[0]
    AO.save()
    return HttpResponse('accessrecord data is successfully')
