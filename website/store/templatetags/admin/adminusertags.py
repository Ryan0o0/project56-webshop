from django import template
from django.db.models import QuerySet

from ...database.adminGetData import *

register = template.Library()

@register.simple_tag()
def userFound(query):
    #Deze functie checkt simpelweg of er wel een user is die overeenkomt met de ID of Naam
    return ifUserExists(query)

@register.simple_tag()
def displayResults(query):
    #Deze functie convert alle gevonden users naar items in een table

    users = getUsers(query)

    html = "<table><tr><th>ID</th><th>Naam</th><th>Achternaam</th><th>E-mail</th><th>Geregistreerd</th><th>Edit</th></tr>"

    for e in users:
        html += "<tr><td>" + str(e.customerID) + "</td><td>" + e.name + "</td><td>" + e.surname + "</td><td>" + e.email + "</td><td>" + str(e.isRegistered) + "</td>" \
            "<td><form action='/admin/edit/user/" + str(e.customerID) +"'><button type='submit' value='Bewerken'/></form></td></tr>"

    html += "</table>"
    return html