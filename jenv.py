import json


def getenv(key):
    file = open("jenv.json", "r")
    try:
        data = json.load(file)
        return data[key]
    except json.JSONDecodeError or KeyError:
        pass
