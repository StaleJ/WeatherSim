import socket
import json
from io import StringIO

ADDRESS = "127.0.0.1"
PORT = 5009
DATABASE = "data.json"
HELP = "requests.json"


def response(request: str) -> None:
    if request == "getall":
        all_data = read_data(DATABASE)
        conn.sendall(all_data.encode())
    elif request == "help":
        help_data = read_data(HELP)
        conn.sendall(help_data.encode())
    elif request == "close":
        close()
    elif request == "getplace":
        places = get_place()
        conn.sendall(places.encode())
    elif "getcity" in request:
        city_data = get_city_data(request.split(";")[1])
        conn.sendall(city_data.encode())
    else:
        print("Error: Request not recognised")


def read_data(filename):
    with open(filename, "r") as file:
        data = json.dumps(file.read())
    file.close()
    return data


def get_json(filename: str) -> dict:
    with open(filename, "r") as _json:
        _dict = json.load(_json)
    return _dict


def close():
    sock.shutdown(socket.SHUT_RDWR)
    sock.close()
    print("Server closed")


#--------------------------------------get commands-------------------------------------
def get_place() -> str:
    _data = get_json(DATABASE)
    return ";" .join(_data.keys())


def get_city_data(city) -> str:
    _data = get_json(DATABASE)
    if city in _data.keys():
        return str(_data[city])
    else:
        return "Place not found"




if __name__ == '__main__':
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # Sets TCP timeout to 1 sec
    sock.bind((ADDRESS, PORT))
    sock.listen()

    while True:
        conn, _ = sock.accept()
        while request_message := conn.recv(1024).decode():
            print(request_message)  # print request from client
            response(request_message)
