from django.core.mail import EmailMessage
from django.shortcuts import redirect
from django.shortcuts import render
from django.template.loader import get_template
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from .database.getData import getProdName, getProdNum, getProdPrice, getProdStock, getProdGenre, getProdType, getProdAuthor, getProdDesc, getProdImage, getProdLanguage, getProdPublish, getProdRating, getProdTotalPages
from .collections.forms import ContactForm
from store.collections.forms import RegistrationForm


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
                "admin@comicfire.com",
                ['admin@comicfire.com'],
                headers={'Reply-to' : contact_email}
            )
            email.send()
            return redirect('contact')

    return render(request, 'contact.html', {'contact_form':formClass, })

def register(request):
    if request.method == 'POST':
        print("POST")
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/contact')
        else:
            return redirect('/register')
    else:
        print("Else!!!")
        form = RegistrationForm()
        return render(request, 'register.html', {'form': form})

def faq(request):
    return render(request, 'faq.html')

def product(request):
    return render(request, 'product.html')

def product2(request, item):
    productNumber = (int(item))
    prodName = getProdName(productNumber)
    prodPrice = getProdPrice(productNumber)
    prodStock = getProdStock(productNumber)
    prodGenre = getProdGenre(productNumber)
    prodType = getProdType(productNumber)
    prodPublisher = getProdPublish(productNumber)
    prodPages = getProdTotalPages(productNumber)
    prodLanguage = getProdLanguage(productNumber)
    prodRating = getProdRating(productNumber)
    prodAuthor = getProdAuthor(productNumber)
    prodDesc = getProdDesc(productNumber)
    prodImage = getProdImage(productNumber)
    return render(request, 'product2.html', {
        'prodNum' : productNumber,
        'prodName' : prodName,
        'prodPrice' : prodPrice,
        'prodStock' : prodStock,
        'prodGenre' : prodGenre,
        'prodType' : prodType,
        'prodPublisher' : prodPublisher,
        'prodPages' : prodPages,
        'prodLanguage' : prodLanguage,
        'prodRating' : range(prodRating),
        'prodAuthor' : prodAuthor,
        'prodDesc' : prodDesc,
        'prodImage' : prodImage,
    })
  
def testing(request):
    return render(request, 'testing.html')

def about(request):
    return render(request, 'about.html')

def logoutview(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('/')
    else:
        return redirect('/')

