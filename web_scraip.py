# python3 /Users/lawrie_6strings/be_professional_pythonist/web_scraip.py
# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup

res = requests.get('https://www.google.com/')
soup = BeautifulSoup(res.text, 'html.parser')
print(soup.header)