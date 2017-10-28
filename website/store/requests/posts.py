from django.shortcuts import redirect, render

def searchPost(request):
    return redirect("/search/" + (str(request.POST.get('searchtext'))))
