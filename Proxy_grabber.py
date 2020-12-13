# THIS IS TEST LINE 
#this grabs the proxy online and stores it into a list
import time
from datetime import datetime
import requests
from bs4 import BeautifulSoup
import csv
from random import choice
import random

def get_proxy():  #this gets all proxies and corresponding port numbers and puts them into a list 'proxy:port'

    url = 'https://www.us-proxy.org'  #website that stores and updates US proxies
    #url = 'https://free-proxy-list.net/anonymous-proxy.html' #website that stores and updates anonymous proxies
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'lxml')
    table = soup.find('table')
    rows = table.find_all('tr')
    #print(rows)
    count = 0
    proxy_lst = []
    for row in rows:
        ip = row.contents[0].text
        port = row.contents[1].text
        anon = row.contents[4].text
        secconn = row.contents[6].text

        # if anon == 'elite proxy' or anon == 'anonymous':
        if anon == 'elite proxy':
        #if (secconn == 'yes' and (anon == 'elite proxy' or anon == 'anonymous')):
        #if (secconn == 'no' and (anon == 'elite proxy' or anon == 'anonymous')):
            print(ip, port, secconn, anon)
            line = 'http://' + ip + ':' + port
            proxies = { 'http': line, 'https': line }
            #print('Scraped proxy {}'.format(proxies))
            try:
                print('Checking if the proxy is good')
                testIP = requests.get('https://httpbin.org/ip', proxies=proxies, timeout=5)
                # print('This is the test ip result {}'.format(testIP.text))
                resIP = testIP.json()['origin']
                origin = resIP.split(',')

                if origin[0] == ip:
                    #print('Proxy ok! appending to list')
                    proxy_lst.append(line)
                    #print('good proxies recovered ---> {}'.format(len(proxy_lst)))
                    count += 1
                    # print()
                    if count == 5:
                        break
            except:
                pass
                # print('Bad proxy {}'.format(line))
    print(proxy_lst)
    data = proxy_lst
    #with open('/Users/jackboland/PycharmProjects/proxylst_anon.csv', 'w', newline='') as csvfile:
    #proxy_lst_file = '/Users/johntaylor/Programming/PycharmProjects/proxylst.csv'
    proxy_lst_file = '/Users/johntaylor/Programming/PycharmProjects/proxylst_2.csv'
    with open(proxy_lst_file, 'w', newline='') as csvfile:
        f = csv.writer(csvfile)
        f.writerow(data)
get_proxy()

