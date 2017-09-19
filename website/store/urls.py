from django.conf.urls import url
from . import views #from currect package import...

urlpatterns = [
    url(r'^$', views.index, name='index')
]