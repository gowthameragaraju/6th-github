from django.shortcuts import render

# Create your views here.
def second(request):
    d={'name':'GOWTHAM','loc':'NELLORE'}
    return render(request,'string.html',d)