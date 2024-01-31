# 특정 가상환경에서만 사용 가능한 폴더들... 깃허브에 올리면 안되는 것을 ignore에 정리 
from flask import Flask, render_template

app = Flask(__name__)

#@app.route('/')은 기본인 get방식으로 요청
#@app.route('/',methods= ['post'])처럼 방식을 지정할 수도 있습니다. 
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/hello')
# 함수명을 index와 다르게 주어야한다.
def hello():
    return "안녕 반가워"


if __name__ == '__main__':
    app.run(debug = True) # flask에서는 이거만하면됨 (패스트api에서는 cmd: reload ) 