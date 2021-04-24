import os, time, os.path 
from os import makedirs
import re
from konlpy.tag import Mecab
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from collections import namedtuple
import glob, pickle, json
import pandas as pd
import numpy as np
import inspect
from logger import Logger
import csv

config = {
    "files_folder":"./data/",
    "visited_file":"./visited_file.csv'",
    "word_idx_file":"./word_idf.json",
    "word_files":"./words/"
}

log = Logger('Utils class')
class utils:
    def __init__(self):
        global config
        Config = namedtuple('Config',('files_folder','visited_file','word_idf_file','word_files'))
        try:
            with open("./util.json", "r") as st_json:
                config = json.loads(st_json.read())
        except Exception as e:
            log.error("init() line="+str(inspect.currentframe().f_lineno)+' '+str(e))
        finally:
            self.config = Config(*config.values())
        self.save_map(self.config.word_files,self.config.word_idf_file)
        #file_list = self.files_to_map(folder,visited)
        #(self.get_visited_file(visited))
        
        #array과 dic, corpus를 저장시키고
        #비교할 query문과 array를 dic을 활용하여 비교한 다음 관련 corpus를 가져온다.
        #self.save_array_file()

    def save_file(self, name,file1):
        with open(name,'wb') as wb:
            for idx, item in enumerate(file1):
                wb.write(item)
            wb.close()

    def get_file_list(self,folder):
        for item in glob.glob(os.path.join(folder,"*")):
            yield item

    def get_word_idx(self, file):
        default = {}
        try:
            with open(file, 'r', encoding='utf-8') as f:
                return json.loads(f.read(), encoding='euc-kr')
        except Exception as e:
            log.error("Get_word_idx() Line="+str(inspect.currentframe().f_lineno)+" Error: "+str(e))
            return default

    def get_map(self, file):
        if not file:
            log.info("get_map() Line="+str(inspect.currentframe().f_lineno)+" file is not exist!")
            return

        default = {}
        try:
            with open(file, 'r', encoding='utf-8') as f:
                data = json.loads(f.read(), encoding='euc-kr')
        except Exception as e:
            log.error("get_map() Line="+str(inspect.currentframe().f_lineno)+" Error: "+str(e))
            data = default
        finally:
            return list(data)
        
    def save_map(self,word_files, word_idf_file):
        if not word_files:
            folder='./'

        if not os.path.exists(word_files):
            log.info("save_map() line = "+str(inspect.currentframe().f_lineno)+" makedirs")
            makedirs(word_files)
        
        words = self.get_map(word_idf_file)
        for word in words:
             if not os.path.exists(word_files + word+'.csv'):
                 with open(word_files + word + '.csv','w', encoding= 'utf-8') as f:
                     f.write(word)
                     f.close()

    def make_linked_list(self, files_folder, htmls, save_pos):
        #visited file에 없다면 폴더 words안의 csv파일에 추가시킨다.
        #files_folder
        #word_files
        #visited_file
        visited = self.get_visited_file(self.config.visited_file)
        items = self.get_file_list(self.config.files_folder)
        words = self.get_file_list(self.config.word_files)
        #item은 html파일 리스트
        for item in items:
            if not os.path.isfile(item):
                continue

            if item in visited:
                continue
            try:
                with open(item,'r',encoding='utf-8') as f:
                    html = f.read()
                    html = re.sub('[^가-힣ㄱ-ㅎ ]',' ',html)
                    html = re.sub(r'(.)\1+',r'\1\1',html)
                    for word in m.pos(html):
                        if word[1] not in ['NNP','NNG','NNB','VA']:
                            continue
                        if (word[0]+'.csv') not in words:
                            #그 단어가 word_files 리스트안에 없다는 뜻이니 새롭게 만든다.
                            with open(word[0]+.'.csv','w',encoding='utf-8') as f1:
                                f.write(item)
                                f.close()
                        else:    
                            with open(word[0]+'.csv'),'a',encoding='utf-8') as f2:
                                f.write(item)
                                f.close()
            except Exception as e:
                log.error("make_linked_list() Line ="+str(inspect.currentframe().f_lineno)+" Error: "+str(e))
        return 

    def get_visited_file(self, file):
        try:
            with open(file,'r') as f:
                lst = f.read()
                lst = lst.split(',')
                lst = [li.strip() for li in lst]
                return lst
        except Exception as e:
            log.error('Get_visited_file() Line = '+ str(inspect.currentframe().f_lineno)+ " Error: "+str(e))
            return []
        
    def files_to_map(self, folder, visited_file):
        """
        Get http list and make dictionary files
        dictionary take key and values, key is refering word and values is indicating numbers of word in files
        
        Args:
            foler is the directory which have a files
        """
        m = Mecab()
        answer = {}
        #이미 넣은 파일들은 건너뛰게 하는 함수
        visited = self.get_visited_file(visited_file)
        check = False
        #print(visited)
        for item in self.get_file_list(folder):
            #print(item)
            if not os.path.isfile(item):
                continue
            if item in visited:
                continue

            encoding = ['utf-8', 'cp949']
            for encode in encoding:
                try:
                    with open(item,'r', encoding = encode) as f:
                        html = f.read()
                        html = re.sub('[^가-힣ㄱ-ㅎ ]',' ',html)
                        html = re.sub(r'(.)\1+',r'\1\1',html)
                        for word in m.pos(html):
                            if word[1] not in ['NNP','NNG','NNB','VA']:
                                continue
                            answer.setdefault(word[0],1)
                            answer[word[0]] = answer[word[0]] + 1
                        visited.append(item)
                        check = True
                except Exception as e:
                    log.error('Files_to_map() Line = '+str(inspect.currentframe().f_lineno)+" Error: "+str(e))
        if answer:
            try:
                json.dump(answer,open('word_idf.json','w'))
            except Exception as e:
                log.error("Files_to_map() Line = " +str(inspect.currentframe().f_lineno)+" Error: "+str(e))

        if check:
            try:
                with open(visited_file,'w',encoding='utf-8') as f:
                    writer = csv.writer(f)
                    writer.writerow(visited)
            except Exception as e:
                log.error("Files_to_map Line = " +str(inspect.currentframe().f_lineno)+" Error: "+str(e))

        return True

if __name__=="__main__":
    utils = utils()