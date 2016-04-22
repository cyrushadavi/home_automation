__author__ = 'Cyrus'
from flask import Flask
from flask import render_template
import hue
app = Flask(__name__)


@app.route('/')
def start():
    return render_template('index.html')

@app.route('/lights')
def toggle_lights():
    return hue.toggle_living_room()

if __name__ == '__main__':
    app.run()