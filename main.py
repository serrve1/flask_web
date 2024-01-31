from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello World!!"

if __name__ == '__main__':
    app.run(debug = True) # flask에서는 이거만하면됨 (패스트api에서는 cmd: reload ) 