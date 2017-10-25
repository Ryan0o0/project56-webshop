from django import template
from ..database.WishListOps import listLength
from ..database.getData import getProdImage
from ..models import WishList, Customers


register = template.Library()

@register.simple_tag()
def displayList(request):
    length = listLength(request.user.id)
    print(length)
    if length == 0:
        html = "<p class='title'>Momenteel zit er nog niks in je winkelwagentje.</p>"
    else:
        html = "<ul class='cartwrap'>"
        cnt = 0
        for e in WishList.objects.all().filter(custId=Customers.customerID):

            #IMG - NAAM - AANTAL - PRIJS
            html += "<li class='cartitem'><div class='productcartimg'><img src='" + getProdImage(e.prodNum) + "' id='zoom_05' data-zoom-image='https://i.pinimg.com/736x/86/ff/e2/86ffe2b49daf0feed78a1c336753696d--black-panther-comic-digital-comics.jpg'></div>"
            html += "<div class='textplace'><button name='removeFromListButton' value='" + str(e.prodNum) +"' class='remove'><i class='fa fa-trash' aria-hidden='true'></i><p>verwijderen</p></button><button class='movetowishlist'><i class='fa fa-heart' aria-hidden='true'></i><p>verplaats naar verlanglijstje</p></button><p class='title'>" + e.prodNum.prodName + "</p>"
            html += "<p>Prijs: €" + str(e.amount * e.prodNum.prodPrice) + "</p>"
            html += "</div></li>"
            cnt += 1
        html += "</ul>"

    return html


