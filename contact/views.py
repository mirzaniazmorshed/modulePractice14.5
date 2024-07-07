from django.shortcuts import render
from . import forms
# Create your views here.
def contact(request):
    contact_form = forms.ContactForm()
    return render(request, 'contact.html', {'form': contact_form})