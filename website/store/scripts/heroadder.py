import urllib.request, json

""""
Voegt voor elke superheld 10 records toe aan arrays (titel, description, aantal paginas, en de imagelink) gesorteerd
op alfabetische volgorde.

Meer heros moeten nog toegevoegd worden, en het moet nog gelinked worden met de database.
"""



heroesarr = ['iron', 'avengers', 'daredevil', 'hulk', 'spider-man']

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
        for cnt in range(0,10):
            print(cnt)
            title = data['data']['results'][cnt]['title']
            desc = data['data']['results'][0]['description']
            pgcount = data['data']['results'][0]['pageCount']
            fullurl = data['data']['results'][0]['thumbnail']['path'] + ".jpg"
            print(title)
            cnt += 1
            titlearr.append(title)
            descarr.append(descarr)
            pagecountarr.append(pagecountarr)
            imgurlarr.append(imgurlarr)
    cnt1 += 1
print(titlearr)



