from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    print('*'*10)
    print('*'*9)
    print('*'*8)
    print('*'*7)
    print('*'*6)
    print('*'*5)
    return HttpResponse("You're voting on question %s.")

def templateRend(request): 
    return render(request, 'index.html')   