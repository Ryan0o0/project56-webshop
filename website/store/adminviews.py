import datetime

from chartit import PivotChart
from chartit import PivotDataPool
from django.db.models import Sum, Avg
from django.shortcuts import render, redirect
from store.collections.adminforms import AdminRegistrationForm, ProductsRegistrationForm
from django.http import HttpResponse
from django.contrib.auth.models import User
from chartit import DataPool, Chart
from .models import OrderDetails

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
        AddressData = Address.objects.get(customerID=userid)
        UserData = Customers.objects.get(customerID=userid)
        Data = {'address' : AddressData.address, 'number' : AddressData.number, 'city' : AddressData.city, 'postalcode' : AddressData.postalcode, 'name': UserData.name, 'surname': UserData.surname, 'telephone': UserData.telephone}
        user_form = EditUserForm(initial=Data)
        return render(request, 'admin/edituser.html', {
            'userid': userid,
            'user_form': user_form,
        })

    def post(self, request, userid):
        if 'deleteuser' in request.POST:
            deleteUser(request)
            return render(request, 'admin/userdeleted.html', {
                'userid': userid,
            })
        if 'edituser' in request.POST:
            user_form = EditUserForm(request.POST)
            print(user_form)
            if user_form.is_valid():
                editUser(request, userid)
                return redirect('/admin/searchusers/')
            return render(request, 'admin/edituser.html', {'userid': userid, 'user_form': user_form})

def createproduct(request):
    if request.method == 'POST':
        form = ProductsRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/admin/')
    else:
        form = ProductsRegistrationForm()
    return render(request, 'admin/createproduct.html', {'form' :  form})

class ProductGraph(View):
    def get(self, request, year, month):
        ordersData = Orders.objects.filter(orderDate__year__icontains=int(year))
        productBarData = PivotDataPool(
            series=[{
                'options': {
                    'source': OrderDetails.objects.all().filter(orderNum__in=ordersData),
                    'categories': ['productNum'],
                    'legend_by': 'productNum',
                    'top_n_per_cat': 5,
                },
                'terms': {
                    'aSum': Sum('productNum')}
            }]
        )
        productBar = PivotChart(
            datasource=productBarData,
            series_options=[{
                'options': {
                    'type': 'column',
                    'stacking': True
                },
                'terms': ['aSum']
            }],
            chart_options={
                'title': {
                    'text': 'Products per amount'
                },
                'xAxis': {
                    'title': {
                        'text': 'Product'
                    }
                }
            }
        )
        print(productBar.datasource.cv_raw)
        return render(request, 'admin/productdata.html', {
            'graph' : productBar,
        })