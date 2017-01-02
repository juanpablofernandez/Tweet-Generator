import re

def histogram(text):
    txt = open(text)
    book = txt.read()
    histogram = {}
    for word in book.split():
        word = word.lower()
        words = re.findall(r"[\w']+", word)
        if len(words) != 0:
            word = words[0]
            if word not in histogram:
                 histogram[word] = 1
            else:
                histogram[word] = histogram[word] + 1
    print histogram
    return histogram

def unique_words(histogram):
    print len(histogram)
    return len(histogram)

def frequency(word, histogram):
    print histogram[word]
    return histogram[word]

histograms = histogram("holmes.txt")
unique_words(histograms)
frequency("could", histograms)
