#!/usr/bin/python3

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
        urls[parsedURL.netloc+parsedURL.path]=params
for dom in urls:
    url2add="https://"+dom+'?'
    for p in urls[dom]:
        url2add+=p+'=&'
    uniqueURLs.append(url2add)
    print(dom)
print(uniqueURLs)
