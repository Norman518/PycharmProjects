from flask import Flask, render_template
app = Flask(__name__)
print(__name__)

@app.route('/')
def hell_world():
    return render_template('index.html')