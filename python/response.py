from product import*
import bs4 
import re
import requests
import time 
import urllib.request as ur


def get_zalando_response(VISION_ENDPOINT,VISION_KEY,path_image):
    prod1, prod2, prod3, prod4 = prod(VISION_ENDPOINT,VISION_KEY,path_image)
    if len(prod1) != 0 :
        for i in prod1:
            name_prod = i

            url = ur.urlopen(f"https://www.zalando.it/catalogo/?q={name_prod.strip().replace(' ', '+')}").read()
            string = bytes.decode(url, 'utf-8')
            print (f"https://www.zalando.it/catalogo/?q={name_prod.strip().replace(' ', '+')}")

    if len(prod2) != 0 :
        for i in prod2:
            name_prod = i

            url = ur.urlopen(f"https://www.zalando.it/catalogo/?q={name_prod.strip().replace(' ', '+')}").read()
            string = bytes.decode(url, 'utf-8')
            print (f"https://www.zalando.it/catalogo/?q={name_prod.strip().replace(' ', '+')}")

    if len(prod3) != 0 :
        for i in prod3:
            name_prod = i

            url = ur.urlopen(f"https://www.zalando.it/catalogo/?q={name_prod.strip().replace(' ', '+')}").read()
            string = bytes.decode(url, 'utf-8')
            print (f"https://www.zalando.it/catalogo/?q={name_prod.strip().replace(' ', '+')}")

    if len(prod4) != 0 :
        for i in prod4:
            name_prod = i

            url = ur.urlopen(f"https://www.zalando.it/catalogo/?q={name_prod.strip().replace(' ', '+')}").read()
            string = bytes.decode(url, 'utf-8')
            print (f"https://www.zalando.it/catalogo/?q={name_prod.strip().replace(' ', '+')}")






# # x = requests.get(url)
# # content = x.content
# soup = bs4.BeautifulSoup(string, 'html')
# # print (soup)

# name =  [name for name in re.findall(r"\>(.*?)\<", str(soup.find_all("h3", {"class":"KxHAYs lystZ1 FxZV-M _4F506m ZkIJC- r9BRio qXofat EKabf7 nBq1-s _2MyPg2"})))]
# azienda_name = [name for name in re.findall(r"\>(.*?)\<", str(soup.find_all("h3",{"class":"_6zR8Lt lystZ1 FxZV-M _4F506m ZkIJC- r9BRio qXofat EKabf7 nBq1-s _2MyPg2"})))]
# price = [name for name in re.findall(r"\>(.*?)\<", str(soup.find_all("p", {"class":"KxHAYs lystZ1 FxZV-M _4F506m"})))]
# product = [i for i in name if i not in (', ')]
# compagny = [e for e in azienda_name if e not in (', ')]
# prize = [x for x in price if x not in (', ')]






