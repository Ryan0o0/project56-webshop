from django import template
import urllib.request, json
from ..database.getData import getProdImage, getProdName, getProdPublish, getProdPrice, getProdAuthor, getProdStock

register = template.Library()

@register.assignment_tag

def any_function():
    with urllib.request.urlopen('https://gateway.marvel.com/v1/public/comics?ts=1&format=comic&formatType=comic&noVariants=true&orderBy=-title&limit=1&apikey=144ba3e33cfbf7edd53ed87d7b64c23a&hash=2c814cdb9f5c3d39bbf973ec7fcc6c6b') as url:
        data = json.loads(url.read().decode())
        title =  data['data']['results'][0]['title']
        desc = 'description: ' + data['data']['results'][0]['description']
        count = 'pagecount: ', data['data']['results'][0]['pageCount']
        fullurl = str(data['data']['results'][0]['thumbnail']['path']) + '.jpg'
    return "{0}, {1}, {2}, {3}".format(title, desc, count, fullurl)


@register.simple_tag()
def prodImageTag(prodNum):
    return getProdImage(prodNum)

@register.simple_tag()
def prodUrlTag(prodNum):
    url = "/product/" + str(prodNum)
    return url

@register.simple_tag()
def prodTitleTag(prodNum):
    return getProdName(prodNum)

@register.simple_tag()
def prodPublTag(prodNum):
    return getProdPublish(prodNum)

@register.simple_tag()
def prodPriceTag(prodNum):
    return getProdPrice(prodNum)

@register.simple_tag()
def prodAuthorTag(prodNum):
    return getProdAuthor(prodNum)

@register.simple_tag()
def prodStockTag(prodNum):
    return getProdStock(prodNum)