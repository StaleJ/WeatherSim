import socket
import json
from io import StringIO

HOST = "server"
PORT = 5009
ENTERPRISE_FRIENDLY_HELLO = "HELLO SERVER"


def request_to_server(request: str) -> str:
    # Send first request to database server
    sock.sendall(request.encode())
    # Receive the size of the file from database
    size_of_file = int(sock.recv(512).decode())
    # Send ok message back, server expects it.
    sock.sendall(ENTERPRISE_FRIENDLY_HELLO.encode())
    # Receive the file from database over the network with the given size
    resp = sock.recv(size_of_file)
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
    while p := input("places> ").capitalize():
        if p in places:
            data = request_to_server(f"getcity;{p}")  # eks get;bergen
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


def get_help(request: str) -> None:
    _help = get_json(request)
    print("OPTIONS")
    print(" " * 8 + "The following options can be used to influence the behavior of Weather app.\n")
    for k, v in _help.items():
        print(" " * 8 + k)
        print(" " * 11 + v + "\n")


if __name__ == '__main__':
    print("Starting Web App Client...")

    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock_address = (HOST, PORT)
        sock.connect(sock_address)

        print("Tell me")
        print("who let the dogs out")
        x = input()
        print(x)
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
                    print("Not supported operation")
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
