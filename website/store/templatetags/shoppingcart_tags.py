from django import template
from ..database.CartOps import cartLength
from ..database.getData import getProdImage
from ..models import ShoppingCart

register = template.Library()

@register.simple_tag()
def displayCart(sessionkey):
    length = cartLength(sessionkey)

    html = "<ul class='cartwrap'>"

    for e in ShoppingCart.objects.all().filter(session_key=sessionkey):
        #IMG - NAAM - AANTAL - PRIJS
        html += "<li class='cartitem'><div class='productcartimg'><img src='" + getProdImage(e.prodNum) + "' id='zoom_05' data-zoom-image='https://i.pinimg.com/736x/86/ff/e2/86ffe2b49daf0feed78a1c336753696d--black-panther-comic-digital-comics.jpg'></div>"
        html += "<div class='textplace'><button name='removeFromCartButton' value='" + str(e.prodNum) +"' class='remove'><i class='fa fa-trash' aria-hidden='true'></i><p>verwijderen</p></button><button class='movetowishlist'><i class='fa fa-heart' aria-hidden='true'></i><p>verplaats naar verlanglijstje</p></button><p class='title'>" + e.prodNum.prodName + "</p>"
        html += "<p>Aantal: " + str(e.amount) + "</p>"
        html += "<p>Prijs: €" + str(e.amount * e.prodNum.prodPrice) + "</p>"
        html += "</div></li>"

    html += "</ul>"
    return html


