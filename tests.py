import word_probability

def test_random(histogram):
    counter = {}
    for i in range(0, 10000):
        word = word_probability.get_random_word(histogram)
        if word not in counter:
            counter[word] = 0
        else:
            counter[word] = counter[word] + 1
    print counter


test_random(word_probability.word_list)
