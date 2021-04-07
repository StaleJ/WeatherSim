import json

def read_json(filename):
    with open(filename, "r") as file:
        data = json.dumps(file.read())
    file.close()
    return data

def print_all(data):
    print(type(data))
    print(type(json.dumps(data)))


if __name__ == '__main__':
    filename = "./server/data.json"
    print("Just checking them types")
    ex = {"Bergen": {"2021-04-06T16:23:42.696386": {"Rain": 0, "Temperature": 0}, "2021-04-06T16:23:42.802723": {"Rain": 0, "Temperature": 6.26}}}
    # print(json.dumps(ex, indent=4))
    data = json.loads(read_json(filename))
    print_all(data)
