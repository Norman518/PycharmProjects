from flask import Flask, render_template

app = Flask(__name__)
print(__name__)


@app.route('/')
def home_page():
    return render_template('index.html')


@app.route('/<string:page_name>')
def dynamic_page(page_name):
    return render_template(page_name)
