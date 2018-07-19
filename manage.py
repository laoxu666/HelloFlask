from flask import Flask, render_template
# 安装驱动 pip install flask-script
from flask_script import Manager

app = Flask(__name__)

manager = Manager(app=app)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/index/')
def index():
    return '这是index!'

@app.route('/say/')
def say():
    # result = 1/0
    return "<h1>Say</h1>"

@app.route('/template/')
def temp():
    ret  = render_template('hello.html')
    print(ret)
    print(type(ret))

    return ret

if __name__ == '__main__':
    # app.run(debug=True,port=8000,host='0.0.0.0')
    manager.run()


