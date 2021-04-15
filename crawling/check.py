from logger import Logger
from collections import deque 
import requests
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import re
from method import Method
import inspect
import urllib.parse


log = Logger('Check Class')
class check:
    ha = 0
    def __init__(self,ha):
        self.ha = 5
        if re.match('^/.+','/catch'):
            print('hh')
        print(re.match('^/.+|\.\..+','..asd'))
        try:
            soup = BeautifulSoup(urlopen("asdf"),'lxml')
        except Exception as e:
            print(str(e))
            log.error("find_url() line="+str(inspect.currentframe().f_lineno)+' '+'asdf')
        me = Method()
        #print(me.find_url('https://www.naver.com'))
    
    def get_line(self):
        """get the line number of code
        """
        return str(inspect.currentframe().f_lineno)+' '

if __name__=='__main__':
    ch = check(23)