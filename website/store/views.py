from django.core.mail import EmailMessage
from django.shortcuts import redirect
from django.shortcuts import render
from django.template.loader import get_template

from .database.DatabaseOps import insert
from .collections.forms import ContactForm


# Create your views here.

def index(request):
    return render(request, 'index.html')

def contact(request):
    formClass = ContactForm

    if request.method == 'POST':
        form = formClass(data=request.POST)

        if form.is_valid():
            contact_name = request.POST.get('contact_name', '')
            contact_email = request.POST.get('contact_email', '')
            contact_content = request.POST.get('content', '')

            template = get_template('mail/contact_template.txt')
            context = {
                    'contact_name' : contact_name,
                    'contact_email' : contact_email,
                    'contact_content' : contact_content,
                }

            content = template.render(context)

            email = EmailMessage(
                "Nieuwe contact aanvraag",
                content,
                "Comic Fire" + '',
                ['keyboardwarriorsinfo@gmail.com'],
                headers={'Reply-to' : contact_email}
            )
            email.send()
            return redirect('contact')

    return render(request, 'contact.html', {'form':formClass, })

def faq(request):
    insert()
    return render(request, 'faq.html')

def product(request):
    return render(request, 'product.html')

def product2(request, item):
    print(item)
    return render(request, 'product.html')
  
def testing(request):
    return render(request, 'testing.html')

