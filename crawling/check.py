from logger import Logger
from collections import deque 
import requests
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import re
from scraping import Scraping
import inspect
import urllib.parse
import urllib.request
from collections import namedtuple
import math, os
from datetime import datetime
import glob


log = Logger('Check Class')
class check:
    ha = 0
    def __init__(self,ha):
        log.make()
        me = Scraping()
        #me.find_url('https://www.naver.com')
        me.scraping()
        #self.get_file(self.read_file(self.get_file_list('./')),'download')
        """        lst = glob.glob(os.path.join('./','data')+'/*')
        with open(lst[0],'r') as f:
            c = f.read()
        log.cut()
        start = datetime.now()
        result = 0
        
        for a in range(10000000):#천만번
            for b in ['네이버','청춘','카페']:
                if b:result += a
        print(datetime.now()-start)
        print(result)"""

    def get_file_list(self,folder):
        for item in os.listdir(folder):
            yield item       

    def files_to_dict(self, files):
        """I only want korean so I don't need english and other language
            This method make dictionary using files and korean

            Args:
                files: collections of html files
        """
        m = Mecab()
        corpus = []
        for item in files:
            if os.path.isfile(item):
                docs = []
                with open(item, 'r') as f:
                    sentences = f.read()
                    sentences = re.sub('[^가-힣ㄱ-ㅎ .!,]',' ',sentences)
                    sentences = re.sub(r'(.)\1+',r'\1\1',sentences)
                    for word in sentences.pos(sentences):
                        if word[1] in ['NNP','NNG','NNB','VA']:
                            docs.extend(word[0])
                    corpus.append(docs)
        vector = CountVectorizer()
        return vector.fit_transform(corpus).toarray()

if __name__=='__main__':
    ch = check(23)