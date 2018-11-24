from urllib.request import urlopen
from urllib.error import HTTPError, URLError
from bs4 import BeautifulSoup as soup
import re


def check_for_none(get_element):
    def wrapper(*args, **kwargs):
        element = get_element(*args, **kwargs)
        if element is None:
            print('Element could not be found.')
        else:
            for i in element:
                print(i)
            return element
    return wrapper


@check_for_none
def get_element(url, tag, parser='lxml'):
    try:
        html = urlopen(url)
        print('URL is ' + url)
    except (HTTPError, URLError) as e:
        print(e)
        return None
    try:
        bs = soup(html, parser)
        result = getattr(bs, tag)
        return result
    except AttributeError as e:
        print(e)
        return None


@check_for_none
def get_class_list(url, tag, classdesc, parser='lxml'):
    try:
        html = urlopen(url)
        print('URL is ' + url)
    except (HTTPError, URLError) as e:
        print(e)
        return None
    try:
        bs = soup(html, parser)
        result = bs.findAll(tag, {'class': classdesc})
        cleanresult = []
        for i in result:
            cleanresult.append(i.get_text())
        return cleanresult
    except AttributeError as e:
        print(e)
        return None


def get_reuters_article(url):
    headline = get_class_list(url, 'h1', 'ArticleHeader_headline')
    articleraw = get_class_list(url, 'p', '')
    articleclean = ''
    finalarticle = []
    articleraw = articleraw[0:-2]
    for sentence in articleraw:
        articleclean = articleclean + sentence
    finalarticle.append(headline)
    finalarticle.append(articleclean)
    return finalarticle


url = 'http://feeds.reuters.com/~r/reuters/environment/~3/3mgGe2M-D1s/vietnam-coffee-oil-production-under-threat-from-tropical-storm-usagi-idUSKCN1NS0EX'
result = get_reuters_article(url)

print(result)