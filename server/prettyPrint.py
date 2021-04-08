import json


def read_json(filename):
    with open(filename, "r") as file:
        data = json.loads(file.read())
    file.close()
    return data


def format1(data: dict):
    string = ""
    for key, value in data.items():
        string += key + ":\n"
        for k, v in value.items():
            string += " " * 4 + k[:10] + " at " + k[11:16] + ":\n"
            for n, m in v.items():
                string += " " * 8 + n + ": " + str(m) + "\n"
    return string


def format2(data: dict):
    string = ""
    for key, value in data.items():
        string += key + ":\n"
        for k, v in value.items():
            string += " " * 4 + k[:10] + " at " + k[11:16] + ": "
            for n, m in v.items():
                string += n + ": " + str(m) + " "
            string += "\n"
    return string


if __name__ == '__main__':
    file = "./server/data.json"
    print("Testing with data from data.json\n")
    ex = {"Bergen": {"2021-04-06T16:23:42.696386": {"Rain": 0, "Temperature": 0}, "2021-04-06T16:23:42.802723": {"Rain": 0, "Temperature": 6.26}}}
    longer_ex = read_json(file)
    print("Format1\n")
    print(format1(ex))
    print("Format2\n")
    print(format2(ex))
    #print(format1(longer_ex)


