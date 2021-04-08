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

With [Python 3.8+](https://Python.org/) installed with numpy

To install numpy use
    $ python -m pip install numpy

Then run from project root:

    $ python server/server.py
    $ python server/weather_station_data_sender.py
    $ python server/client_server.py
    $ python client/WeatherAppClient.py


The`WeatherAppClient` is a command line program. \
You can use it to view the weather data that has been generated

To see possible commands, type:

    $ WAclient> help


To recieve all data since the simulation start, type:

    $ WAclient> get data all

## Running with docker 

Clone the repo and run this command in the project root:
    
    docker compose up --build --force-recreate

## About

Data will be periodically genereated from `station.py`. `weather_station_data_sender.py` then transmits
the data by UDP to `server.py` which stores it to `data.json`. This data can then get read from `client_server.py` with TCP
by the command line program `WeatherAppClient.py`.


<h4 align="center">
  <img alt="WeatherModel" src="img/model1.png">
</h4>


## Known bugs

`data.json` will eventually get very big, limiting *the whole goddamn operation.*

`docker_entrypoint.sh` may be changed by Git automatically to have a CLRF ending on Windows machine if this option is enabled in your local Git. When `docker_entrypoint.sh` has End of line sequence set as CLRF the `docker compose up` command will fail to launch the server, and you will get a error that may look like `standard_init_linux.go:219: exec user process caused: no such file or directory`. The fix is either no not use Windows EOL symbols or change just `docker_entrypoint.sh` EOL.

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
