from flask import Flask, render_template
app = Flask(__name__)
print(__name__)

@app.route('/')
def defaultpage():
    return render_template('index.html')

@app.route('/index.html')
def homepage():
    return render_template('index.html')

@app.route('/work.html')
def workpage():
    return render_template('work.html')

@app.route('/works.html')
def workspage():
    return render_template('works.html')

@app.route('/contact.html')
def contactpage():
    return render_template('contact.html')

@app.route('/components.html')
def componentspage():
    return render_template('components.html')

@app.route('/about.html')
def aboutpage():
    return render_template('about.html')