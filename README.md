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

# git

```bash
# 01- create a repo at github and git these commands
git remote add origin https://github.com/HaythamMohamd/app_python.git
git branch -M main
git push -u origin main
# 02- at local repo
git init
git add -A
git commit -m "Intial commit"
git log --oneline --graph --decorate
git log
git checkout feature
git checkout -b feature
git add -A
git commit -m "Changed readme from feature branch"
git switch main
git commit -am "Changed readme from main branch"
git merge feature
git commit -am "Accepted two changes from main and feature branch"
git push
git checkout  feature
git push --set-upstream origin feature

git reset
git revert

git tag v1.0.0
git push --tags

git stash
git stash pop

git reflog
```

testing feature branch
