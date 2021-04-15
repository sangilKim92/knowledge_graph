from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
from collections import deque 
import re
from logger import Logger
import urllib.parse
import inspect

log = Logger('Method Class')
class Method:
    def __init__(self):
        self.visited = {}
        self.links = deque()

    #@classmethod
    def find_url(self, url):
        log.info('find_url() start!')

        if not url:
            log.info("find_url() Line="+str(inspect.currentframe().f_lineno)+' '" does not have url")
            return

        if type(url) is not str:
            log.info("find_url() Line="+str(inspect.currentframe().f_lineno)+' '" has not str:url")
            return

        try:
            soup = BeautifulSoup(urlopen(url),'lxml')
        except Exception as e:
            log.error("find_url() line="+str(inspect.currentframe().f_lineno)+' '+str(e))
            return self.links

        for link in soup.findAll('a'):
            temp_url = str(link.get('href'))

            if 'http' in temp_url:
                #절대주소
                pass
            elif re.match('^/.+|^\.\..+', temp_url):
                #상대주소를 절대주소로 url 변경
                temp_url = urllib.parse.urljoin(url,temp_url)
            else:
                #그 외는 None 처리
                temp_url=None

            if temp_url and temp_url not in self.visited:
                self.visited.setdefault(temp_url,True)
                self.links.append(temp_url)

        return self.links #deque로 넘겨주어 popleft()로 앞에서부터 뺀다.

    def scraping(self):
        """Let's start the scraping
            속도향상을 위해 multi processes 와 multi threading 적용
        """
        log.info("scraping() start!")
        return

    #STATIC class 로 만들어서 모든 파일에서 사용해야 한다.
    def get_line(self):
        """get the line number of code
        """
        return str(inspect.currentframe().f_lineno)+' '
    
    

if __name__=='__main__':
    method = Method()
    