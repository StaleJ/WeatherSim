'''
	Simple udp socket that sendst the data from the weather station to localhost
'''
import socket
import sys
from time import sleep
from station import StationSimulator

HOST = 'localhost'  # TODO change this to the server where database is
PORT = 50008        # Arbitrary non-privileged port TODO define a better port?
sim_int = 0.1       # Float representing simulation interval, lower = faster

# Make the UDP socket used to send with
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    print('Socket created')
except socket.error as e:
    print('Failed to create socket', e)
    sys.exit()

# Simulate some data
print("starting simulation")
simulator = StationSimulator(simulation_interval=sim_int)
simulator.turn_on()
print("Sim turned on")

for _ in range(30):
    sleep(sim_int)
    # Get the data from station/simulation
    data = (simulator.rain, simulator.temperature,
            simulator.location, simulator.month)
    # Encode the data TODO decide the format of what to send, now its arbitrary
    try:
        s.sendto(str(data).encode(), ((HOST, PORT)))
    except socket.error as e:
        print("Could not send data: ", e)

simulator.shut_down()
print("Stopped simulation...")

print("closing socket and weather station...")
s.close()
sys.exit()
