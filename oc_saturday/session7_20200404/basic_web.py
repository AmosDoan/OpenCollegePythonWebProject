from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return "welcome to my homepage!"


@app.route('/test')
def test():
    a = request.args.get('name')

    if a is None:
        return "hello"

    return "hello " + a


@app.route('/about')
def about():
    return render_template('introduce.html')


count = 0


@app.route('/visit')
def visit():
    global count
    count = count + 1

    if count == 1:
        return "당신은 1번째 방문객입니다! 축하합니다!"
    else:
        return "당신은 " + str(count) + "번째 방문객입니다!"


if __name__ == "__main__":
    app.run()