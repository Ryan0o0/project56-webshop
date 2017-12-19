from django import template
from ...database.adminGetData import *

register = template.Library()

@register.simple_tag()
def productFound(query):
    #Deze functie checkt simpelweg of er wel een user is die overeenkomt met de ID of Naam
    return ifProductExists(query)


