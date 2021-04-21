import os, time, os.path
import re
from konlpy.tag import Mecab
from sklearn.feature_extraction.text import CountVectorizer
import glob
class utils:
    def __init__(self):
        folder = "/home/com/data/"
        self.array, self.dic = self.files_to_array(self.get_file_list(folder))
        print(len(self.array))

    def get_file_list(self,folder):
        for item in glob.glob(os.path.join(folder,"*")):
            yield item

    def read_file(self, files):
        for item in files:
            if os.path.isfile(item):
                with open(item, 'r') as f:
                    yield (f.read())

    def get_file(self, files ,query):
        for item in files:
            if query in item:
                print(item)

    def files_to_array(self, files):
        """I only want korean so I don't need english and other language
            This method make dictionary using files and korean

            Args:
                files: collections of html files
        """
        m = Mecab()
        corpus = []
        for item in files:
            if os.path.isfile(item):
                encoding = ['utf-8', 'cp949']

                for encode in encoding:
                    try:
                        with open(item, 'r', encoding=encode) as f:
                            docs=""
                            sentences = f.read()
                            sentences = re.sub('[^가-힣ㄱ-ㅎ .!,]',' ',sentences)
                            sentences = re.sub(r'(.)\1+',r'\1\1',sentences)
                            for word in m.pos(sentences):
                                if word[1] in ['NNP','NNG','NNB','VA']:
                                    docs = docs +" "+ word[0]
                            corpus.append(docs)
                            break
                    except Exception as e:
                        #log.error('files_to_array() Line = ')
                        print("Error: {}".format(e))
        vector = CountVectorizer()
        return vector.fit_transform(corpus).toarray(), vector.vocabulary_
if __name__=="__main__":
    utils = utils()
