from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Hostel
from django.views.generic.edit import CreateView
from django.views import generic
from .forms import LoginForm

# Create your views here.

def getIndex(request):
    return render(request,'hostelmanager/home.html')
def getHome(request):
    return render(request,'hostelmanager/services.html')

def getAbout(request):
    return render(request,'hostelmanager/about.html')
def getLogin(request):
    return render(request, 'hostelmanager/login.html')

def getDashboard(request):
    return render(request,'hostelmanager/hostelmanager-dashboard.html')
def renderHostels(request):
    return render(request,'hostelmanager/all_hostels.html')

#New object to database.
class HostelCreate(CreateView):
    model = Hostel
    fields=['owner_id','hostel_id','hostel_name','location','rooms','rent']

#Get all the registered Hostels.
class RegisteredHostels(generic.ListView):
    context_object_name = 'all_hostels'
    template_name = 'hostelmanager/all_hostels.html'

    def get_queryset(self):
        return Hostel.objects.all()


#This view is required to log the user in
def user_login(request):
    if request.method=='POST':
        form=LoginForm(request.POST)

        if form.is_valid():
            cd=form.cleaned_data
            user=authenticate(username=cd['username'],password=cd['password'])

            if user is not None:
                if user.is_active:
                    login(request,user)
                    return redirect('hostelmanager:dashboard',)
                else:
                    return HttpResponse('Disabled Account')
            else:
                return HttpResponse('Invalid Login')
    else:
        form=LoginForm()
    return render(request,'hostelmanager/login.html',{'form':form})