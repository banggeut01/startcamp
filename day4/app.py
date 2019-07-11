# app.py

# 0. flask package 가져오기
from flask import Flask, render_template

# 1. app 설정
app = Flask(__name__)

# 2. 요청 경로(route) + 함수 만들기
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/hello/<string:name>')
def hello(name):
    return render_template('hello.html', name=name)

# main이면 계속 실행시킴
if __name__ == '__main__':
    app.run(debug=True)