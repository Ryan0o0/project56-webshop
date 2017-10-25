from django import template
from ..database.WishListOps import listLength
from ..database.getData import getProdImage
from ..models import WishList, Customers


register = template.Library()

@register.simple_tag()
def displayList(userid):
    length = listLength(userid)
    if length == 0:
        html = "<p class='title'>Momenteel zit er nog niks in je verlanglijst.</p>"
    else:
        html = "<ul class='cartwrap'>"
        for e in WishList.objects.all().filter(custId=Customers(userid)):
            html += "<li class='cartitem'><div class='productcartimg'><a href='/product/" + str(e.productNum.prodNum) + "'><img src='" + getProdImage(e.productNum.prodNum) + "' id='zoom_05' data-zoom-image='https://i.pinimg.com/736x/86/ff/e2/86ffe2b49daf0feed78a1c336753696d--black-panther-comic-digital-comics.jpg'></a></div>"
            html += "<div class='textplace'><button name='removeFromWishListButton' value='" + str(e.productNum) +"' class='remove'><i class='fa fa-trash' aria-hidden='true'></i><p>verwijderen</p></button><p class='title'>" + e.productNum.prodName + "</p>"
            html += "</div></li>"

        # .... loop

        html += "</ul>"

    return html


