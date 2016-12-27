import random

file = open("/usr/share/dict/words")
file = file.read()
dictionary_words = file.split()

def get_random_words(word_count):
    sentence = ""
    for i in range(0,words):
        random_number = random.randint(0, len(dictionary_words)-1)
        sentence += dictionary_words[random_number] + " "
        test = True
    print sentence

words = input("Number of Words: ")
get_random_words(words)
