from django import forms
from .models import Contact, Service

class ContactForm(forms.ModelForm):
    service = forms.ModelChoiceField(queryset=Service.objects.all(), empty_label="Select Service")
    
    class Meta:
        model = Contact
        fields = ['first_name', 'last_name', 'email', 'phone', 'kvk', 'website', 'service', 'remarks']