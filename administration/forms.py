from django import forms

class ClientForm(forms.Form):
    id_number=forms.IntegerField()
    first_name=forms.CharField(max_length=32)
    last_name=forms.CharField(max_length=32)
    phone=forms.CharField(max_length=14)
    email=forms.CharField(max_length=50)
    username=forms.CharField(max_length=50)
