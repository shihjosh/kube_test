from django.shortcuts import render,HttpResponse

# Create your views here.
def core(request):
    return render(request, 'home/home.html')

def other(request):
    return render(request, 'home/other.html')