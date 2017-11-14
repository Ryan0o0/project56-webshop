from django import template
from ..database.AccountOps import *

register = template.Library()

@register.simple_tag()
def displayorders(request):
    print(getOrderAmount(request))
    if getOrderAmount(request) == 0:
        html = "Je hebt nog geen orders geplaatst bij ons."
    else:
        html = "<ul>"
        for e in Orders.objects.all().filter(customerID=Customers(request.user.id)):
            html = html + "<li> Order nummer: " + str(e.orderNum) + " Geplaatst op: +" + str(e.orderDate) + " Status: " + e.orderStatus + "</li>"
        html = html + "</ul>"

    return html