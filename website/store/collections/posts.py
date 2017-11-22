from django.shortcuts import redirect, render

from ..database.getData import queryVerbeterFunctie

def searchPost(request):
    query = request.POST.get('searchtext')
    filter = request.POST.get('filter')
    # if len(query) == 0:
    # return redirect('/')
    if filter != None:
        return redirect("/search/" + queryVerbeterFunctie(str(request.POST.get('searchtext'))) + "/" + filter)
    else:
        return redirect("/search/" + queryVerbeterFunctie(str(request.POST.get('searchtext'))) + "/items")
