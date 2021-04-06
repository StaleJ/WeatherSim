from socket import socket, AF_INET, SOCK_DGRAM
import json


def create_socket(address, port):
    sock = socket(AF_INET, SOCK_DGRAM)
    sock.bind((address, port))
    return sock


def receive(sock):
    msg, addr = sock.recvfrom(2048)
    return msg.decode()


def saveToJson(jsondata: dict):
    # Read data.json and convert to dict
    a_file = open("data.json", "r")
    json_object = json.load(a_file)
    a_file.close()
    
    # Merging Dictionaries
    city = list(jsondata.keys()).pop()
    dict1 = json_object.get(city, {})
    dict2 = jsondata.get(city)
    dict1.update(dict2)
    json_object[city] = dict1
    
    # Dumps file
    a_file = open("data.json", "w")
    json.dump(json_object, a_file)

    a_file.close()


def main():
    address = "localhost"
    port = 50008

    sock = create_socket(address, port)
    count = 0

    while True:
        msg = receive(sock)
        jsonfile = json.loads(msg)
        saveToJson(jsonfile)
        count += 1
        print(count)


if __name__ == '__main__':
    main()




""" Server Plan

TCP server
Json format til db
2 clients

Process requests from:
- Weather station
    - Regardless of data type
    - Write to db
- Clients
    - Multithreaded with station
    - No login required
    - Ask and ye shall receive
    - No writing

Database:
- Json (maybe?)
- Only 1 write access at a time
- Read is fine tho

Per file:
1. Listen
2. Receive
3. Send
4. Send/receive db
...
5. Receive close -> close
6. Profit

"""