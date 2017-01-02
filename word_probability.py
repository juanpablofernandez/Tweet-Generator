import re
import random

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
    return histogram

def word_probability(histogram):
    count = 0
    for word in histogram:
        value = histogram[word]
        count = count + value
        histogram[word] = count
    new_histogram = {}
    return histogram

def get_random_word(histogram):
    first_value = histogram[histogram.keys()[0]]
    last_value = histogram[histogram.keys()[-1]]
    random_number = random.randint(first_value, last_value)
    past_value = 0
    for key, value in histogram.items():
        if random_number > past_value and random_number <= value:
            return key
        past_value = value

word_list = histogram("frase.txt")
word_list = word_probability(word_list)
print get_random_word(word_list)

def test_random(histogram):
    counter = {}
    for i in range(0, 10000):
        word = get_random_word(histogram)
        if word not in counter:
            counter[word] = 0
        else:
            counter[word] = counter[word] + 1
    print counter
