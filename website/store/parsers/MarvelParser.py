import urllib.request, json

from store.models import Products, ProductDetails #IGNORE THIS ERROR, IT WILL WORK WHEN RUNNING python manage.py shell

""""
Er staan errors in volgens PyCharm. Dit is niet correct.

Runnen kan via de console only: python mange.py shell
cd naar de juiste directory
run MarvelParser.py
"""



heroesarr = ['iron_man', 'avengers', 'daredevil', 'hulk', 'spider-man']
#heroesarr = ['iron_man']

titlearr = []
descarr = []
pagecountarr = []
imgurlarr = []
cnt = 0
cnt1 = 0

for i in heroesarr:
    print(i)
    cnt = 0
    with urllib.request.urlopen("https://gateway.marvel.com/v1/public/comics?titleStartsWith=" + heroesarr[cnt1] +"&issueNumber=1&ts=1&format=comic&formatType=comic&noVariants=true&orderBy=-title&limit=100&apikey=144ba3e33cfbf7edd53ed87d7b64c23a&hash=2c814cdb9f5c3d39bbf973ec7fcc6c6b") as url:
        data = json.loads(url.read().decode())
        for cnt in range(0, 9):
            print(cnt)
            dataIndexed = data['data']['results'][cnt]
            title = dataIndexed['title']
            desc = dataIndexed['description']
            pgcount = dataIndexed['pageCount']
            fullurl = dataIndexed['thumbnail']['path'] + ".jpg"
            price = dataIndexed['prices'][0]['price']
            if not 'language' not in dataIndexed:
                lang = dataIndexed['textObjects'][0]['language']
            else:
                lang = "en-us"
            publ = dataIndexed['dates'][0]['date']

            prodN = str(title)
            prodP = float(price)
            prodID = Products.objects.all().order_by("-prodNum")
            prodNm = prodID[0].prodNum + 1
            prodPag = int(pgcount)
            prodLang = str(lang)
            prodDesc = str(desc)
            prodImg = str(fullurl)
            prodDate = publ
            prodDID = ProductDetails.objects.all().order_by("-id")
            prodDNm = prodDID[0].id + 1
            prodAuth = "Stan Lee"

            if not Products.objects.filter(prodName=prodN).exists():
                p = Products(prodNum=prodNm, prodName=prodN, prodPrice=prodP, prodStock=420)
                pd = ProductDetails(id=prodDNm, genre="Actie", type="Comic", publisher="Marvel Comics",
                                    totalPages=prodPag, language=prodLang, rating=1, author=prodAuth, desc=prodDesc,
                                    imageLink=prodImg, prodNum=p, pubDatum=prodDate)
                p.save()
                pd.save()
            else:
                print("Already added")

    cnt1 += 1


