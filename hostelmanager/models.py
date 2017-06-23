from django.db import models

# Create your models here.
class HostelOwner(models.Model):
    idno=models.IntegerField(primary_key=True,max_length=8)
    first_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)
    phone=models.CharField(unique=True,max_length=14)
    email=models.CharField(unique=True,null=True,max_length=32)

    def __str__(self):
        return self.first_name

