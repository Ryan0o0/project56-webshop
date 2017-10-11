from Django.core.paginator import Paginator
objects = ['A', 'B']
maxResults = 1
page = Paginator(objects, maxResults)
print(page.count)
print(page.num_pages)

def getResult(objects, maxResults, pageNumber):
  page.object_list = objects
  page.per_page = maxResults
  return page.page(pageNumber)
