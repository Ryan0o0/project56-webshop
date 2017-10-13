from Django.core.paginator import Paginator
from ...database.getData import getResult

objects = ['A', 'B']
maxResults = 15
page = Paginator(objects, maxResults)
print(page.count)
print(page.num_pages)


def returnPage(query):
  page.object_list = getResult(query)
  page.per_page = 1000
  return page.page(1)
