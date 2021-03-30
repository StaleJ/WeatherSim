# TODO: Create TCP connection
# TODO: Create shell like client
# TODO: Create temp server?
# TODO: Make mock data
# TODO: Format data
# TODO: Decode data from server.

import socket
import json

HOST = "127.0.0.1"
PORT = 5009


def request_to_server(sock: socket, command: str) -> str:
    sock.sendall(command.encode())
    resp = sock.recv(1024)
    return resp.decode()


def close_socket(sock: socket) -> None:
    print("test")
    sock.close()


if __name__ == '__main__':

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock_address = (HOST, PORT)
    sock.connect(sock_address)

    print("Press Enter to exit")
    while (command := input("WAclient> ")).lower():
        if command == "get data -all":
            test = json.loads(request_to_server(sock, command))
            print(test)
            type(test)
        elif command == "ping":
            ping = request_to_server(sock, command)
            print(ping)
        else:
            print("Invalid command")

# TODO : create help -> show possible commands
# TODO: get data -all command
