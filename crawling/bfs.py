from collections import deque
from logger import Logger

log = Logger('BFS Class')
class bfs:

    def __init__(self):
        log.make()
        self.visited={}
        self.filters=[]
        self.urls=deque()
        

    def find_a_tag(self,url=None):
        visited = self.visited
        urls = self.urls

        if url not in visited:
            visited[url] = True
            urls.append()