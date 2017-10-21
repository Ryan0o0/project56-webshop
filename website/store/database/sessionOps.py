from ..models import ShoppingCart

def updateCartKeys(oldkey, newkey):
    for e in ShoppingCart.objects.all().filter(session_key=oldkey):
        ne = e
        ne.session_key = newkey
        ne.save()
