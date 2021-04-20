from bs4 import BeautifulSoup
from urllib.request import Request, urlopen, urlretrieve
from collections import deque 
from logger import Logger
from urllib.parse import urljoin, urlparse
from os import makedirs
import os.path, time, re, json, requests, inspect, os
from collections import namedtuple
import math
from datetime import datetime

config = {
    "save_file":"./data/",
    "abs_save_file":"./abs_data/",
    "link_level":3,
    "thread":1,
    "allowed_url":[],
    "not_allowed_url":[],
    "url":"https://www.naver.com",
    "query":[]
}


log = Logger('Method Class')
class Method:
    def __init__(self):
        log.make()
        global config
        self.visited = {}
        self.links = deque()
        self.answer = []
        Config = namedtuple('Config',('save_file','abs_save_file','link_level','thread','allowed_url','not_allowed_url','url','query'))
        try:
            with open("./config.json", "r") as st_json:
                config = json.loads(st_json.read())
        except Exception as e:
            log.error("init() line="+str(inspect.currentframe().f_lineno)+' '+str(e))
        finally:
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
            soup = BeautifulSoup(requests.get(url).text,'lxml')
        except Exception as e:
            log.error("find_url() line="+str(inspect.currentframe().f_lineno)+' Error: '+str(e))
            return None
        for link in soup.findAll('a'):
            temp_url = str(link.get('href'))

            allow = self.allowed_url_check(temp_url)
            if not allow:
                continue

            #만약 상대주소로 되어있다면 not_allowed_url_check에 넣은게 들어갈 수 도 있다.
            # 가령 /policy/privacy.html 같은 경우 절대주소로 바꾸면 www.naver.com/policy/privacy.html 로 된다.
            # 따라서 걸러지지 않는데 이는 처음 시작 주소를 잘선택하면 문제없다. 
            disallow = self.not_allowed_url_check(temp_url)
            if not disallow:
                continue

            if 'http' in temp_url:
                #절대주소
                pass
            elif re.match('/.+|\.\..+' , temp_url):
                #match 함수는 시작부터 일치하는지 검사한다. search는 문자열 내에 존재하면 찾아준다.
                #상대주소를 절대주소로 url 변경
                temp_url = urljoin(url,temp_url)
            else:
                #그 외는 None 처리
                temp_url=None

            if temp_url and temp_url not in self.visited:
                self.visited.setdefault(temp_url,True)
                self.links.append(temp_url)
        log.info('find_url() end!')
            
        return soup #deque로 넘겨주어 popleft()로 앞에서부터 뺀다.

    def download_file(self,url):
        log.info('download_file() start line'+str(inspect.currentframe().f_lineno))
        o = urlparse(url)
        savedir = os.path.dirname(self.config.save_file)

        if not os.path.exists(savedir):
            log.info("download_file() line = "+str(inspect.currentframe().f_lineno)+" makedirs")
            makedirs(savedir)
        try:
            urlretrieve(url, self.config.save_file+str(datetime.now()))
            log.info("download_file() line = "+str(inspect.currentframe().f_lineno)+" download file")
            return True
            #다운받으면 다운받은 주소 넘겨주기
        except Exception as e:
            log.error("download_file() line = "+str(inspect.currentframe().f_lineno)+" Error: "+str(e))
            return False


    def scraping(self):
        """Let's start the scraping
            속도향상을 위해 multi processes 와 multi threading 적용
        """
        log.info("scraping() start!")

        Answer = namedtuple('answer',('url','text'))
        self.links.append(self.config.url)
        #몇 단계까지 크롤링할건지
        for i in range(self.config.link_level):
            log.info("scraping() Line = "+str(inspect.currentframe().f_lineno)+ " ->  {}번째 Link_level scraping 중".format(i+1))
            if not self.links:
                log.info('Scraping() does not have url! line='+str(inspect.currentframe().f_lineno))

            #pop 쓰지않아야 할듯
            #순서와 리스트 다시 고려해서
            #yield 사용할지 link부터할지 정해야함
            num = len(self.links)
            for a in range(num):
                url  = self.links.popleft()
                check = self.download_file(url)
                
                if check:
                    if i < self.config.link_level - 1:
                        soup = self.find_url(url)
                    self.find_content(url)
            #데이터를 먼저 가져온 다음 link 넣기
            
        return
    
    def allowed_url_check(self,url):
        if not self.config.allowed_url:
            return True

        for i in self.config.allowed_url:
            if i in url:
                return True
        return False

    def not_allowed_url_check(self, url):
        if not self.config.not_allowed_url:
            return True
        
        for i in self.config.not_allowed_url:
            if i in url:
                return  False
        return True

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

    def find_content(self,url):
        """
            HTML안의 핵심 tag 뽑는 알고리즘

            Args:
                url: tag 뽑을 url주소
        """
        log.info('find_content() start!')
        Tag = namedtuple('tag',('idx','result','content'))
        soup = BeautifulSoup(requests.get(url).text,'lxml')
        all_tag = [tag for tag in soup.find_all()]
        body = soup.find('body')
        #body의 a link 개수를 넘긴다.
        LCb = self.number_of_a_characters(body)
        #body의 text 길이를 넘긴다.
        Cb = self.number_of_characters(body)
        e = math.log(1)
        """
            식 = CTDi = Ci/Ti * log( (Ci / nLCi * LCi) + (LCb/Cb*Ci) + (e) ) ( Ci* Ti / LCi / LTi)
        
        """
        max_result = 0
        pos = 0
        #각 태그마다 Composite Text Density를 구한다.
        for idx,tag in enumerate(all_tag):
            log.info('find_content() for문 도는중!')
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
        try:
            text_file = open(self.config.abs_save_file+str(datetime.now())+'.txt', 'w')
            text_file.write(url+'\n')
            text_file.write(all_tag[pos].text)
        except Exception as e:
            log.error('find_content() Line = '+str(inspect.currentframe().f_lineno)+" Error: "+str(e))
        
        log.info('find_content() end!')
        return all_tag[pos].text

    
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
    
if __name__== "__main__":
    method = Method()