# app.py

# 0. flask package 가져오기
from flask import Flask, render_template, request
import random

# 1. app 설정
app = Flask(__name__)

# 2. 요청 경로(route) + 함수 만들기
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/hello/<string:name>')
# url에서 name을 사용할 때 인자에 넣어줌
def hello(name):
    return render_template('hello.html', name=name)

@app.route('/lunch')
def lunch():
    menus = ['레드코코넛누들', '소블고기', '삼계탕', '싸이버거', '치킨']
    pick = random.choice(menus)
    return render_template('lunch.html', menus=menus, pick=pick)

@app.route('/naver')
def naver():
    return render_template('naver.html')

@app.route('/ping')
def ping():
    return render_template('ping.html')

@app.route('/pong')
def pong():
    # 사용자가 보낸 데이터를 받아와서
    text = request.args.get('say') 
    print(request.args) # => ImmutableMultiDict([('say', '말')])
    # 템플릿에 넘겨준다.
    return render_template('pong.html', text=text)

@app.route('/random')
def random_game():
    return render_template('random_game.html')

@app.route('/result')
def result():
    mood = request.args.get('mood')
    weather = request.args.get('weather')
    playlist = {
        '외로움' : '"https://www.youtube.com/embed/IPfJnp1guPc"'
    }
    music = random.choice(playlist[mood])
    return render_template('result_page.html', mood=mood, weather=weather, music=music)
# http://ba99bfb3.ngrok.io/random 참고

# main이면 계속 실행시킴
if __name__ == '__main__':
    app.run(debug=True)