# 특정 가상환경에서만 사용 가능한 폴더들... 깃허브에 올리면 안되는 것을 ignore에 정리 
from flask import Flask, render_template, request

app = Flask(__name__)
#@app.route('/')은 기본인 get방식으로 요청
#@app.route('/',methods= ['post'])처럼 방식을 지정할 수도 있습니다. 
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/hello/<name>')
# 함수명을 index와 다르게 주어야한다.
def hello(name):
    # flask는 request.args라는걸로 쿼리를 받는다.
    action = request.args.get('action')
    sound = request.args.get('sound')
    # 딕셔너리 형태로 적는게 효율적이다.
    return render_template('hello.html', data = {"name" : name ,"action": action,"sound" :sound} )

@app.route('/login', methods = ['GET','POST'] )
def login():
    if request.method == 'POST' :
        username = request.form.get('username')
        password = request.form.get('password')
        print(username , password)
        return "Success"
    elif request.method == 'GET':
        return render_template('login.html')


@app.route('/register', methods = ['GET','POST'] )
def register():
    if request.method == 'POST' :
        username = request.form.get('username')
        email = request.form.get('email')
        phone = request.form.get('phone')
        password = request.form.get('password')
        print(username , email, phone, password)
        return email
    elif request.method == 'GET':
        return render_template('register.html')

if __name__ == '__main__':
    app.run(debug = True) # flask에서는 이거만하면됨 (패스트api에서는 cmd: reload ) 