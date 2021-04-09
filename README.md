<h4 align="center">
  <img alt="CloudyWeather" 
       src="img/cloud.png">
</h4>

**Welcome to the WeatherSim!** \
This program will simulate a weather database and
server in which for you to retrieve data from. Our main goal is to
 demonstrate basic socket programming with **UDP** and **TCP**.

---

# Installation

## Configuration

With [Python 3.8+](https://Python.org/) 

To install requirements/dependencies:
```sh
$ pip install -r requirements.txt  # or
$ pip3 install -r requirements.txt
```
## Production
### Automatically with Docker
For a very quick and easy deploy of your app we recommend hosting the app in a Docker container and running that.
It is fairly straight forward:
```sh
$ sudo docker-compose up -d && sudo docker attach user_client
```
Press **Return** after you have run the command above, and you should be greeted with the message:
```sh
### WeatherAPP 2.0 ###
WebApp running on http://0.0.0.0:5000/
Press 'help' for Commands | press Enter to exit 
```

If changes to the project are made you can redeploy with:
```sh
$ docker-compose up -d --build --force-recreate && sudo docker attach user_client
```
### Manually
For manually deploying you need to run these python scripts simultaneous in their specific folders:
```sh
$ python weather_app_client.py           # /client
$ python client_server.py                # /server
$ python server.pu                       # /server
$ python weather_station_data_sender.py  # /station
$ python app.py                          # /server/webapp
```
**NOTE:** We highly recommend you to use Docker instead of the manual approach.  
# Usage
We have three ways of interacting with the app, a shell `WeatherAppClient`, [Website](group30.codes), and [REST api](group30.codes/swagger-ui/).  


## How to use the shell/CLI
The`WeatherAppClient` is a command line program. \
You can use it to view the weather data that has been generated

To see possible commands, type:
```zsh
$ WAclient> help
```

To recieve all data since the simulation start, type:
```zsh
$ WAclient> get data all
```

You can also use the flask app we made to view the data in a 

## About

Data will be periodically genereated from `station.py`. `weather_station_data_sender.py` then transmits
the data by UDP to `server.py` which stores it to `data.json`. This data can then get read from `client_server.py` with TCP
by the command line program `WeatherAppClient.py`.


<h4 align="center">
  <img alt="WeatherModel" src="img/model1.png">
</h4>


## Known bugs

`data.json` will eventually get very big, limiting *the whole goddamn operation.*

---   

## Participants: 

Students: \
[`Ståle Jacobsen`](https://github.com/StaleJ) \
[`Erlend Haugen`](https://github.com/HaugPixel) \
[`Kim Andre Grønstøl`](https://github.com/KimAndreG) \
[`Martin Eide`](https://github.com/mrtineide) \
[`Henrik Eide`](https://github.com/HenrikEide) 

TI's: \
[`Lenanomous`](https://github.com/daq012) \
[`Sedrick Varnes`](https://github.com/sedrickvarnes)


### CopyRight
<a href='https://pngtree.com/so/cartoon'>cartoon png from pngtree.com</a>
