from history import History
import scrape
from summarize import summarize

if __name__ == '__main__':
    history = History()
    target = scrape.get_article(scrape.url)
    print('\n\n\n')
    print(summarize(target[3], 1.25))


# This application is a work in progress and not meant to be run aside from testing purposes.
