import uuid

from flask import Flask, request, jsonify

from main import config
from main import database
from main.database import Fruit

app = Flask(__name__)


@app.route('/fruits', methods=['GET', 'POST'])
def fruit_api():

    def get_fruits():
        fruits = database.find_fruits()
        res = {
            'result': 'OK',
            'fruits': fruits
        }
        return res

    def post_fruit(data):
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
        return jsonify(get_fruits())
    else:
        return jsonify(post_fruit(request.json))


if __name__ == "__main__":
    conf = config.AppConf().get_conf()
    app.run(host=conf['server']['host'], port=conf['server']['port'],
            debug=True)
