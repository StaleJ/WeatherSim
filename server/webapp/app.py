import json

from apispec import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin
from flask import Flask, render_template
from flask_apispec import doc
from flask_apispec.extension import FlaskApiSpec
from flask_apispec.views import MethodResource
from flask_restful import Resource, Api

app = Flask(__name__)
DATA = "../data.json"
api = Api(app)
app.config.update({'APISPEC_SPEC': APISpec(
    title="Group30's WeatherAPP",
    version='v1',
    plugins=[MarshmallowPlugin()],
    openapi_version='2.0.0'
),
    'APISPEC_SWAGGER_URL': '/swagger/',
    'APISPEC_SWAGGER_UI_URL': '/swagger-ui/'})

docs = FlaskApiSpec(app)


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


def get_city() -> list:
    list_ = []
    all_data = get_all_data()
    for city in all_data.keys():
        list_.append(city)

    return list_


def get_request(city, updates=24) -> dict:
    cap_city = city.capitalize()
    data = {}
    all_data = get_all_data()
    for i in range(min(updates, len(all_data[cap_city]))):
        day = all_data[cap_city].popitem()
        data[day[0]] = day[1]

    return data

# REST API


class City(MethodResource,Resource):

    @doc(description="Gives data for the last 24h for specific city", tags=["GET"])
    def get(self, city) -> dict:
        return get_request(city)


class AllData(MethodResource, Resource):

    @doc(description="Gives data for the last 24h for all cities", tags=["GET"])
    def get(self) -> dict:
        data = {}
        all_data = get_all_data()
        for city in all_data.keys():
            data[city] = get_request(city)
        return data


class Last(MethodResource, Resource):

    @doc(description="Give last measurement for all cities", tags=["GET"])
    def get(self) -> dict:
        data = {}
        all_data = get_all_data()
        for city in all_data.keys():
            data[city] = get_request(city,1)

        return data


class LastCity(MethodResource,Resource):

    @doc(description="Give last measurement for specific city", tags=["GET"])
    def get(self, city):
        return {city: get_request(city, 1)}


class All(MethodResource, Resource):
    @doc(description="Give last measurement for all cities",tags=["GET"])
    def get(self):
        return get_all_data()


#
# Setup the Api resource routing here
#

api.add_resource(City, '/<city>')  # gives data for the last 24h for specific city
api.add_resource(AllData, '/data')  # gives data for the last 24h for all cities
api.add_resource(Last, '/last')  # give last measurement for all cities
api.add_resource(LastCity, '/<city>/last')  # give last measurement for specific city
api.add_resource(All, '/all')  # Returns all data in the database
docs.register(City)
docs.register(AllData)
docs.register(Last)
docs.register(LastCity)
docs.register(All)

if __name__ == '__main__':
    app.run(debug=True)
