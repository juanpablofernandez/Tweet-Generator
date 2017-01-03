from flask import Flask
import word_probability
app = Flask(__name__)

@app.route('/')
def hello_world():
    histogram = word_probability.word_list
    sentence = word_probability.get_random_sentence(histogram, 17)
    return sentence
