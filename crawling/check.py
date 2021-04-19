from logger import Logger
from collections import deque 
import requests
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import re
from method import Method
import inspect
import urllib.parse
from bfs import bfs
from collections import namedtuple
import math


log = Logger('Check Class')
class check:
    ha = 0
    def __init__(self,ha):
        log.make()
        print(self.ha)
        print(re.match('/.+|\.\..+','/../asdf'))
        try:
            soup = BeautifulSoup(urlopen("asdf"),'lxml')
        except Exception as e:
            print(str(e))
            log.error("find_url() line="+str(inspect.currentframe().f_lineno)+' '+'asdf')
        me = Method()
        #me.find_url('https://www.naver.com')
        test = 'https://www,naver.com/김천'.encode('utf-8')
        url = 'https://stackoverflow.com/questions/36108621/get-all-html-tags-with-beautiful-soup'
        self.find_content(url)
        
    def get_line(self):
        """get the line number of code
        """
        return str(inspect.currentframe().f_lineno)+' '

    def find_content(self,url):
        """
            HTML안의 핵심 tag 뽑는 알고리즘

            Args:
                url: tag 뽑을 url주소
        """
        Tag = namedtuple('tag',('idx','result','content'))

        soup = BeautifulSoup(urlopen(url),'lxml')
        all_tag = [tag for tag in soup.find_all()]
        body = soup.find_all('body')
        #body의 a link 개수를 넘긴다.
        LCb = self.number_of_a_characters(body[0])
        #body의 text 길이를 넘긴다.
        Cb = self.number_of_characters(body[0])
        e = math.log(1)
        """
            식 = CTDi = Ci/Ti * log( (Ci / nLCi * LCi) + (LCb/Cb*Ci) + (e) ) ( Ci* Ti / LCi / LTi)
        
        """
        max_result = 0
        #각 태그마다 Composite Text Density를 구한다.
        pos = 0
        for idx,tag in enumerate(all_tag):
            #text 길이를 넘긴다.
            Ci = self.number_of_characters(tag)
            #태그의 개수를 넘긴다.
            Ti = self.number_of_tag(tag)
            #a link 개수를 넘긴다
            LTi = self.number_of_a_tags(tag)
            #a link text 길이를 넘긴다.
            LCi = self.number_of_a_characters(tag)
            #a link가 아닌 태그의 text길이를 넘긴다.
            nLCi = self.number_of_na_chracters(tag)

            result =  Ci/ Ti * math.log( ( Ci / nLCi * LCi ) + ( LCb / Cb * Ci ) + (e) ) * ( Ci * Ti / LCi / LTi )
            if result > max_result:
                max_result = result
                pos = idx
        print(all_tag[pos].text)
        #Charnumber= 
    
    def number_of_tag(self,tag):
        if not tag:
            return 1
        return 1+len(tag.find_all())

    def number_of_a_tags(self,tag):
        if not tag:
            return 1
        return 1 + len(tag.find_all('a'))

    def number_of_na_chracters(self,tag):
        if not tag:
            return 1
        answer = 1
        for row in tag.find_all():
            if row.name != 'a':
                answer += len(row.text)
        return answer

    def number_of_a_characters(self,tag):
        if not tag:
            return 1
        answer = 1
        for a in tag.find_all('a'):
            answer += len(a.text)
        return answer

    def number_of_characters(self,tag):
        if not tag:
            return 1#없으면
        return 1 + len(tag.text)


if __name__=='__main__':
    ch = check(23)