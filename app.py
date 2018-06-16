from flask import Flask

app = Flask(__name__)

import json
import random


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/roll')
def roll_the_dice():
    die1 = random.randint(1, 12)
    return die1


@app.route('/test')
def hello_test():
    return 'Hello Test!'


if __name__ == '__main__':
    app.debug = True
    app.run()
