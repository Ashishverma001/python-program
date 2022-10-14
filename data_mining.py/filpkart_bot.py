
import os 
import requests
import datetime 
import pandas as pd 
from bs4 import BeautifulSoup


def get_soup(url):
    r = requests.get(url)
    if r.status_code == 200:
        return BeautifulSoup(r.text)
    return None

def get_produts(soup):
    target = soup.find ('div', class_ ='_1AtVbE col-12-12')
    if target is not None:
        items = target.find_all('div',class_ ='_1YokD2 _3Mn1Gg')
        print(f'found{len(items)}items')
        return items

def extract_one(item):
    data = {}
    title = item.find('div',class_ ='_1AtVbE col-12-12')
    sell_price = item.find('div',class_ ='dyC4hf')
    orig_price = item.find('div',class_ = '_30jeq3 _16Jk6d')
    rating = item.find('div',class_ = '_3LWZlK')
    num_ratings = item.find('span', class_ ='_2_R_DZ')
    if title:
        data['title']= title.text.strip()
    if sell_price:
        printsell_price.text.strip()
    if orig_price:
        print(orig_price.text.strip())
    if rating:
        print(rating.text.strip())
    if num_ratings:
        print(num_ratings.text.strip())
    print()
