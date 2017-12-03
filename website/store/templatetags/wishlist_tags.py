from django import template
from ..database.WishListOps import listLength
from ..database.getData import getProdImage
from ..models import WishList, Customers


register = template.Library()

@register.simple_tag()
def wishListItems(sessionkey):
    return WishList.objects.all().filter(custId=sessionkey)

@register.simple_tag()
def displayWishListItem(e):
    html = "<div class='productcartimg'>"
    html += "<a href='/product/" + str(e.productNum.prodNum) + "'><img src='" + getProdImage(e.productNum.prodNum) + "' id='zoom_05' data-zoom-image='https://i.pinimg.com/736x/86/ff/e2/86ffe2b49daf0feed78a1c336753696d--black-panther-comic-digital-comics.jpg'></a></div>"
    html += "<div class='textplace'><button name='removeFromWishListButton' value='" + str(e.productNum.prodNum) + "' class='remove'><i class='fa fa-trash' aria-hidden='true'></i><p>Verwijderen</p></button><button name='addToCartButton' value='" + str(e.productNum.prodNum) + "' class='movetowishlist'><i class='fa fa-shopping-cart' aria-hidden='true'></i><p>Toevoegen aan winkelwagentje</p></button><p class='title'>" + e.productNum.prodName + "</p>"
    html += "</div>"
    return html

@register.simple_tag()
def wishListEmpty(id):
    if WishList.objects.filter(custId=id).count() == 0:
        return True
    else:
        return False

