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
import math, os
from datetime import datetime


log = Logger('Check Class')
class check:
    ha = 0
    def __init__(self,ha):
        log.make()
        me = Method()
        #me.find_url('https://www.naver.com')
        me.scraping()
        #self.get_file(self.read_file(self.get_file_list('./')),'download')
        


if __name__=='__main__':
    ch = check(23)