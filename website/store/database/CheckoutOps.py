from django.db.models import Max

from ..models import Orders, OrderDetails, ShoppingCart
from django.utils import timezone
from .CartOps import clearCart

def createOrder(request):
    date = timezone.now().date()
    status = "Processed"
    orderEntry = Orders(orderNum=getNewOrderNum(), orderDate=date, orderStatus=status)
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