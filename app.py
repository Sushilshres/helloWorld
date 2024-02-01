from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World from Sushil Shrestha! I am adding my first code change.'

@app.route('/hello')
def hello():
    return render_template('hello.html')


if __name__ == '__main__':
    app.run()