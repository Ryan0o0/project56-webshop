from django import template
from ..database.AccountOps import *

register = template.Library()

@register.simple_tag()
def displayorders(request):
    print(getOrderAmount(request))
    if getOrderAmount(request) == 0:
        html = "Je hebt nog geen orders geplaatst bij ons."
    else:
        html = "<table><tbody><tr><th>Order Nummer</th><th>Datum Geplaatst</th><th>Status</th></tr>"
        for e in Orders.objects.all().filter(customerID=Customers(request.user.id)):
            html = html + "<tr><td>" + str(e.orderNum) + "</td><td>" + str(e.orderDate) + "</td><td>" + e.orderStatus + "</td></tr>"
        html = html + "</tbody></table>"

    return html

@register.simple_tag()
def displayuser(request):
	object = Customers.objects.get(customerID = request.user.id)
	object2 = Address.objects.get(customerID = request.user.id)
	html = "<table><tbody>"
	html += "<tr><th>Voornaam</th><td>{0}</td></tr><tr><th>Achternaam</th><td>{1}</td></tr><tr><th>Email</th><td>{2}</td></tr><tr><th style='border-bottom-left-radius: 5px;'>Adres</th><td>{3} {4} {5} {6}</td></tr>".format(object.name, object.surname, object.email, object2.address, str(object2.number), object2.city, str(object2.postalcode))
	html += "</tbody></table>"
	return html
