from django import template

from store.models import OrderDetails
from store.models import Products
from store.models import ProductDetails
from ..database.AccountOps import *

register = template.Library()

@register.simple_tag()
def displayorders(request):
    print(getOrderAmount(request))
    if getOrderAmount(request) == 0:
        html = "Je hebt nog geen orders geplaatst bij ons."
    else:
        html = "<div class='table1'><table><tbody><tr><th>Order Nummer</th><th>Datum Geplaatst</th><th>Status</th></tr>"
        for e in Orders.objects.all().filter(customerID=Customers(request.user.id)):
            html = html + "<tr><td><a href='bestelling?ordernum=" + str(e.orderNum) +"'><i class='fa fa-external-link' aria-hidden='true'></i></a>" + str(e.orderNum) + "</td><td>" + str(e.orderDate) + "</td><td>" + e.orderStatus + "</td></tr>"
        html = html + "</tbody></table></div>"

    return html

@register.simple_tag()
def displayuser(request):
	object = Customers.objects.get(customerID = request.user.id)
	object2 = Address.objects.get(customerID = request.user.id)
	html = "<div class='table1'><table><tbody>"
	html += "<tr><th>Voornaam</th><td>{0}</td></tr><tr><th>Achternaam</th><td>{1}</td></tr><tr><th>Email</th><td>{2}</td></tr><tr><th style='border-bottom-left-radius: 5px;'>Adres</th><td>{3} {4} {5} {6}</td></tr>".format(object.name, object.surname, object.email, object2.address, str(object2.number), object2.city, str(object2.postalcode))
	html += "</tbody></table></div>"
	return html

@register.simple_tag()
def displayorderdetails(ordernum):
    ordernum = int(ordernum)
    object = Orders.objects.get(orderNum=ordernum)
    html = "<div class='table1'><table><tbody><tr><th>Ordernummer</th><td>" + str(ordernum) +"</td></tr><tr><th>Status</th><td>" + object.orderStatus + "</td></tr><tr><th style='border-bottom-left-radius: 5px; border: none;'>Datum</th><td>" + str(object.orderDate) + "</td></tr></tbody></table></div>"
    html += "</div><div class='aboutsection'><div class='table1'><table><tbody><tr><th style='border-top-left-radius: 5px; border: none;'>Productnummer</th><th>Naam</th><th>Prijs</th><th style='border-top-right-radius: 5px; border: none;'>Aantal</th></tr>"
    for e in OrderDetails.objects.all().filter(orderNum=ordernum):
        productEnt = Products.objects.get(prodNum=e.productNum.prodNum)
        productdetailEnt = ProductDetails.objects.get(prodNum=e.productNum.prodNum)
        html = html + "<tr><td>" + str(e.productNum) + "</td><td><a href='/product/" + str(productEnt.prodNum) + "'>" + "<img src='" + str(productdetailEnt.imageLink) +"'></a><p>" + str(productEnt.prodName) + "</p></td><td>€ " + str(productEnt.prodPrice) + "</td><td>" + str(e.amount) + "</td></tr>"
    html += "</tr></tbody></table></div>"
    return html
