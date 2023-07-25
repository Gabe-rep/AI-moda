from product import*
import bs4 
import re
import requests
import time 
import urllib.request as ur


def get_zalando_response () :

    name_prod = prod()

    url = ur.urlopen(f"https://www.zalando.it/catalogo/?q={name_prod.strip().replace(' ', '+')}").read()
    string = bytes.decode(url, 'utf-8')


    # x = requests.get(url)
    # content = x.content
    soup = bs4.BeautifulSoup(string, 'html')


    name =  [name for name in re.findall(r"\>(.*?)\<", str(soup.find_all("h3", {"class":"KxHAYs lystZ1 FxZV-M _4F506m ZkIJC- r9BRio qXofat EKabf7 nBq1-s _2MyPg2"})))]
    azienda_name = [name for name in re.findall(r"\>(.*?)\<", str(soup.find_all("h3",{"class":"_6zR8Lt lystZ1 FxZV-M _4F506m ZkIJC- r9BRio qXofat EKabf7 nBq1-s _2MyPg2"})))]
    price = [name for name in re.findall(r"\>(.*?)\<", str(soup.find_all("p", {"class":"KxHAYs lystZ1 FxZV-M _4F506m"})))]
    product = [i for i in name if i not in (', ')]
    compagny = [e for e in azienda_name if e not in (', ')]
    price = [x for x in price if x not in (', ')]


    print (product)
    print (compagny)
    print (price)


get_zalando_response ()


