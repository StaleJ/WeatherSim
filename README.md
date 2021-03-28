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

With [Python 3](https://Python.org/) installed, run

    $ python3 WeatherData.py
    $ python3 WeatherAppClient.py


The`WeatherAppClient` is a command line program. \
You can use it to view the weather data that has been generated

To see possible commands, type

    $ WAclient> help


To see all data since simulation start, type

    $ WAclient> get data -all


## About

Data will be periodically genereated from `Station.py` which is called by
WeatherBaseClient. This data is then forwarded by UDP to Server.py` which stores this data.

<h4 align="center">
  <img alt="WeatherModel" src="img/model1.png">
</h4>

Using the commandline from `client.py` you can retrieve various form of data from the server `server.py`.
## Known bugs

`DataStorage.txt` will eventually get very big, limiting the whole goddamn operation`.

---   

## Participants: 

Students: \
[`Ståle Jacobsen`](https://github.com/StaleJ) \
[`Erlend Haugen`](https://github.com/HaugPixel) \
[`Kim Andre Grønstøl`](https://github.com/KimAndreG) \
[`Martin Friedle`](https://github.com/mrtineide) \
[`Henrik Eide`](https://github.com/HenrikEide) 

TI's: \
[`Lenanomous`](https://github.com/daq012) \
[`Sedrick Varnes`](https://github.com/sedrickvarnes)


### CopyRight
<a href='https://pngtree.com/so/cartoon'>cartoon png from pngtree.com</a>