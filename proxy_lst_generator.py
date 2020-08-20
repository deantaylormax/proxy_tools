#free proxy list generator
import requests
from bs4 import BeautifulSoup
import random

def get_proxy():  #this downloads 20 proxies puts them in a file and randomly pulls one to use for web scraper.

    #list of URLS from which to grab the proxies
    url_lst = ['https://www.us-proxy.org', 'https://free-proxy-list.net/anonymous-proxy.html']

    #list of urls to use.  These urls work with the beautiful soup code below.  
    #If you find other urls, you will have to modify the beautiful soup code to traverse the html of those websites to extract the proxies and ports

    #url_lst = ['https://free-proxy-list.net/anonymous-proxy.html']
    #url = 'https://www.us-proxy.org'  #website that stores and updates US proxies
    #url = 'https://free-proxy-list.net/anonymous-proxy.html' #website that stores and updates anonymous proxies
    type = 'elite proxy'  #this selection masks your real IP and masks the fact that you are using a proxy
    #type = 'anon'   #this will mask your real IP but informs site that you are using a proxy

    proxy_lst = []
    for url in url_lst:
        r = requests.get(url)
        soup = BeautifulSoup(r.content, 'lxml')
        table = soup.find('table')
        rows = table.find_all('tr')
        for row in rows[1:21]:
            ip = row.contents[0].text
            port = row.contents[1].text
            anon = row.contents[4].text
            secconn = row.contents[6].text
            if anon == type:  #elite proxies do not allow sites to learn that you are using a proxy
                line = 'http://' + ip + ':' + port
                proxy_lst.append(line)
    print(f'{len(proxy_lst)} PROXIES')
    proxy = random.choice(proxy_lst) #picks a random valid proxy from the list
    print(f'proxy selected is - {proxy}') #identifies the proxy selected
    return proxy

proxy = get_proxy()

#you can then continue code below entering 'proxy' wherever you need that random proxy to be entered, e.g. in selenium webdriver options settings.
