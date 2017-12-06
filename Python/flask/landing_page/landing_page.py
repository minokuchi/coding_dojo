from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', name="Mark", desc="Coding Dojo Ninja")

@app.route('/ninjas')
def ninja_page():
    return render_template('ninjas.html')

@app.route('/dojos')
def new_dojo():
    return render_template('dojos.html')

@app.route('/process')
def process():
    return render_template('index.html', name="Mark", desc="Coding Dojo Ninja")

app.run(debug=True)

