from django.conf.urls import url
from . import views #from currect package import...
from django.contrib.auth.views import login
urlpatterns = [
    # url(r'^$', login, {'template_name': 'index.html'}, name='index'),
    url(r'^$', login, {'template_name': 'index.html'}, name='index'),
    url(r'^register/$', views.register, name="register"),
    url(r'^contact/$', views.contact, name='contact'), #url = ip/contact/ of ip/contact (de eerste / is niet nodig)
    url(r'^faq$', views.faq, name='faq'),
    url(r'^product$', views.product, name='product'),
    url(r'^about$', views.about, name='about'),
    url(r'^product/(?P<item>\d+)$', views.product2, name='product2'), #url = /product/{item}, \d+ betekent 1 nummer of meer
    url(r'^testing$', views.testing, name='testing'),
    url(r'^logout/$', views.logoutview, name='logout'),
]
