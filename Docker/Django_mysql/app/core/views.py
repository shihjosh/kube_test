from django.shortcuts import render,HttpResponse

# Create your views here.
def core(request):
    return render(request, 'home/home.html' ,{})

def other(request):
    return render(request, 'home/other.html',{})

def item1(request):
    return render(request, 'home/item1.html',{"name": 'Dashboard'})

def item2(request):
    return render(request, 'home/item2.html',{"name": 'item2'})
