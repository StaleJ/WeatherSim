import json

from flask import Flask, render_template
from flask_restful import Resource, Api

app = Flask(__name__)
DATA = "../data.json"
api = Api(app)


@app.route('/')
def index():
    return render_template('index.html', data=get_city())


@app.route('/about')
def about():
    return render_template('about.html')


def get_all_data() -> dict:
    with open(DATA, "r") as file:
        json_object = json.loads(file.read())
    file.close()
    return json_object


def get_last_temp_rain():
    data = {}
    all_data = get_all_data()
    for city in all_data.keys():
        data[city] = all_data[city.capitalize()]

    return data


def get_city():
    list_ = []
    all_data = get_all_data()
    for city in all_data.keys():
        list_.append(city)

    return list_


#  REST API

class RainCity(Resource):

    def get(self, city: str):
        cap_city = city.capitalize()
        data = {}
        all_data = get_all_data()
        for i in range(min(24, len(all_data[cap_city]))):
            day = all_data[cap_city].popitem()
            data[day[0]] = day[1]['Rain']

        return data


class Rain(Resource):

    def get(self):
        data = {}
        all_data = get_all_data()
        for city in all_data.keys():
            data[city] = RainCity.get(self, city)
        return data


class LastCity(Resource):

    def get(self):
        return get_last_temp_rain()


#
# Actually setup the Api resource routing here
#

api.add_resource(RainCity, '/rain/<city>')
api.add_resource(Rain, '/rain')
api.add_resource(LastCity, '/last')

if __name__ == '__main__':
    app.run(debug=True)
