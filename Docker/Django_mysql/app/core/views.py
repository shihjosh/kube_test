from django.shortcuts import render,HttpResponse

from core.models import Music
from django.core import serializers
from datetime import datetime

# Create your views here.
def core(request):
    return render(request, 'home/home.html' ,{})

def other(request):
    return render(request, 'home/other.html',{})

def item1(request):
    return render(request, 'home/item1.html',{"name": 'Dashboard'})

def item2(request):
    # try: 
    #     unit = Music.objects.get(song="song1") #讀取一筆資料
    # except:
    #     errormessage = " (讀取錯誤!)"
    # # return render(request, 'home/item2.html',{"name": 'item2'}
    # return render(request, 'home/item2.html',locals())

    # objects.all()取得所有資料
    name = "item2"
    students = Music.objects.all().order_by('id')
    text_tse = serializers.serialize("json", Music.objects.all()) #
    time_test = datetime.now()
    #讀取資料表, 依 id 遞增排序(欄位前加入負號-id代表遞減排序)
    return render(request, "home/item2.html", locals())
