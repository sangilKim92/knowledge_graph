from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
from collections import deque 
import re
from logger import Logger
import urllib.parse
import inspect
import json
from collections import namedtuple

config = {
    "save_file":"./",
    "link_level":3,
    "max_num":100000,
    "allowed_url":[],
    "not_allowed_url":[],
    "url":"https://www.naver.com",
    "query":[]
}

log = Logger('Method Class')
class Method:
    def __init__(self):
        log.make()
        self.visited = {}
        self.links = deque()
        Config = namedtuple('Config',('save_file','link_level','max_num','allowed_url','not_allowed_url','url','query'))
        self.answer = []
        try:
            with open("./config.json", "r") as st_json:
                config = json.loads(st_json.read()) if st_json else config
        except Exception as e:
            log.error("init() line="+str(inspect.currentframe().f_lineno)+' '+str(e))
        else:
            self.config = Config(*config.values())

    #@classmethod
    def find_url(self, url):
        log.info('find_url() start!')

        #arguments url null check
        if not url:
            log.info("find_url() Line="+str(inspect.currentframe().f_lineno)+" args: url does not exist")
            return

        #arguments url type check
        if type(url) is not str:
            log.info("find_url() Line="+str(inspect.currentframe().f_lineno)+" args: url tpye is not string")
            return

        try:
            soup = BeautifulSoup(urlopen(url),'lxml')
        except Exception as e:
            log.error("find_url() line="+str(inspect.currentframe().f_lineno)+' '+str(e))
            return None

        for link in soup.findAll('a'):
            temp_url = str(link.get('href'))

            if 'http' in temp_url:
                #절대주소
                pass
            elif re.match('/.+|\.\..+' , temp_url): #match 함수는 시작부터 일치하는지 검사한다. search는 문자열 내에 존재하면 찾아준다.
                #상대주소를 절대주소로 url 변경
                temp_url = urllib.parse.urljoin(url,temp_url)
            else:
                #그 외는 None 처리
                temp_url=None

            if temp_url and temp_url not in self.visited:
                self.visited.setdefault(temp_url,True)
                self.links.append(temp_url)

        return soup #deque로 넘겨주어 popleft()로 앞에서부터 뺀다.

    def scraping(self):
        """Let's start the scraping
            속도향상을 위해 multi processes 와 multi threading 적용
        """
        log.info("scraping() start!")

        Answer = namedtuple('answer',('url','text'))
        self.links.append(self.config.url)
        #몇 단계까지 크롤링할건지
        for i in range(self.config.link_level):
            if not self.links:
                log.info('Scraping() does not have url! line='+str(inspect.currentframe().f_lineno))

            #pop 쓰지않아야 할듯
            #순서와 리스트 다시 고려해서
            #yield 사용할지 link부터할지 정해야함
            url  = self.links.popleft()
            print(url)
            #데이터를 먼저 가져온 다음 link 넣기
            
            soup = find_url(url)

            
            #파싱 method

        return
    
    def query_check(self, soup):
        if not soup:
            log.info('query_check() does not have soup! line = '+str(inspect.currentframe.f_lineno))
            return False

        if not self.config.query:#질의어가 없으니 무조건 True
            return True

        for i in self.config.query:
            if i in str(soup):
                return True
        return False

    #STATIC class 로 만들어서 모든 파일에서 사용해야 한다.
    def get_line(self):
        """get the line number of code
        """
        return str(inspect.currentframe().f_lineno)+' '
    
    
if __name__== "__main__":
    method = Method()