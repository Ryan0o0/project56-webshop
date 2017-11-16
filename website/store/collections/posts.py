from django.shortcuts import redirect, render

from ..database.getData import queryVerbeterFunctie

def searchPost(request):
    query = request.POST.get('searchtext')
    if len(query) == 0:
        return redirect('/')
    return redirect("/search/" + queryVerbeterFunctie(str(request.POST.get('searchtext'))))
