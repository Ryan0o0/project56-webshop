from django.shortcuts import render
from forms import ContactForm


# Create your views here.

def index(request):
    return render(request, 'index.html')

def contact(request):
    form = ContactForm()
    return render(request, 'contact.html', {'form':form, })


def faq(request):
    return render(request, 'faq.html')
