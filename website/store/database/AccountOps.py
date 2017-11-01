from ..models import Address, Customers


def saveAddress(request):
    account_address = request.POST.get('address', '')
    account_number = request.POST.get('number', '')
    account_city = request.POST.get('city', '')
    account_postalcode = request.POST.get('postalcode', '')

    account = Address(customerID=Customers(request.user.id), address=account_address, number=account_number, city=account_city, postalcode=account_postalcode)
    account.save()

def saveCustomerInfo(request):
    account_name = request.POST.get('name', '')
    account_surname = request.POST.get('surname', '')
    account_telephone = request.POST.get('telephone', '')

    accountinfo = Customers(customerID=Customers(request.user.id), email=request.session['customer_email'], name=account_name, surname=account_surname, telephone=account_telephone, isRegistered=True)
    accountinfo.save()
