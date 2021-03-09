from flask import Flask
from flask import request
import random
import json

app = Flask(__name__)
with open('dinner.json') as f:
    food = json.load(f)

@app.route('/list_food')
def get_food():
    return '<br />'.join(list(dict.fromkeys(f['food'] for f in food)))

@app.route('/list_tastes')
def get_tastes():
    return '<br />'.join(list(dict.fromkeys(f['taste'] for f in food)))

@app.route('/dinner', methods = ['GET'])
def get_dinner():
    wanted_taste = request.args.get('味道')

    filtered_food = filter(lambda f: f['taste'] == wanted_taste, food)
    matching_food = list(filtered_food)

    if len(matching_food) == 0:
        return 'ahhh，没有符合主人口味的菜，你要饿死了'   
    else:
        chosen_food = random.choice(matching_food)['food']

    return '今晚为主人做' + chosen_food



