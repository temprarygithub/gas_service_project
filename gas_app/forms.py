from django import forms
from .models import Service_requests , Support_Representative

class Service_Request_Form(forms.ModelForm):
    class Meta:
        model = Service_requests
        fields = ['service_type', 'description', 'files']

class Track_Status_Form(forms.Form):
    account_number = forms.CharField(max_length=20)

class SupportRepresentativeForm(forms.ModelForm):
    class Meta:
        model = Support_Representative
        fields = ['name', 'username', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }