from logger import Logger
from collections import deque 
import requests
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import re
from method import Method
import inspect
import urllib.parse
import urllib.request
from collections import namedtuple
import math
from datetime import datetime


log = Logger('Check Class')
class check:
    ha = 0
    def __init__(self,ha):
        log.make()
        me = Method()
        #me.find_url('https://www.naver.com')
        me.scraping()
        #print(urllib.parse.quote('https://www.naver.com/홍대', safe=':/?='))
        
    def hashCode(self, url):
        #url를 hashCode로 바꾼다.
        #python 내장 hash는 같은 값이 들어가도 다른 값을 return하기에 새로 정의한다.
        answer = 2300
        mul = 17
        for idx in url:
            answer = answer * mul +  ord(idx)
        return str(answer)

if __name__=='__main__':
    ch = check(23)