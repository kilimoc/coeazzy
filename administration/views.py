from django.http import HttpResponse
from django.shortcuts import render
from administration.forms import ClientForm
from django.views import  generic
from django.views.generic.edit import CreateView,UpdateView,DeleteView

from administration.models import Client

#generic views;
class IndexView(generic.ListView):
    template_name = 'administration/all_clients.html'
    context_object_name = 'client_list'

    def get_queryset(self):
        return Client.objects.all()
class DetailView(generic.DateDetailView):
    model = Client
    template_name = 'administration/client_details.html'

#This is the view to add new Client
class ClientCreate(CreateView):
    modal=Client
    fields = ['id_number','first_name','last_name','phone','email','username']

def clientProfile(request):
    return render(request,'administration/client_details.html')

# Create your views here.
def getHome(request):
    return render(request,'administration/home.html')
def getDashboard(request):
    return render(request,'administration/admin-dashboard.html')

def registerClient(request):
    return render(request,'administration/newClient.html')

#This view is to register a new Client.
def clientRegistration(request):
    #data={};
    if request.method=='POST':
        form=ClientForm(request.POST)
        if form.is_valid():
            idno=request.POST.get('id_number','')
            first_name=request.POST.get('first_name','')
            last_name = request.POST.get('last_name','')
            phone = request.POST.get('phone','')
            email = request.POST.get('email','')
            username=request.POST.get('username','')
            client=Client(id_number=idno,first_name=first_name,last_name=last_name,phone=phone,email=email,username=username)
            client.save()
            #data['success']='Sucessfullly Registered';
            #return HttpResponse(json.dumps(data), content_type="application/json")
            return HttpResponse("You are an official Registered Hostel Owner at CoEazzy");

    else:
        form=ClientForm()
    return render(request,'administration/newClient.html',{'form':form})

