from bs4 import BeautifulSoup
import requests
import os
import shadow_useragent
import urllib.request
import shutil
from urllib.request import Request, urlopen

#https://www.vogue.com/fashion-shows/fall-2021-menswear
#https://www.vogue.com/fashion-shows/spring-2021-couture

#jupyter timeit  & lprun

def scrap():


   # page = requests.get(urlsuiv, headers=headers)

    page = requests.get(urlsuiv)
    soup = BeautifulSoup(page.text, 'html.parser')

    titre = soup.find_all('div', attrs={'class': 'print-info--look'})
    image = soup.find_all('img', attrs={'class': 'slide--image'})

    rows1 = []
    rows2 = []
    rows = []

    for data1 in titre:
        brand = data1.get_text().replace('\n','').replace('\r','').replace('                        ','').replace('                    ','').replace(' ','-')
        rows1.append([brand.upper()])

    for f1 in image:
        urlimg = f1.get('src')
        rows2.append([urlimg])

    for i in range(len(rows2)):
        nom = rows1[i]
        image = rows2[i]
        nom = ''.join(nom)
        image = ''.join(image)

        print(nom)
        for data4 in nom:
            urllib.request.urlretrieve(image, "./"+FNAME+"/"+nom.upper() + ".jpg")

if __name__ == '__main__':
     # ua = shadow_useragent.ShadowUserAgent()
     # ua.force_update()
     # my_user_agent = ua.percent(0.01)
     # headers = {
     #     'User-Agent': '{}'.format(my_user_agent),
     #     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
     #     'Accept-Language': 'en-US,en;q=0.5',
     #     'Connection': 'keep-alive',
     #     'Upgrade-Insecure-Requests': '1',
     #     'Pragma': 'no-cache',
     #     'Cache-Control': 'no-cache',
     # }
     FNAME = "CHANEL SPRING 2020 COUTURE"
     urlsuiv = 'https://www.vogue.com/fashion-shows/spring-2020-couture/chanel/slideshow/collection/print'

     os.makedirs("./"+FNAME+"/", exist_ok=True)
     scrap()