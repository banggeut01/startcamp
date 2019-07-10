import random
from flask import Flask, render_template

app = Flask(__name__)

# @app.route()는 경로를 만들어줌.
# 반환 return값은 str
@app.route('/')
def hello():
    # rendering "만들다" 서버에서 hello.html 파일을 만들어 클라이언트에 뿌려주는 것이다.
    # templates라고 하는 폴더 안에 있는 것만 렌더 템플릿을 해줄 수 있다!
    return render_template('hello.html')

@app.route('/hi')
def hi():
    # return '<h1>용흠 하이~</h1>'
    return render_template('hi.html')

# variable routing! 경로를 변수로 활용한다.
# <데이터타입:인자>
@app.route('/hi/<string:name>')
def higyo(name):
    # return f'{name}아 안녕?'
    return render_template('hi2.html', name1=name)

# /cube/<숫자>
# 세제곱  결과를 보여주는 페이지!
@app.route('/cube/<int:num>')
def triple_multi(num):
    return str(num**3)

# /lunch/사람이름
# ~에게 메뉴 중 하나 추천해주는 페이지
@app.route('/lunch/<string:name>')
def lunch_recom(name):
    menu = ['한식', '특식a', '특식b']
    # return f'{name}님 {random.choice(menu)}를 추천드립니다.'
    return render_template('lunch.html', name=name, pick=random.choice(menu))

# /lotto
# 로또 번호 6개를 추천해주는 페이지
@app.route('/lotto')
def lotto():
    lotto = random.sample(range(1,46), 6)
    return f'이번주 당첨번호는 {lotto}!!'

if __name__ == '__main__':
    # python app.py를 하면 아래의 코드 블록을 실행시킨다.
    app.run(debug = True)