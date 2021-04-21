#!/usr/bin/python3
# https://www.ayima.com/us/insights/seo/analysing-url-parameters-with-python-for-seo.html

from urllib.parse import urlparse
from urllib.parse import parse_qs

file1 = open('paramURLs.txt', 'r')
Lines = file1.readlines()
 
urls = {}
parameters = {}
uniqueURLs = []
for url in Lines:
    u=urlparse(url)
    #print(u)
    parsedURL=urlparse(url)
    params=[]
    print(parsedURL)
    print('---------------')
    for param in parse_qs(parsedURL.query):
        #print(parsedURL.netloc)
        params.append(param)
	#parameters[param] = parameters.get(param, 0) + 1
        urls[parsedURL.netloc+parsedURL.path]=params
        #urls["domain"]["params"]="A"
for dom in urls:
    url2add="https://"+dom+'?'
    for p in urls[dom]:
        url2add+=p+'=&'
    uniqueURLs.append(url2add)
    print(dom)
    print(uniqueURLs)
#print(urls["domain"])
#print(uniqueURLs)
#https://about.att.com:80/allpostpage.html?category=Consumer&months=All&page=1
