from django.shortcuts import render
# Create your views here.

def index(request):
    return render(request,'icGridApp/index.html')

def nextpage(request):
    return render(request,'icGridApp/next.html')

def previouspage(request):
    return render(request,'icGridApp/previous.html')

