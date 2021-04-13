from logger import Logger
from collections import deque 
import requests
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import re

class check:
    ha = 0
    def __init__(self,ha):
        self.ha = 5
    
    def print_ha(self):
        print(self.ha)
        print(ha)

check(5)