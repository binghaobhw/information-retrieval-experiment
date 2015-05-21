# -*- coding: utf-8 -*-
import re

from web_crawler import collection as col
import requests
from ltp import segment
from bs4 import BeautifulSoup, Comment


HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding': 'gzip,deflate,sdch',
    'Accept-Language': 'en,zh-CN;q=0.8,zh;q=0.6,zh-TW;q=0.4',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Referer': 'https://www.google.com.hk/',
    'User-agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.146 Safari/537.36'}
browser = requests.Session()


def split_to_word(text):
    return segment(text)


def get_page(url):
    try:
        response = browser.get(url, timeout=5, headers=HEADERS)
        if response.status_code == requests.codes.ok:
            return BeautifulSoup(response.text)
        else:
            return BeautifulSoup()
    except:
        return BeautifulSoup()


def union(a, b):
    """

    >>> a, b = ['a', 'b', 'c'], ['b', 'c', 'd']
    >>> union(a,b)
    >>> print a
    ['a', 'b', 'c', 'd']
    """
    for e in b:
        if e not in a:
            a.append(e)


def get_next_target(page):
    """

    >>> ('link1', 16) == get_next_target('aa<a href="link1">link</a>bbcc')
    True
    >>> (None, 0) == get_next_target('aabbcc')
    True
    """
    start_link = page.find('<a href=')
    if start_link == -1:
        return None, 0
    start_quote = page.find('"', start_link)
    end_quote = page.find('"', start_quote + 1)
    url = page[start_quote + 1:end_quote]
    return url, end_quote


def get_all_links(soup):
    links = []
    for a in soup.find_all('a'):
        if a.has_attr('href'):
            links.append(a.get('href'))
    return links


def add_to_index(keyword, url):
    entry = col.find_one({'keyword': keyword})
    if entry:
        if not url in entry['url']:
            entry['url'].append(url)
            col.save(entry)
        return
    # not found, add new keyword to index
    col.insert({'keyword': keyword, 'url': [url]})


def add_page_to_index(url, text_list):
    for text in text_list:
        for word in split_to_word(text):
            add_to_index(word, url)


def visible(element):
    if element.parent.name in ['style', 'script', '[document]', 'head', 'title']:
        return False
    elif isinstance(element, Comment):
        return False
    elif re.match('\n', unicode(element)):
        return False
    else:
        return True


def get_visible_text_list(soup):
    elements = soup.find_all(text=True)
    visible_elements = filter(visible, elements)
    return map(unicode, visible_elements)


def crawl_web(seed, max_depth):
    to_crawl = [seed]
    crawled = []
    next_depth = []
    depth = 0
    while to_crawl and depth <= max_depth:
        page = to_crawl.pop(0)
        if page not in crawled:
            soup = get_page(page)
            visible_text_list = get_visible_text_list(soup)
            add_page_to_index(page, visible_text_list)
            union(to_crawl, get_all_links(soup))
            crawled.append(page)
        if not to_crawl:
            to_crawl, next_depth = next_depth, []
            depth += 1
