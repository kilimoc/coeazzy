from django.shortcuts import render

# Create your views here.

def getIndex(request):
    return render(request,'hostelmanager/index.html')
def getHome(request):
    return render(request,'hostelmanager/home.html')

def getAbout(request):
    return render(request,'hostelmanager/about.html')
