from ..models import WishList, Products, Customers


def addToWishList(request, prodnum):

    if not checkIfExists(request, prodnum):
        item = WishList(custId=Customers(request.user.id), productNum=Products(prodNum=prodnum))
        item.save()

def checkIfExists(request, prodnum):
    return WishList.objects.filter(custId=Customers(request.user.id), productNum=Products(prodNum=prodnum)).exists()

def listLength(userid):
    return WishList.objects.all().filter(custId=Customers(userid)).count()

def removeFromWishList(request, prodnum):
    WishList.objects.filter(custId=Customers(request.user.id), productNum=Products(prodNum=prodnum)).delete()
