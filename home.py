from crypt import methods
from flask import Flask, render_template
from app import call, calling
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about/')
def about():
    return render_template('about.html')

@app.route('/listings/')
def listings():
    return render_template('listings.html')

@app.route('/contact/')
def contact():
    return render_template('contact.html')

@app.route('/bato/')
def bato():
    return render_template('bato.html', call=call(), calling=calling())  

if __name__ == '__main__':
    app.run(debug=True)





    


