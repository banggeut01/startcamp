# music_recom.py
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/random')
def random():
    return render_template('random.html')

@app.route('/result')
def result():
    emo = request.args.get('emo')
    return render_template('result.html', emo = emo)
    
if __name__ == '__main__':
    app.run(debug=True)