from django import template
from ..database.CartOps import cartLength
from ..database.getData import getProdImage
from ..models import ShoppingCart

register = template.Library()

@register.simple_tag()
def displayCart(sessionkey):
    length = cartLength(sessionkey)

    html = ""

    for e in ShoppingCart.objects.all().filter(session_key=sessionkey):
        #IMG - NAAM - AANTAL - PRIJS
        html += "<img src='" + getProdImage(e.prodNum) + "' id='zoom_05' data-zoom-image='https://i.pinimg.com/736x/86/ff/e2/86ffe2b49daf0feed78a1c336753696d--black-panther-comic-digital-comics.jpg' style='width:150px;height:160px;'>"
        html += " " + e.prodNum.prodName
        html += " Aantal: " + str(e.amount)
        html += " Prijs: " + str(e.amount * e.prodNum.prodPrice)

        html += "<br/>"
    return html


