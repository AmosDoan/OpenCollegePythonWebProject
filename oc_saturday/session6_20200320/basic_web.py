from flask import Flask

# Flask 생성자를 통하여 Flask Class의 Instance를 생성하고, 그것을 app에 저장한다.
app = Flask(__name__)


# Web API를 두개 만들었다.
# / 주소에 대한 요청이 들어오면 실행되는 함수다.
@app.route('/')
def index():
    return "this is my homepage!"


# /about 주소에 대한 요청이 들어오면 실행되는 함수다.
@app.route('/about')
def about():
    return "저는 Amos입니다."

# Flask object의 run 메소드를 실행한다.
if __name__ == '__main__':
    app.run()