import os, time, os.path
import re
from konlpy.tag import Mecab
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
import glob, pickle
import pandas as pd
import numpy as np
class utils:
    def __init__(self):
        folder = "/home/data/crawling/data/"
        file_list = self.get_file_list(folder)
        self.files_to_array(file_list)
        
        #array과 dic, corpus를 저장시키고
        #비교할 query문과 array를 dic을 활용하여 비교한 다음 관련 corpus를 가져온다.
        #self.save_array_file()


    def save_map_file(self,name,dic):
        with open(name,'wb') as fw:
            pickle.dump(dic,fw)
    

    def save_file(self, name,file1):
        with open(name,'wb') as wb:
            for idx, item in enumerate(file1):
                wb.write(item)
            wb.close()

    def get_file_list(self,folder):
        for item in glob.glob(os.path.join(folder,"*")):
            yield item


    def files_to_array(self, folder):
        """
        I only want korean so I don't need english and other language
        This method make dictionary using files and korean

        Args:
            files: collections of html files
        """
        m = Mecab()
        corpus = []
        ori_corpus = []
        for item in folder:
            if os.path.isfile(item):
                encoding = ['utf-8', 'cp949']
                for encode in encoding:
                    try:
                        with open(item, 'r', encoding=encode) as f:
                            docs=""
                            sentences = f.read()
                            sentences = re.sub('[^가-힣ㄱ-ㅎ ]',' ',sentences)
                            sentences = re.sub(r'(.)\1+',r'\1\1',sentences)
                            for word in m.pos(sentences):
                                if word[1] in ['NNP','NNG','NNB','VA']:
                                    docs = docs +" "+ word[0]
                            corpus.append(docs)
                            ori_corpus.append(sentences.encode('utf-8'))
                            f.close()
                            break
                    except Exception as e:
                        #log.error('files_to_array() Line = ')
                        print("Error: {}".format(e))
                        f.close()
        tfidf = TfidfVectorizer().fit(corpus)
        self.save_file('/home/data/crawling/index_array.txt',tfidf.transform(corpus).toarray())
        print(tfidf.transform(corpus).toarray().shape)
        #self.save_map_file('/home/data/crawling/mapping.pickle',tfidf.vocabulary_)
        #self.save_file('/home/data/crawling/index_corpus.csv',ori_corpus)
        return 

if __name__=="__main__":
    utils = utils()
