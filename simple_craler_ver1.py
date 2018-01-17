# !/usr/bin/env python  
# -*- coding:utf-8 -*-
#Filename:simple_craler_ver1.py

from __future__ import division
import lxml
from lxml.html import fromstring
import requests
import re
import mechanize
import operator
import sys
import os
from urlparse import urlsplit


def send_requests(url):
    headers = {
        #'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:55.0) Gecko/20100101 Firefox/55.0',
        
    }
    try:
        req = requests.get(url, headers=headers,timeout=5)
    except:
        return 'err ', url, None
    #print req.content
    return req.text
url = sys.argv[1]


def get_all_Links(self):
    try:
        page_source = send_requests(url)
        if not page_source:
            raise NoneTypeError
        doc = lxml.html.document_fromstring(page_source)
        tags = ['a', 'iframe', 'frame']
        doc.make_links_absolute(url)
    except Exception,e:
        print e
        pass
        #return resHost, None
    links = doc.iterlinks()
    trueLinks = []
    for link in links:
        if link[0].tag in tags:
            trueLinks.append(link[2])
    return trueLinks

def get_domainname(url):
    url_parsed = urlsplit(url)
    #print url_parsed
    domain_name = url_parsed.netloc
    return domain_name

def urls_removal(urls):
    u = {}
    urls_Removal=[]
    for link in urls :
        #print link
        if (link.find('?')>0):
            m_link = link.split('?')
            values = m_link[-1]
            values = values.split('&')
            url = m_link[0]
            P=[]
            for j in values:
                Parameter = j.split('=')[0]
                P.append(Parameter)
            if url not in u.keys():
                c = link.split(': ')[-1]
                #print c
                urls_Removal.append(c)
            u[url] = set(P)
    #print u
    return urls_Removal

def print_all_links():
    for link in get_all_Links(send_requests(url)):
        print link


def main():
    print_all_links()

if __name__ == '__main__':
	main()
