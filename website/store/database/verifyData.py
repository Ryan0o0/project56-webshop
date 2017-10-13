from ..models import Products

def verifyProdNum(prodNumber):
    bool = Products.objects.filter(prodNum=prodNumber).exists()
    return bool
