import os
import json

loaded_json = []

path = os.path.dirname(os.path.abspath(__file__)) + "\\" + 'data.txt'

with open(path) as json_file:
    loaded_json = json.load(json_file)


class DataLoader:
    def __init__(self):
        self