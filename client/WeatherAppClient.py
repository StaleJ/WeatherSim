# TODO: Create TCP connection
# TODO: Create shell like client
# TODO: Create temp server?
# TODO: Make mock data
# TODO: Format data
# TODO: Decode data from server.

import socket
import json
from io import StringIO

HOST = "127.0.0.1"
PORT = 5009


def request_to_server(request: str) -> str:
    sock.sendall(request.encode())
    resp = sock.recv(1024)
    return resp.decode()


def close_socket(request: str) -> None:  # Redundant?
    sock.sendall(request.encode())
    sock.close()
    print("server closed")


def get_all_data(request: str) -> None:
    all_data = json.loads(request_to_server(request))  # loads converts str -> dict
    print(all_data)


def get_help(request: str) -> None: # TODO : Fix this to get_json
    _help = json.loads(request_to_server(request))
    _io = StringIO(_help)
    _dict = json.load(_io)
    for k, v in _dict.items():
        print(f'Request: {k}. \nDescription: {v}\n')


if __name__ == '__main__':

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock_address = (HOST, PORT)
    sock.connect(sock_address)

    print("Press Enter to exit")
    while (command := input("WAclient> ")).lower():
        if command == "get data -all":
            get_all_data(command)
        elif command == "ping":
            ping = request_to_server(command)
            print(ping)
        elif command == "help":
            get_help(command)
        elif command == "close":
            close_socket(command)
        else:
            print("Invalid command")

# TODO : create help -> show possible commands
# TODO: get data -all command: do more testing
