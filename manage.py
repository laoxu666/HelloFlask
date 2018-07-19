import uuid

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

#string 请求参数中不能带斜线/  默认为路径分隔符
# @app.route('/student/<string:id>/')
# @app.route('/student/<int:id>/')
# @app.route('/student/<path:id>/')
# http://127.0.0.1:5000/student/100aaa/hehe/
@app.route('/student/<uuid:id>/')
def student(id):
    print(type(id))
    print(id)
    return "有趣的参数"

@app.route('/getuuid/')
def get_uuid():
    return str(uuid.uuid4())

# d8892d52-ffce-408c-9d55-59ee5cf1e448

if __name__ == '__main__':
    # app.run(debug=True,port=8000,host='0.0.0.0')
    manager.run()


