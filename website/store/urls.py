from django.conf.urls import url
from . import views #from currect package import...

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^contact/$', views.contact, name='contact'), #url = ip/contact/ of ip/contact (de eerste / is niet nodig)
    url(r'^faq$', views.faq, name='faq'),
    url(r'^about$', views.about, name='about'),
    url(r'^product$', views.product, name='product'),
    url(r'^.well-known/$', views.index, name='.well-known'),
    url(r'^product/(?P<item>\d+)$', views.product2, name='product2'), #url = /product/{item}, \d+ betekent 1 nummer of meer
    url(r'^testing$', views.testing, name='testing'),
]
