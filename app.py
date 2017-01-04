from flask import Flask
import word_probability

app = Flask(__name__)

@app.route('/')

def run():
    histogram = word_probability.word_list
    sentence = word_probability.get_random_sentence(histogram, 17)
    return sentence

if __name__ == "__main__":
    run()
