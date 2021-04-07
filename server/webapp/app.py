import json

from flask import Flask, render_template
from flask_restful import Resource, Api

app = Flask(__name__)
DATA = "../data.json"
api = Api(app)


@app.route('/')
@app.route('/<name>')
def hello(name=None):
    return render_template('index.html', name=name)


def get_all_data() -> dict:
    with open(DATA, "r") as file:
        json_object = json.loads(file.read())
    file.close()
    return json_object


#  REST API

class RainCity(Resource):

    def get(self, city):
        data = {}
        all_data = get_all_data()
        for i in range(min(24, len(all_data[city]))):
            day = all_data[city].popitem()
            data[day[0]] = day[1]['Rain']

        return data


class Rain(Resource):

    def get(self):
        data = {}
        all_data = get_all_data()
        for city in all_data.keys():
            data[city] = RainCity.get(self,city)
        return data


#
# Actually setup the Api resource routing here
#

api.add_resource(RainCity, '/rain/<city>')
api.add_resource(Rain, '/rain')

if __name__ == '__main__':
    app.run(debug=True)
