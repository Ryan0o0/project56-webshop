from django.core.mail import EmailMessage
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.template.loader import render_to_string
from store.tokens import account_activation_token
from django.contrib.auth.models import User
from django.template.loader import get_template
from django.contrib.auth import login, logout
from .database.getData import getProdName, getProdPrice, getProdStock, getProdGenre, getProdType, getProdAuthor, getProdDesc, getProdImage, getProdLanguage, getProdPublish, getProdRating, getProdTotalPages, getProdData
from .database.verifyData import verifyProdNum
from .collections.forms import ContactForm, RegistrationForm, LogginginForm, CheckoutForm, CustomerDetails, AccountForm
from django.http import *
from .database.getData import getResult2
from django.contrib.auth import authenticate
from .database.CartOps import addToCart, removeFromCart
from .database.WishListOps import addToWishList, removeFromWishList
from .requests.posts import *
from .database.CheckoutOps import *
from .database.AccountOps import *

# Create your views here.

def index(request):
    if request.method == 'POST':
        if 'searchtext' in request.POST:
            return searchPost(request)

    return render(request, 'index.html')

def contact(request):
    formClass = ContactForm

    if request.method == 'POST':
        if 'searchtext' in request.POST:
            return searchPost(request)
        elif 'contactsubmitbutton' in request.POST:
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
                    'noreply@comicfire.com',
                    ['admin@comicfire.com'],
                    headers = {'Reply-to': contact_email}
                )
                email.send()
                return redirect('messagesend')

    return render(request, 'contact.html', {'contact_form':formClass, })

def register(request):
    args = {}
    if request.method == 'POST':
        if 'searchtext' in request.POST:
            return searchPost(request)
        elif 'registerbutton' in request.POST:
            form = RegistrationForm(request.POST)
            if form.is_valid():
                user = form.save(commit=False)
                user.is_active = False
                user.save()
                current_site = get_current_site(request)
                message = render_to_string('mail/acc_active_email.html', {
                    'user': user,
                    'domain': current_site.domain,
                    'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                    'token': account_activation_token.make_token(user),
                })
                mail_subject = 'Activate your blog account'
                to_email = form.cleaned_data.get('email')
                email = EmailMessage(mail_subject, message, to=[to_email])
                email.send()
                # form.save()
                return render(request, 'completeregistration.html')
    else:
        form = RegistrationForm()
    args['form'] = form
    return render(request, 'register.html', args)

def faq(request):
    if request.method == 'POST':
        if 'searchtext' in request.POST:
            return searchPost(request)

    return render(request, 'faq.html')

def about(request):
    if request.method == 'POST':
        if 'searchtext' in request.POST:
            return searchPost(request)

    return render(request, 'about.html')

def product(request, item):
    if request.method == 'POST':
        if 'searchtext' in request.POST:
            return searchPost(request)
        elif "addToCartButton" in request.POST:
            print("Adding to cart")
            if not request.session.exists(request.session.session_key):
                print("Creating session...")
                request.session.create()
            addToCart(request, item)
            return redirect('/winkelwagentje/')
        elif "addtowishlistButton" in request.POST:
            addToWishList(request, item)
            return redirect('/verlanglijst/')

    if not verifyProdNum(item):
        return render(request, 'productnietgevonden.html')

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
    prodDate = getProdData(productNumber)
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
        'prodDate' : prodDate,
    })

def search(request, query):
    thequery = query
    return render(request, 'testing.html', {
        'query' : thequery,
    })

