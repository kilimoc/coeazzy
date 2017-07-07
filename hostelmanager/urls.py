from django.conf.urls import url
from . import views

app_name='hostelmanager';

urlpatterns = [
    url(r'^$',views.getIndex,name='index' ),
    url(r'^services/',views.getHome,name='services' ),
    url(r'^products/', views.renderProducts, name='products'),
    url(r'^about/', views.getAbout, name='about'),
    url(r'^login/', views.user_login, name='login'),
    url(r'^header/', views.getHeader, name='header'),

    #Dashboard
    url(r'^dashboard/', views.getDashboard, name='dashboard'),
    #New Hostel
    url(r'^hostel/add/$', views.HostelCreate.as_view(), name='hostel-add'),
      #All Hostels
    url(r'^all_hostels/$',views.RegisteredHostels.as_view(), name='all-hostels'),

    #Get specific Hostel Detail
    url(r'^hostel_report/', views.getSpecificHostelReport.as_view(), name='hostelreport'),

]
