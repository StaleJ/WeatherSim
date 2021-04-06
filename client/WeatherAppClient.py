import socket
import json
from io import StringIO

HOST = "127.0.0.1"
PORT = 5009


def request_to_server(request: str) -> str:
    sock.sendall(request.encode())
    resp = sock.recv(1024)
    return resp.decode()


def get_json(request: str) -> dict:
    _data = json.loads(request_to_server(request))
    _io = StringIO(_data)
    _dict = json.load(_io)
    return _dict


def close_socket(request: str) -> None:
    sock.sendall(request.encode())
    sock.close()
    print("server closed")


def get_all_data() -> None:
    all_data = get_json("getall")  # loads converts str -> dict
    print(all_data)


def get_places() -> None:
    places = request_to_server("getplace").split(";")
    print("Available places:")
    for p in places:
        print(p)
    while p := input("places> ").upper():
        if p in places:
            data = request_to_server(f"getcity;{p}")  # eks getbergen
            print(data)
        else:
            print(f"{p} is not available")


def get_temp() -> None:
    _temp = json.loads(request_to_server("gettemp"))
    print(f"The temperature at {', '.join(_temp.keys())}:\n")
    for k, v in _temp.items():
        print(" " * 8 + f"{k} is {v}°C.\n")


def get_rain() -> None:
    _rain = json.loads(request_to_server("getrain"))
    print(f"Rain at {', '.join(_rain.keys())}:\n")
    for k, v in _rain.items():
        print(" " * 8 + f"{k} has {v}mm rain.\n")


def get_month() -> None:
    months = request_to_server("getmonth").split(";")
    print("Available months:")
    for m in months:
        print(m)
    while m := input("months> "):
        if m in months:
            request_to_server(f"get data {m}")  # Eks: get data may
        else:
            print(f"{m} is not available")


def get_help(request: str) -> None:
    _help = get_json(request)
    print("OPTIONS")
    print(" " * 8 + "The following options can be used to influence the behavior of Weather app.\n")
    for k, v in _help.items():
        print(" " * 8 + k)
        print(" " * 11 + v + "\n")


if __name__ == '__main__':

    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock_address = (HOST, PORT)
        sock.connect(sock_address)

        print("Press Enter to exit")
        while (command := input("WAclient> ")).lower():
            input_ = command.split()
            method = input_[0] + input_[1] if len(input_) > 1 else input_[0]
            value = input_[2] if len(input_) > 2 else None
            if method == "getdata":
                if value == "place":
                    get_places()
                    continue
                elif value == "month":
                    get_month()
                    continue
                elif value == "temp":
                    get_temp()
                    continue
                elif value == "rain":
                    get_rain()
                    continue
                elif value == "all":
                    get_all_data()
                    continue
            if method == "help":
                get_help(method)
            elif method == "close":
                close_socket(method)
            else:
                print(f"{command} is not a valid request.\nUse help for more information")

    except OSError as error:
        print(f"Cant connect to the server!\nOSError : {error}")
