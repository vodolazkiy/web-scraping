from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.stem.snowball import SnowballStemmer


def summarize(text, weight=1.25):
    stemmer = SnowballStemmer('english')
    stopwordset = set(stopwords.words('english'))
    words = word_tokenize(text)
    freqtable = dict()
    for word in words:
        word = word.lower()
        if word in stopwordset:
            continue
        word = stemmer.stem(word)
        if word in freqtable:
            freqtable[word] += 1
        else:
            freqtable[word] = 1
    sentences = sent_tokenize(text)
    sentencevalue = dict()
    for sentence in sentences:
        for word, freq in freqtable.items():
            if word in sentence.lower():
                if sentence in sentencevalue:
                    sentencevalue[sentence] += freq
                else:
                    sentencevalue[sentence] = freq
    sumvalues = 0
    for sentence in sentencevalue:
        sumvalues += sentencevalue[sentence]
    # Average value of a sentence from original text
    average = int(sumvalues / len(sentencevalue))
    summary = ''
    for sentence in sentences:
        if (sentence in sentencevalue) and (sentencevalue[sentence] > (weight * average)):
            summary += ' ' + sentence
    return summary
