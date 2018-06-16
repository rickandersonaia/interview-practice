from flask import Flask

app = Flask(__name__)

import json
import random


@app.route('/')
def hello_world():
    return 'Hello World!'

# This route creates a random number from 1 to 12 and stores that value in a
# dice variable.  It then places those numbers in a dictionary and encodes them
@app.route('/roll')
def roll_the_dice():
    die1 = random.randint(1, 12)
    die2 = random.randint(1, 12)
    return json.JSONEncoder().encode({'die1': die1, 'die2': die2})


if __name__ == '__main__':
    app.debug = True
    app.run()
