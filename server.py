from flask import Flask
import word_probability
app = Flask(__name__)

@app.route('/')
def hello_world():
    word_list = word_probability.word_list
    word = word_probability.get_random_word(word_list)
    return word
