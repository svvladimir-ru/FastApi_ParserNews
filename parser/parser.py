import requests
import logging
import collections
import csv
import re
import pprint
from bs4 import BeautifulSoup
from time import sleep


pp = pprint.PrettyPrinter(indent=4)


def get_html(url, params=None):
    r = requests.get(url, params=params)
    return r


class Lenta:
    """Парсер ленты"""
    def __init__(self):
        self.url = 'http://lenta.ru/rss'
        self.item = []
        self.full_item = []

    def news(self, limit=None):
        soup = BeautifulSoup(get_html(self.url).text, "html.parser")
        pars_items = soup.find_all('item', limit=limit)
        for i in pars_items:
            self.item.append(
                {
                    'author': i.find('author').get_text(),
                    'title': i.find('title').get_text(),
                    'link': i.find('guid').get_text(),
                    'description': i.find('description').get_text(),
                    'pubdate': i.find('pubdate').get_text(),
                    'image': i.find('enclosure').get('url'),
                    'category': i.find('category').get_text()
                }
            )

        return self.item

    def grub(self, url):
        soup = BeautifulSoup(get_html(url).text, "html.parser")
        a = {}
        a.update(
            {
                'title': soup.find('h1', class_='b-topic__title').get_text(),
                'image': soup.find('div', class_='b-topic__title-image').find('img').get('src'),
            }
        )
        for i in soup.find(class_='b-text').find_all('p'):
            a.update({
                'content': i.get_text(),
            })
        return a


class Interfax(Lenta):

    def __init__(self):
        super().__init__()
        self.url = 'http://www.interfax.ru/rss.asp'
        self.item = []

    def news(self, limit=None):
        soup = BeautifulSoup(get_html(self.url).text, "html.parser")
        pars_items = soup.find_all('item', limit=limit)
        for i in pars_items:
            self.item.append(
                {
                    'title': i.find('title').get_text(),
                    'link': i.find('guid').get_text(),
                    'description': i.find('description').get_text(),
                    'pubdate': i.find('pubdate').get_text(),
                    'category': i.find('category').get_text()
                }
            )
        return self.item

    def grub(self, url):
        soup = BeautifulSoup(get_html(url).content, "html.parser")  # .content для нормальной работы кодировки
        print(url)
        a = {}
        full_text = []
        a.update(
            {
                'title': soup.find('h1', itemprop='headline').get_text(),
                # 'image': soup.find('figure', class_='inner').find('img').get('src'),
            }
        )
        for i in soup.find('article', itemprop='articleBody').find_all('p'):
            full_text.append(i.get_text())
        a.update({
            'content': ''.join(full_text),
        })
        return a


class Kommersant(Interfax):

    def __init__(self):
        self.url = 'http://www.kommersant.ru/RSS/news.xml'
        self.item = []

    def news(self, limit=None):
        super().news(limit=limit)
        return self.item

    def grub(self, url):
        soup = BeautifulSoup(get_html(url).content, "html.parser")
        print(url)
        a = {}
        a.update(
            {
                'title': soup.find('h1', itemprop='headline').get_text(),
                'content': soup.find('div', class_='article_text_wrapper').get_text(),
            }
        )
        return a


class M24():
    def __init__(self):
        self.url = 'http://www.m24.ru/rss.xml'
        self.item = []

    def news(self, limit=None):
        soup = BeautifulSoup(get_html(self.url).text, "html.parser")
        pars_items = soup.find_all('item', limit=limit)
        # print(pars_items)
        for i in pars_items:
            self.item.append(
                {
                    'id': i.find('id').get_text(),
                    'title': i.find('title').get_text(),
                    'link': i.find('link').next_element.replace('\n', '').replace('\t', ''),
                    'description': i.find('description').get_text(),
                    'pubdate': i.find('pubdate').get_text(),
                    'image': i.find('enclosure').get('url'),
                    'category': i.find('category').get_text(),
                    'genre': i.find('yandex:genre').get_text(),
                }
            )
            if i.find('media:group'):
                self.item.append({
                    'media:group': {
                        'media:content': i.find('media:group').find('media:content').get('url'),
                        'media:player': i.find('media:group').find('media:player').get('url'),
                        'media:thumbnail': i.find('media:group').find('media:thumbnail').get('url')
                    }
                })
        return self.item

    def grub(self, url):
        soup = BeautifulSoup(get_html(url).content, "html.parser")  # .content для нормальной работы кодировки
        # items = soup.find('div', class_='infinitblock')
        print(url)
        a = {}
        full_text = []
        a.update(
            {
                'title': soup.find('div', class_='b-material-before-body').find('h1').get_text(),
                'image': url + soup.find('div', class_='b-material-incut-m-image').find('img').get('src'),  # полная ссылка
            }
        )
        for i in soup.find('div', class_='js-mediator-article').find_all('p', class_=None):
            full_text.append(i.get_text())
        a.update({
            'content': ''.join(full_text),
        })
        return a


class Graber():
    HEADERS = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 ('
                      'KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',
        'accept': '*/*'
    }

    def __init__(self):
        self.lenta = Lenta()
        self.interfax = Interfax()
        self.kommersant = Kommersant()
        self.m24 = M24()
