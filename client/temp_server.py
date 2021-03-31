import socket
import json

city = ["Bergen", "Oslo"]


def response(request: str) -> str:
    global city

    input_ = request.split()
    method = input_[0] + input_[1] if len(input_) > 1 else None
    if method == "getplace":
        return ";".join(city).encode()


def get_all_data():
    with open("temp_data.json", "r") as file:
        data = json.dumps(file.read())
    file.close()
    return data


def get_help_client():
    with open("requests.json", "r") as file:
        data = json.dumps(file.read())
    file.close()
    return data


def close():
    sock.shutdown(socket.SHUT_RDWR)
    sock.close()
    print("server closed")


if __name__ == '__main__':
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # Sets TCP timeout to 1 sec
    sock.bind(("127.0.0.1", 5009))
    sock.listen()

    while True:
        conn, _ = sock.accept()
        while request_message := conn.recv(1024).decode():
            print(request_message)  # prints request from client
            if request_message == "get data -all":
                all_data = get_all_data()
                conn.send(all_data.encode())
            elif request_message == "ping":
                conn.sendall("pong".encode())
            elif request_message == "help":
                help_request = get_help_client()
                conn.send(help_request.encode())
            elif request_message == "get place":
                conn.sendall(response(request_message))
            elif request_message == "close":
                close()
