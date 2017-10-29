from django.db.models import Max

from ..models import Orders, OrderDetails, ShoppingCart, Customers
from django.utils import timezone
from .CartOps import clearCart

def createOrder(request):
    date = timezone.now().date()
    status = "Processed"

    if not request.user.is_authenticated:
        custID = createCustomer(request)
    else:
        custID = request.user.id

    orderEntry = Orders(orderNum=getNewOrderNum(), orderDate=date, orderStatus=status, customerID=Customers(customerID=custID))
    orderEntry.save()
    for e in ShoppingCart.objects.all().filter(session_key=request.session.session_key):
        orderDetailsEntry = OrderDetails(amount=e.amount, orderNum=Orders(orderNum=orderEntry.orderNum), productNum=e.prodNum)
        orderDetailsEntry.save()
    clearCart(request)

def getNewOrderNum():
    maxC = Orders.objects.all().aggregate(Max('orderNum'))
    if maxC.get('orderNum__max') == None:
        return 1
    else:
        return maxC.get('orderNum__max') + 1

def createCustomer(request):
    customerEntry = Customers(customerID=getNewCustomerNum(), email=request.session['customer_email'], name=request.session['customer_fname'], surname=request.session['customer_lname'], telephone=request.session['customer_phone'], isRegistered=False)
    customerEntry.save()
    return customerEntry.customerID

def getNewCustomerNum():
    maxC = Customers.objects.all().aggregate(Max('customerID'))
    if maxC.get('customerID__max') == None:
        return 1
    else:
        return maxC.get('customerID__max') + 1