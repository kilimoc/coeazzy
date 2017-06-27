


from django.conf.urls import url
from . import views

app_name='administration';

urlpatterns = [
    url(r'^$',views.getHome,name='home'),
    url(r'^dashboard/',views.getDashboard,name='dashboard'),
    url(r'^client_registration/',views.registerClient,name='newclient'),
    url(r'^newclient/',views.clientRegistration,name='registerclient'),
    url(r'^allclients/',views.IndexView.as_view(),name='allclients'),

    url(r'^(?P<pk>[0-9]+)/$',views.DetailView.as_view(),name='detail'),
   #Add new Client To the new site
   url(r'^client/add/$',views.ClientCreate.as_view(),name='client-add'),




]
