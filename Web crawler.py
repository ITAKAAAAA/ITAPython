import requests
from bs4 import BeautifulSoup

def trade_spider(max_pages):
    for x in range(1, max_pages + 1):
