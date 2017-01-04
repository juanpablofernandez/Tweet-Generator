from flask import Flask
import word_probability

app = Flask(__name__)

@app.route('/')
def start_app():
    print "Running..."
    histogram = word_probability.word_list
    sentence = word_probability.get_random_sentence(histogram, 17)
    return sentence

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
