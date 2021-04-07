import json

from flask import Flask, render_template
from flask_restful import Resource, Api

app = Flask(__name__)
DATA = "../data.json"
api = Api(app)


@app.route('/', methods=['GET', 'POST'])
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


def get_city() -> list:  # Return
    list_ = []
    all_data = get_all_data()
    for city in all_data.keys():
        list_.append(city)

    return list_


# REST API

class City(Resource):

    def get(self, city, updates=24):
        cap_city = city.capitalize()
        data = {}
        all_data = get_all_data()
        for i in range(min(updates, len(all_data[cap_city]))):
            day = all_data[cap_city].popitem()
            data[day[0]] = day[1]

        return data


class Rain(Resource):

    def get(self):
        data = {}
        all_data = get_all_data()
        for city in all_data.keys():
            data[city] = City.get(self, city)
        return data


class Last(Resource):

    def get(self):
        data = {}
        all_data = get_all_data()
        for city in all_data.keys():
            data[city] = City.get(self, city, 1)

        return data


class LastCity(Resource):

    def get(self, city):
        return {city: City.get(self, city, 1)}


class All(Resource):

    def get(self):
        return get_all_data()


#
# Setup the Api resource routing here
#

api.add_resource(City, '/<city>')  # gives data for the last 24h for specific city
api.add_resource(Rain, '/data')  # gives data for the last 24h for all cities
api.add_resource(Last, '/last')  # give last measurement for all cities
api.add_resource(LastCity, '/<city>/last')  # give last measurement for specific city
api.add_resource(All, '/all')  # Returns all data in the database

if __name__ == '__main__':
    app.run(debug=True)