def logoutview(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('/')
    else:
        return redirect('/')



def loginview(request):
    args = {}
    if request.method == "POST":
        if 'searchtext' in request.POST:
            return searchPost(request)
        elif 'loginbutton' in request.POST:
            form = LogginginForm(request.POST)
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
    else:
        form = LogginginForm()
    args['form'] = form
    return render(request, 'login.html', args)

def registrationcomplete(request):
    if request.method == "POST":
        if 'searchtext' in request.POST:
            return searchPost(request)
    return render(request, 'completeregistration.html')

def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        # return redirect('home')
        return render(request, 'completeregistration.html')
    else:
        return HttpResponse('Activation link is invalid!')

def contactRequestHandeld(request):
    if request.method == "POST":
        if 'searchtext' in request.POST:
            return searchPost(request)
    return render(request, 'mailsend.html')

def results(request, query):
    #returnPage(request.GET.get('searchtext'))
    object = getResult2(query)
    print(object)
#    prodName = getProdName()
 #   prodPrice = getProdPrice()
  #  prodStock = getProdStock()
   # prodAuthor = getProdAuthor()
    return render(request, 'testing.html')

def shoppingcart(request):
    if request.method == 'POST':
        if 'searchtext' in request.POST:
            return searchPost(request)
        elif 'removeFromCartButton' in request.POST:
            removeFromCart(request, int(request.POST.get('removeFromCartButton')))
            return redirect('/winkelwagentje/')
        elif "moveToWishListButton" in request.POST:
            addToWishList(request, int(request.POST.get('moveToWishListButton')))
            return redirect('/verlanglijst/')
        elif 'placeorderbutton' in request.POST:
            return redirect('/processorder/')

    return render(request, 'shoppingcart.html')

def wishlist(request):
    if not request.user.is_authenticated:
        return redirect('/')

    if request.method == 'POST':
        if 'searchtext' in request.POST:
            return searchPost(request)
        elif 'removeFromWishListButton' in request.POST:
            removeFromWishList(request, int(request.POST.get('removeFromWishListButton')))
            return redirect('/verlanglijst/')
    return render(request, 'wishlist.html')

def processOrder(request):
    if not request.META.get('HTTP_REFERER') is None:
        if '/winkelwagentje/' in request.META.get('HTTP_REFERER') or '/processorder/' in request.META.get('HTTP_REFERER'):
            if request.user.is_authenticated:
                return redirect('/checkout/')
            else:
                args = {}
                if request.method == 'POST':
                    if 'loginbutton' in request.POST:
                        form = LogginginForm(request.POST)
                        username = request.POST['username']
                        password = request.POST['password']
                        user = authenticate(request, username=username, password=password)
                        if user is not None:
                            login(request, user)
                            return redirect('/checkout/')
                        else:
                            args['form'] = form
                            return render(request, 'processorder.html', args)
                else:
                    form = LogginginForm()
                args['form'] = form
                return render(request, 'processorder.html', args)
    else:
        return redirect('/')

def customerdetails(request):
    args = {}
    if not request.META.get('HTTP_REFERER') is None:
        if '/processorder/' in request.META.get('HTTP_REFERER') or '/customerdetails/' in request.META.get('HTTP_REFERER'):
            if request.method =='POST':
                if 'customerdetailssubmitbutton' in request.POST:
                    form = CustomerDetails(data=request.POST)

                    if form.is_valid():
                        request.session['customer_fname'] = request.POST.get('customer_fname', '')
                        request.session['customer_lname'] = request.POST.get('customer_lname', '')
                        request.session['customer_email'] = request.POST.get('customer_email', '')
                        request.session['customer_phone'] = request.POST.get('customer_phone', '')
                        return redirect('/checkout/')
            else:
                form = CustomerDetails()
            args['customerdetailsform'] = form
            return render(request, 'customerdetails.html', args)
        else:
            return redirect('/')
    return redirect('/')

def checkout(request):
    args = {}
    if not request.META.get('HTTP_REFERER') is None:
        if '/customerdetails/' in request.META.get('HTTP_REFERER') or '/checkout/' in request.META.get('HTTP_REFERER') or ('/winkelwagentje/' in request.META.get('HTTP_REFERER') and request.user.is_authenticated) or ('/processorder/' in request.META.get('HTTP_REFERER') and request.user.is_authenticated):
            print("Getting stuck here for some fucked reason")
            if request.method =='POST':
                if 'checkoutsubmitbutton' in request.POST:
                    form = CheckoutForm(data=request.POST)

                    if form.is_valid():
                        print("Placing order... stand by")
                        createOrder(request)
                        return redirect('/contact/')
            else:
                form = CheckoutForm()
            args['checkoutform'] = form
            return render(request, 'checkout.html', args)
        else:
            return redirect('/')
    print("Doing this one...")
    return redirect('/')

def account(request):
    return render(request, 'account.html')

def accountedit(request):
    if not request.user.is_authenticated:
        return redirect('/')
    else:
        if request.method == 'POST':
            account_form = AccountForm(request.POST, instance=request.user)
            if account_form.is_valid():
                saveAdress(request)
                return redirect('/account/')
            else:
                print("error")
        else:
            account_form = AccountForm()

        return render(request, 'accountedit.html', {
            'account_form': account_form,
        })


