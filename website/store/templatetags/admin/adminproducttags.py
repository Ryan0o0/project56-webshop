from django import template
from django.db.models import QuerySet
from ...collections.tools import *
from django.contrib.auth.models import User
from ...database.adminGetData import *
from django.shortcuts import *

register = template.Library()

@register.simple_tag()
def productFound(query):
    #Deze functie checkt simpelweg of er wel een user is die overeenkomt met de ID of Naam
    return ifProductExists(query)


