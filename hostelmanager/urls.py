from django.conf.urls import url
from . import views

app_name='hostelmanager';

urlpatterns = [
    url(r'^$',views.getIndex,name='index' ),
    url(r'^services/',views.getHome,name='services' ),
    url(r'^about/', views.getAbout, name='about'),
]
