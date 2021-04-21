import os, time, os.path

class utils:
    def __init__(self):
        pass
    
    def get_file_list(self,folder):
        for item in os.listdir(folder):
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

if __name__ : "__main__"
    utils = utils()