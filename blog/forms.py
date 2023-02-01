from django import forms
from .models import Contact

#Creates a form that allows users to contact the website host
class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'