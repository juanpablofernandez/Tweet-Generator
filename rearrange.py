import random

words = "hello world this is jay and I am here to do the tweet generator"
wordArray = words.split()
used_numbers = []
rearranged_sentence = ""

while len(used_numbers) != len(wordArray):
    random_number = random.randint(0, len(wordArray)-1)
    if random_number not in used_numbers:
        used_numbers.append(random_number)
        rearranged_sentence += wordArray[random_number] + " "

print rearranged_sentence
