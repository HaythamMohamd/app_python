# app pythonn

## intitialization

```bash
python -m venv venv
source venv/bin/activate
pip install flask
```

## Developmnet

```bash
python -m venv venv
source venv/bin/activate
pip freeze > requirements.txt
pip install -r requirements.txt
```

### main.py

```bash
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>hello from virtual env </h1>'


if __name__ == '__main__':
    app.run('0.0.0.0', 8888)

```

### wsgi.py

```bash
from main import app as application

if __name__ == '__main__':
    application.run()
```

## Run app

```bash
python3 main.py
or
gunicorn wsgi
```

testing main branch branch
