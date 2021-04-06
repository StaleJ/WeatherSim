import socket
import json

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
    else:
        print("Error: Request not recognised")


def read_data(filename):
    with open(filename, "r") as file:
        data = json.dumps(file.read())
    file.close()
    return data


def close():
    sock.shutdown(socket.SHUT_RDWR)
    sock.close()
    print("Server closed")


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
