from django.db import models
from django.core.urlresolvers import reverse

from administration.models import Client

# Create your models here.
class HostelOwner(models.Model):
    idno=models.IntegerField(primary_key=True)
    first_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)
    phone=models.CharField(unique=True,max_length=14)
    email=models.CharField(unique=True,null=True,max_length=32)

    def __str__(self):
        return self.first_name



class Hostel(models.Model):
    owner_id=models.ForeignKey(Client,on_delete=models.CASCADE)
    hostel_id=models.AutoField(primary_key=True)
    hostel_name=models.CharField(max_length=30)
    location=models.CharField(max_length=30)
    rooms=models.IntegerField()
    rent=models.DecimalField(max_digits=7,decimal_places=2,default=00)

    def get_absolute_url(self):
        reverse('hostelmanager:dashboard',)



    def __str__(self):
        return self.hostel_name



