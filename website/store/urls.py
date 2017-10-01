from django.conf.urls import url
from . import views #from currect package import...

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^contact$', views.contact, name='contact'), #url = ip/contact (de eerste / is niet nodig)
    url(r'^faq$', views.faq, name='faq'),
    url(r'^product$', views.product, name='product'),
    url(r'^.well-known/$', views.index, name='.well-known'),
]
