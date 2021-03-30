from socket import socket
import json
import unittest

def get_all_data():
    with open("temp_data.json", "r") as file:
        data = json.dumps(file.read())
    file.close()
    return data


if __name__ == '__main__':
    sock = socket()
    sock.bind(("127.0.0.1", 5009))
    sock.listen()

    while True:
        conn, _ = sock.accept()
        while True:
            request_message = conn.recv(1024)
            request_message_decoded = request_message.decode()
            print(request_message.decode())
            if not request_message_decoded:
                conn.close()
                break
            elif request_message_decoded == "get data -all":
                all_data = get_all_data()
                conn.send(all_data.encode())
            elif request_message_decoded == "ping":
                conn.sendall("pong".encode())


print(get_all_data())


