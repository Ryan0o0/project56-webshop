from ..models import Products

def insert():
    b = Products(prodNum=3, prodName="TestInsert", prodPrice=34.45, prodStock=334)
    b.save()