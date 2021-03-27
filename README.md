<h4 align="center">
  <img alt="CloudyWeather" 
       src="cloud.png"
</h4>

***Welcome to the WeatherSimAPI!*** This program will simulate a weather database and
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

Data will be periodically genereated from `Simulation.py` which is called by
WeatherBaseClient. This data is then forwarded by UDP to `WeatherServer.py` which stores this data.

<h4 align="center">
  <img alt="WeatherModel" src="Model1.png">
</h4>

Using the client `WeatherClient.py` you can retrieve information from the server `WeatherServer.py`

## Known bugs

`DataStorage.txt` will eventually get very big, limiting the whole goddamn operation`.

   

###Participants: 

Students: \
[`Ståle Jacobsen`](https://github.com/noffle/) \
[`Erlend Haugen`](https://github.com/HaugPixel) \
[`Kim Andre Grønstøl`](https://github.com/KimAndreG) \
[`Martin Friedle`](https://github.com/noffle/twitter-kv) \
[`Henrik Eide`](https://github.com/HenrikEide) 

TI's: \
[`Lenanomous`](https://github.com/) \
[`Sedrick Varnes`](https://github.com/sedrickvarnes)


###CopyRight
<a href='https://pngtree.com/so/cartoon'>cartoon png from pngtree.com</a>