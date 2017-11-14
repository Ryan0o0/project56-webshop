from django.shortcuts import redirect, render

from website.store.database.getData import queryVerbeterFunctie


def searchPost(request):
    return redirect("search/" + queryVerbeterFunctie(str(request.POST.get('searchtext'))))
