# from flask import Flask, render_template

# app = Flask(__name__)


# @app.route('/')
# def index():
#     return '<h1>hello from virtual env </h1>'


# if __name__ == '__main__':
#     app.run('0.0.0.0', 8888)

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run('0.0.0.0', 8888)
