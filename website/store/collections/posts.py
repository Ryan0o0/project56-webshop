from django.shortcuts import redirect, render

from store.database.WishListOps import addToWishList
from ..database.getData import queryVerbeterFunctie

def searchPost(request):
    filter = request.POST.get('filter')
    if filter != None:
        return redirect("/search/" + queryVerbeterFunctie(str(request.POST.get('searchtext'))) + "/" + filter)
    else:
        return redirect("/search/" + queryVerbeterFunctie(str(request.POST.get('searchtext'))) + "/items")

def addToWishListPost(request):
    addToWishList(request, int(request.POST.get('moveToWishListButton')))
    return redirect('/verlanglijst/')