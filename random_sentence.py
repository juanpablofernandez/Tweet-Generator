import random

def words(text):
    txt = open(text)
    book = txt.read()
    counter = 0
    d = {}
    for word in book.split():
        word = word.lower()
        counter += 1
        if word in d:
            value = d[word]
            value += 1
            d[word] = value
        else:
            d[word] = 1
    return d

def arrange(key):
    count = 0
    for value in key:
        value_for_key = key[value]
        key[value] = count + value_for_key
        count = key[value]
    return key

def getrandom(myDictionary):
    first = myDictionary[myDictionary.keys()[0]]
    last = myDictionary[myDictionary.keys()[-1]]
    random_int = random.randint(first, last)
    past = 0
    for key, value in myDictionary.items():
        if random_int > past and random_int <= value:
            return key
        past = value

def makearray(key, number):
    sentence = ""
    for i in range(0, number):
        random_word = getrandom(key)
        sentence += random_word + " "
    return sentence

key = words("book.txt")
key = arrange(key)
print makearray(key, 17)
