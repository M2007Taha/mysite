from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect

def home(request):
    
    return render(request,'home.html')
def page1(request):
    return render(request,'page1.html')
def page2(request):
    return render(request,'page2.html')
def about(request):
    return render(request,'about.html')
def login(request):
    return render(request,'login.html')
