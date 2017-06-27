from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.

class Client(models.Model):
    id_number=models.IntegerField(primary_key=True)
    first_name=models.CharField(max_length=32)
    last_name=models.CharField(max_length=32)
    phone=models.CharField(max_length=14)
    email=models.CharField(max_length=50)
    username=models.CharField(max_length=50)

    def get_absolute_url(self):
        return reverse('administrator:detail',kwargs={'pk':self.pk})

    def __str__(self):
        return self.first_name
