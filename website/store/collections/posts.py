from django.shortcuts import redirect, render

from ..database.getData import queryVerbeterFunctie

def searchPost(request):
    filter = request.POST.get('filter')
    if filter != None:
        return redirect("/search/" + queryVerbeterFunctie(str(request.POST.get('searchtext'))) + "/" + filter)
    else:
        return redirect("/search/" + queryVerbeterFunctie(str(request.POST.get('searchtext'))) + "/items")
