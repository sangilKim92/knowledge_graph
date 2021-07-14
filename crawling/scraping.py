from bs4 import BeautifulSoup
from urllib.request import Request, urlopen, urlretrieve
from collections import deque 
from logger import Logger
from urllib.parse import urljoin, urlparse
from os import makedirs
import os.path, time, re, json, requests, inspect, os, math
from collections import namedtuple
from datetime import datetime
import os
import urllib.request
from kafkaConnect import send_to_consumer

config = {
    "save_file":"./data/",
    "abs_save_file":"./abs_data/",
    "link_level":3,
    "max":1000,
    "thread":1,
    "allowed_url":[],
    "not_allowed_url":[],
    "url":"https://www.naver.com",
    "query":[]
}

headers = { 
    'User-Agent' : ('Mozilla/5.0 (Windows NT 10.0;Win64; x64)\
    AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98\
    Safari/537.36'),
    'Accept-Language': 'en-US,en;q=0.8',
} 


log = Logger('Scarping Class')
class Scraping:
    def __init__(self):
        log.make()
        global config
        global headers
        self.visited = {}
        self.links = deque()
        self.answer = []
        Config = namedtuple('Config',('save_file','abs_save_file','link_level','max','thread','allowed_url','not_allowed_url','url','query'))
        try:
            with open("./config.json", "r") as st_json:
                config = json.loads(st_json.read())
        except Exception as e:
            log.error("init() line="+str(inspect.currentframe().f_lineno)+' '+str(e))
        finally:
            self.config = Config(*config.values())
            self.headers = headers

    #@classmethod
    def find_url(self, url):
        """find link tag in html
        
            Args:
                url: url take address of website finding the link tag
        """
        #arguments url null check
        if not url:
            log.info("find_url() Line="+str(inspect.currentframe().f_lineno)+" args: url does not exist")
            return

        #arguments url type check
        if type(url) is not str:
            log.info("find_url() Line="+str(inspect.currentframe().f_lineno)+" args: url tpye is not string")
            return

        try:

            url = urllib.parse.quote(url, safe=':/&?=')
            req = Request(url, headers = self.headers)
            site = urlopen(req, timeout=2)
            soup = BeautifulSoup(site.read(),'lxml')
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

            #request q보내려는 url가 실행파일, 집파일, rmp, deb, gz인 경우 건너뛴다.
            
            if 'Content-Type' not in site.headers:
                continue
            
            if 'text/html' not in site.headers['Content-Type']:
                continue
                
            #if re.search('(exe)$|(zip)$|(rpm)$|(gz)$|(deb)$|(txt)$|(csv)$|(pdf)$|(ppt)$', temp_url):
            #    continue

            if 'https' in temp_url:
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
            
        return soup #deque로 넘겨주어 popleft()로 앞에서부터 뺀다.
    
    def hashCode(self, url):
        """We don't need to get same web page so we have to distingush the same page
            If I store website using url, most of url contain '/' which is prohibitted by operating system.
            So I have to change url to int result using hashCode method

            Args:
                url: url is the website url 
        """
        if not url:
            logger.info('hashCode() Line='+str(inspect.currentframe().f_lineno)+' url is not exist')

        answer = 17
        mul = 7
        for idx in url:
            answer = answer * mul +  ord(idx)
        return str(answer)

    def download_file(self,url):
        try:
            """
            #url 마지막 /뒤에 . 이 있다면 파일일 가능성이 있다. 
            path = urlparse(url).path.rsplit('/',1)[-1]
            if '.' in path:
                print(path)
                return
            """
            if not url:
                logger.info('download_file() Line='+str(inspect.currentframe().f_lineno)+' url is not exist')

            if not os.path.exists(self.config.save_file):
                log.info("download_file() line = "+str(inspect.currentframe().f_lineno)+" makedirs")
                makedirs(self.config.save_file)
            
            #주소 사이즈가 너무 크거나 로딩이 오래걸리면 out

            url = urllib.parse.quote(url, safe=':/&?=')
            
            save_file = self.config.save_file+self.hashCode(url)+'.txt'
            if os.path.exists(save_file):
                log.info('download_file() File= {} is already exists'.format(url))
                return False
            req = Request(url, headers = self.headers)
            site = urlopen(req,timeout = 2).read()
            #사이트가 너무 크면 넘어감
            if site.__sizeof__() > 400000:
                log.info('download_file() File = '+url+" is out of size")
                return False
            #원하는 단어가 없으면 넘어감
            if not self.query_check(site):
                log.info('download_file() File = '+url+" does not contain query terms")
                return False
            #url주소는 /를 포함하기에 url를 주소로 만들수 없다. 따로 hashCode를 만들어 주소를 숫자로 바꾼다.
            with open(save_file, mode="wb") as f:
                f.write(site)
                log.info("download_file() File = "+save_file+" 생성!")
            return True
            #다운받으면 다운받은 주소 넘겨주기
        except Exception as e:
            log.error("download_file() line = "+str(inspect.currentframe().f_lineno)+" Error: "+str(e))
            return False


    def scraping(self):
        """Let's start the scraping
            속도향상을 위해 multi processes 적용
        """
        log.info("scraping() start!")

        self.links.append(self.config.url)
        #몇 단계까지 크롤링할건지
        number = 0
        for i in range(self.config.link_level):
            if not self.links:
                log.info('Scraping() does not have url! line='+str(inspect.currentframe().f_lineno))
                return

            #pop 쓰지않아야 할듯
            #순서와 리스트 다시 고려해서
            #yield 사용할지 link부터할지 정해야함
            num = len(self.links)
            log.info("scraping() Line = "+str(inspect.currentframe().f_lineno)+ " ->  {}번째 Link_level scraping -> num 개수:{}".format(i+1,num))
            for a in range(num):
                number += 1
                if number > self.config.max:
                    log.info("scraping() Line = "+str(inspect.currentframe().f_lineno)+" -> max: {} 까지 완료".format(number))
                    return
                url  = self.links.popleft()
                print(number, '개 scarping완료 ', url)
                check = self.download_file(url)
                if check:
                    self.find_content(url)
                if i < self.config.link_level - 1:
                    soup = self.find_url(url)
                log.cut()
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
            if str(i).encode('utf-8') in soup:
                return True
        return False

    def find_content(self,url):
        """
            HTML안의 핵심 tag 뽑는 알고리즘

            Args:
                url: tag 뽑을 url주소
        """
        Tag = namedtuple('tag',('idx','result','content'))
        try:
            url = urllib.parse.quote(url, safe=':/&?=')

            if not os.path.exists(self.config.abs_save_file):
                log.info("find_content() line = "+str(inspect.currentframe().f_lineno)+" makedirs")
                makedirs(self.config.abs_save_file)

            save_file = self.config.abs_save_file+self.hashCode(url)+'.txt'
            if os.path.exists(save_file):
                log.info('find_content() File= {} is already exists'.format(url))
                return

            req = requests.get(url, headers= self.headers,timeout=2).text
            
            pattern1 = ("<script([^'\"]|\"[^\"]*\"|'[^']*')*?(</script>|/>)")
            pattern2 = ("<meta([^'\"]|\"[^\"]*\"|'[^']*')*?(</meta>|/>)")
            pattern3 = ("<link([^'\"]|\"[^\"]*\"|'[^']*')*?(</link>|/>)")
            pattern4 = ("<style([^'\"]|\"[^\"]*\"|'[^']*')*?(</style>|/>)")

            pattern = []
            pattern.append(pattern1)
            pattern.append(pattern2)
            pattern.append(pattern3)
            pattern.append(pattern4)

            for pat in pattern:
                req = re.sub(pat,"", req, flags = re.S)

            soup = BeautifulSoup(req,'lxml')
    
        except Exception as e:
            log.error('find_content() line= '+str(inspect.currentframe().f_lineno)+" Error: "+str(e))
            return 
        all_tag = [tag for tag in soup.find_all()]
        #print(len(all_tag))
        body = soup.find('body')
        #script, style, comment, link 태그는 의미가 없으므로 삭제한다.
        #body의 a link 개수를 넘긴다.
        LCb = self.number_of_a_characters(body)
        #body의 text 길이를 넘긴다.
        Cb = self.number_of_characters(body)
        e = math.log(1)
        """
            식 = CTDi = Ci/Ti * log( (Ci / nLCi * LCi) + (LCb/Cb*Ci) + (e) ) ( Ci* Ti / LCi / LTi)
            Ci = the number of all characters under i
            Ti = the number of all tags under i
            nLCi = the number of all non-hyperlink characters under i
            LCi = the number of all hyperlink characters under i
            LTi = the number of all hyperlink tags under i
            LCb = the number of all hyperlink characters under the <body> tag
            Cb = the number of all characters under the <body> tag

            i = i is a tag in a  web page
        """
        max_result = 0
        pos = 0
        #각 태그마다 Composite Text Density를 구한다.
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
        try:
            text_file = open(save_file, 'w')
            text_file.write(url+'\n')
            text_file.write(all_tag[pos].text)
            send_to_consumer(all_tag[pos].text)
            log.info('find_content() File = '+save_file+" 생성!")
        except Exception as e:
            log.error('find_content() Line = '+str(inspect.currentframe().f_lineno)+" Error: "+str(e))
        
        return 

    
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
    method = Scraping()