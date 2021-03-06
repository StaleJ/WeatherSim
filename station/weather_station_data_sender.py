'''
	Simple udp socket that sends the data from the weather station to localhost
'''
import json
import socket
import sys
from datetime import datetime, timedelta
from time import sleep

from station import StationSimulator

HOST = "server" if len(sys.argv)>1 else "localhost"

PORT = 50008  # Arbitrary non-privileged port TODO define a better port?
sim_int = 0.1  # Float representing simulation interval, lower = faster

# Make the UDP socket used to send with
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    print('Socket created')
except socket.error as e:
    print('Failed to create socket', e)
    sys.exit()

# Simulate some data
print("Starting simulation from weather station container")
simulator = StationSimulator(simulation_interval=sim_int)
simulator.turn_on()
print("Sim turned on")

count = 0
for by in ["Stavanger","Bergen","Oslo"]:
    for i in range(50):  # 100 here is arbitrary, its just to make it not go forever
        count += 1
        sleep(sim_int)
        iso_date = datetime.now() + timedelta(hours=i)
        # Get the data from station/simulation
        data = {str(by): {
            iso_date.isoformat(): {
                "Rain": simulator.rain,
                "Temperature": simulator.temperature
            }
        }
        }

        # Convert to JSON/str we can use json.loads(receivedData.decode()) to decode it
        dataToSend = json.dumps(data)

        try:
            s.sendto(str(dataToSend).encode(), (HOST, PORT))
            print("Sent to socket this: ", dataToSend)  # Debug print
        except socket.error as e:
            print("Could not send data: ", e)

simulator.shut_down()
print("Stopped simulation now...")
print(count)

print("closing socket and weather station...")
print("Goodbye")
s.close()
sys.exit()
