from socket import socket
import json

if __name__ == '__main__':
    sock = socket()
    sock.bind(("127.0.0.1", 5009))
    sock.listen()

    while True:
        conn, _ = sock.accept()
        while True:
            request_message = conn.recv(1024)
            if not request_message:
                conn.close()
                break
            conn.sendall("pong".encode())


def get_all_data():
    with open("temp_data.json", "r") as file:
        data = json.load(file)
    file.close()
    return data


print(get_all_data())
