from ..models import Address, Customers
from ..collections.forms import AccountForm

def saveAdress(request):
    account_address = request.POST.get('address', '')
    account_number = request.POST.get('number', '')
    account_city = request.POST.get('city', '')
    account_postalcode = request.POST.get('postalcode', '')

    account = Address(customerID=Customers(request.user.id), address=account_address, number=account_number, city=account_city, postalcode=account_postalcode)
    account.save()
