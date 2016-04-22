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

@app.route('/party')
def toggle_party():
    return hue.throw_party()

@app.route('/load')
def get_state():
    return hue.get_living_room_state()


if __name__ == '__main__':
    app.run()
