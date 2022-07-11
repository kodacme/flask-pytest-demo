import uuid

from flask import Flask, request, jsonify

from app import database
from app.database import Fruit

app = Flask(__name__)


@app.route('/hello', methods=['GET', 'POST'])
def hello():

    def get_hello(data):
        name = data['name']
        fruits = database.find_fruits()
        print(fruits)
        fruits = list(filter(lambda f: f.name == name, fruits))
        res = {
            'result': 'OK',
            fruits: fruits
        }
        return res

    def post_hello(data):
        name = data['name']
        fruit_type = data['type']
        fruit_id = str(uuid.uuid4())
        fruit = Fruit(fruit_id, name, fruit_type, False)
        database.save_fruit(fruit)

        res = {
            'result': 'OK',
            'id': fruit_id
        }
        return res

    if request.method == 'GET':
        return jsonify(get_hello(request.args.to_dict()))
    else:
        return jsonify(post_hello(request.json))


if __name__ == "__main__":
    app.run(debug=True)
