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
            return element
    return wrapper


def create_article_list(url, headline, author='', raw=''):
    clean = ''
    final = []
    for sentence in raw:
        clean = clean + sentence
    process = [url, headline, author, clean]
    for i in process:
        if i is '':
            continue
        else:
            final.append(i)
    return final


@check_for_none
def get_element(url, tag, parser='lxml'):
    try:
        html = urlopen(url)
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
def get_class_list(url, tag, attr='class', desc='', parser='lxml'):
    try:
        html = urlopen(url)
    except (HTTPError, URLError) as e:
        print(e)
        return None
    try:
        bs = soup(html, parser)
        result = bs.findAll(tag, {attr: desc})
        cleanresult = []
        for i in result:
            cleanresult.append(i.get_text())
        return cleanresult
    except AttributeError as e:
        print(e)
        return None


def get_reuters_article(url):
    headline = get_class_list(url, 'h1', attr='class', desc='ArticleHeader_headline')
    author = get_class_list(url, 'p', attr='class', desc='Attribution_content')
    raw = get_class_list(url, 'p')
    raw = raw[0:-2]
    result = create_article_list(url, headline, author, raw)
    return result


def get_nyt_article(url):
    headline = get_element(url, 'h1')
    author = get_class_list(url, 'span', attr='itemprop', desc='name')
    author = author[0]
    raw = get_class_list(url, 'p', desc='css-1ebnwsw')
    headline = headline.get_text()
    result = create_article_list(url, headline, author, raw)
    return result


def get_article(url):
    for source in sources:
        if source in url:
            return sources[source](url)
        else:
            return 'This applciation is not configured for that website.'


sources = {
    'reuters.com': get_reuters_article,
    'nytimes.com': get_nyt_article
}


url = 'https://www.reuters.com/article/us-california-wildfires/rain-complicates-grim-task-of-finding-remains-of-california-wildfire-idUSKCN1NS0S8?feedType=RSS&feedName=environmentNews&utm_source=feedburner&utm_medium=feed&utm_campaign=Feed%3A+reuters%2Fenvironment+%28News+%2F+US+%2F+Environment%29'

result = get_article(url)

print(result)