from django import template
from ..database.AccountOps import *

register = template.Library()

@register.simple_tag()
def displayorders(request):
    print(getOrderAmount(request))
    if getOrderAmount(request) == 0:
        html = "Je hebt nog geen orders geplaatst bij ons."
    else:
        html = "<table><tbody><tr><td>Order Nummer</td><td>Datum Geplaatst</td><td>Status</td></tr>"
        for e in Orders.objects.all().filter(customerID=Customers(request.user.id)):
            html = html + "<tr><td>" + str(e.orderNum) + "</td><td>" + str(e.orderDate) + "</td><td>" + e.orderStatus + "</td></tr>"
        html = html + "</tbody></table>"

    return html