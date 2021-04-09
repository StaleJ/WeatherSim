import socket
import json

ADDRESS = "127.0.0.1"
PORT = 5009
DATABASE = "./server/data.json"
HELP = "./server/requests.json"
ENTERPRISE_FRIENDLY_HELLO = "HELLO SERVER"


def send_file_size_to_client(buffer_size: int):
    conn.sendall(str(buffer_size).encode())
    ENTERPRISE_FRIENDLY_REPLY_FROM_CLIENT = conn.recv(512).decode()
    if ENTERPRISE_FRIENDLY_REPLY_FROM_CLIENT == ENTERPRISE_FRIENDLY_HELLO:
        return
    else:
        raise OverflowError(f"Client failed to say hello back properly, it said:{ENTERPRISE_FRIENDLY_REPLY_FROM_CLIENT}")


def response(request: str) -> None:
    # Step two
    if request == "getall":
        all_data = read_data(DATABASE)
        send_file_size_to_client(len(all_data))
        conn.sendall(all_data.encode())
    elif request == "help":
        help_data = read_data(HELP)
        send_file_size_to_client(len(help_data))
        conn.sendall(help_data.encode())
    elif request == "close":
        close()
    elif request == "getplace":
        places = get_place()
        send_file_size_to_client(len(places))
        conn.sendall(places.encode())
    elif "getcity" in request:
        city_data = get_city_data(request.split(";")[1])
        send_file_size_to_client(len(city_data))
        conn.sendall(city_data.encode())
    elif request == "getrain":
        rain_data = get_rain()
        send_file_size_to_client(len(rain_data))
        conn.sendall(rain_data.encode())
    elif request == "gettemp":
        temp_data = get_temp()
        send_file_size_to_client(len(temp_data)) 
        conn.sendall(temp_data.encode())
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


# --------------------------------------get commands-------------------------------------


def get_place() -> str:
    _data = get_json(DATABASE)
    return ";".join(_data.keys())


def get_city_data(city) -> str:
    _data = get_json(DATABASE)
    if city in _data.keys():
        return str(_data[city])
    else:
        return "Place not found"


def get_rain() -> str:
    _out = {}
    _data = get_json(DATABASE)
    for city in _data.keys():
        last_reading = list(_data[city].keys())[-1]
        _rain = _data[city][last_reading]["Rain"]
        _out[city] = _rain
    return json.dumps(_out)


def get_temp() -> str:
    _out = {}
    _data = get_json(DATABASE)
    for city in _data.keys():
        last_reading = list(_data[city].keys())[-1]
        _rain = _data[city][last_reading]["Temperature"]
        _out[city] = _rain
    return json.dumps(_out)


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
