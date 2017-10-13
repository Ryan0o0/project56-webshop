from ..models import Products

def verifyProdNum(prodNumber):
    return Products.objects.filter(prodNum=prodNumber).exists()
