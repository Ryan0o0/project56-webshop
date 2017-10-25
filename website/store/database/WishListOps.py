from ..models import WishList, Products


def addToWishList(request, prodnum):

    if not checkIfExists(request, prodnum):
        item = WishList(custId=request.user.id, productNum=Products(prodNum=prodnum))
        item.save()
    else:
        incrementEntry(request, prodnum)

def checkIfExists(request, prodnum):
    return WishList.objects.filter(custId=request.user.id, productNum=Products(prodNum=prodnum)).exists()

def incrementEntry(request, prodnum):
    existingEntry = WishList.objects.get(custId=request.user.id, productNum=Products(prodNum=prodnum))
    existingEntry.save()

def listLength(request):
    return WishList.objects.all().filter(custId=request.user.id).count()

def removeFromWishList(request, prodnum):
    WishList.objects.filter(custId=request.user.id, productNum=Products(prodNum=prodnum)).delete()
