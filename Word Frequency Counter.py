import requests
from bs4 import BeautifulSoup
import operator

def contaParole(file):
    word_list = []
    fr = open(file, 'r')
    text = fr.read()
    fr.close
    words = text.content.lower().split()
    for each_word in words:
        print(each_word)
        word_list.append(each_word)

contaParole('sample.txt')