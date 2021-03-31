from time import sleep
import json

from station import StationSimulator

def write_json(data, filename='test_data_json.json'):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4, sort_keys=True, default=str)
    f.close()



if __name__ == "__main__":

    # Instantiate a station simulator
    bergen_station = StationSimulator(simulation_interval=1)
    # Turn on the simulator
    bergen_station.turn_on()

    # Two lists for temperature and precipitation
    jsonfile = {}

    # Capture data for 72 hours
    # Note that the simulation interval is 1 second
    for hours in range(5):
        sleep(1)
        with open("test_data_json.json", 'r') as f:
            jsonfile = json.load(f)
            location = str(bergen_station.location)
            month = bergen_station.month
            day = hours // 24
            rain = bergen_station.rain
            temp = bergen_station.temperature
            data = jsonfile[location]
            data[hours] = {
                "Month": month,
                "Day": day,
                "Rain": rain,
                "Temp": temp
            }
            jsonfile.update(data)
            write_json(jsonfile)
        f.close()



    # Shut down the simulation
    bergen_station.shut_down()

    # Print the collected data

