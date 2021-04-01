# TODO: Create TCP connection
# TODO: Create shell like client
# TODO: Create temp server?
# TODO: Make mock data
# TODO: Format data
# TODO: Decode data from server.
import math
import socket
import json
from io import StringIO

HOST = "127.0.0.1"
PORT = 5009


def request_to_server(request: str) -> str:
    sock.sendall(request.encode())
    resp = sock.recv(1024)
    return resp.decode()


def close_socket(request: str) -> None:
    sock.sendall(request.encode())
    sock.close()
    print("server closed")


def get_all_data(request: str) -> None:
    all_data = json.loads(request_to_server(request))  # loads converts str -> dict
    print(all_data)


def get_places() -> None:
    places = request_to_server("get place").split(";")
    print("Available places:")
    for p in places:
        print(p)
    while (p := input("places> ")) not in places:  # TODO : Kanskje gjøre dette på en bedre måte
        print(f"Place {p} is not available")
    request_to_server(f"get data {p}")


def get_help(request: str) -> None:
    _help = json.loads(request_to_server(request))
    _io = StringIO(_help)
    _dict = json.load(_io)
    longest_description = 0
    longest_key = 0
    for key, value in _dict.items():
        if len(value) > longest_description:
            longest_description = len(value)
        if len(key) > longest_key:
            longest_key = len(value)

    longest_description += 13
    longest_key += 9
    help_header = "All Commands!"
    rest = longest_description - len(help_header)
    print("-" * (math.floor(rest / 2) + 3) + help_header + "-" * (math.ceil(rest / 2) + 3) + "\n" + "|" + " " * (
                longest_description + 4) + "|")
    for k, v in _dict.items():
        print(
            f'|  Request: {k}' + " " * (longest_description - longest_key) + "  |" + f'\n|  Description: {v}' + " " * (
                        longest_description - 13) + '  |\n|  ' + " " * (
                longest_description) + "  |")
        print("-" * (longest_description + 6) + "\n")


# Forslag til get: get data <day>, get data <month> ? noe mer? rain and temp
# get data <place>

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
                if value == "day":
                    pass
                elif value == "place":
                    pass
                elif value == "month":
                    pass
                elif value == "temp":
                    pass
                elif value == "rain":
                    pass
                else:
                    print(f"{value} is not a valid request.\nUse help for more information")
            if method == "help":
                pass
            elif method == "close":
                pass
            else:
                print("Invalid command")

    except OSError as error:
        print(f"Cant connect to the server!\nOSError : {error}")
