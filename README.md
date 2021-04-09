<h4 align="center">
  <img alt="CloudyWeather" 
       src="img/cloud.png">
</h4>

**Welcome to the WeatherSim!** \
This program will simulate a weather database and
server in which for you to retrieve data from. Our main goal is to
 demonstrate basic socket programming with **UDP** and **TCP**.

---

## Usage

With [Python 3.8+](https://Python.org/) 

To install requirements/dependencies:
```zsh
$ pip install -r requirements.txt
```
Then run project:
```zsh
$ docker-compose up -d && docker attach user_client
```

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
