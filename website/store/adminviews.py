from django.shortcuts import render, redirect
from store.collections.adminforms import AdminRegistrationForm
from django.http import HttpResponse
from django.contrib.auth.models import User

#Admin index - comicfire.com/admin/
from django.views import View

from store.database.adminGetData import ifUserExists
from django.contrib.auth import login, logout, update_session_auth_hash
from .collections.tools import *
from .collections.forms import *
from .database.AccountOps import *
from .collections.posts import *
from django.contrib.auth import authenticate

def admin(request):
    args = {}
    if request.method == "POST":
        print(request.POST)
        if 'loginbutton' in request.POST:
            form = LogginginForm(request.POST)
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/admin')
    else:
        form = LogginginForm()
    args['form'] = form
    return render(request, 'admin/admin.html', args)

#De searchusers functie -> zoekt users aan de hand van ID of naam
def searchusers(request):
    if request.method == 'GET':
        if 'query' in request.GET:
            return searchusersresults(request)
    return render(request, 'admin/searchuser.html')

#De result pagina van de searchusers functie
def searchusersresults(request):
    getUserPar = request.GET['query']
    return render(request, 'admin/searchuser.html', {
        'query' : getUserPar,
    })

def createuser(request):
    if request.method == 'POST':
        form = AdminRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/admin/')
    else:
        form = AdminRegistrationForm()
    return render(request, 'admin/createuser.html', {'form' :  form})

#Class based view instead of Function based view
class EditUser(View):
    def get(self, request, userid):
        return render(request, 'admin/edituser.html', {
            'userid': userid,
        })
    def post(self, request, userid):
        if 'deleteuser' in request.POST:
            deleteUser(request)
            return render(request, 'admin/userdeleted.html', {
                'userid': userid,
            })

