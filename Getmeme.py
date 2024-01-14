from bs4 import BeautifulSoup
import requests
from random import randint
src = []
index = randint(1, 93)


def memesPage():
    global index
    if not src:
        index += 1
        Meme_New_List(index)
    if index > 93:
        index = 1


def Meme_New_List(page):
    meme_html = requests.get(
        'https://memes.tw/wtf?sort=top-year&contest=11&page=%s' % (page))
    soup = BeautifulSoup(meme_html.text, 'html.parser')
    img_links = soup.find_all('img', 'img-fluid lazy')
    for imgs in img_links:
        src.append(imgs.get('data-src'))
    memesPage()


def MemeSend():
    #
    memesPage()
    return src.pop()
