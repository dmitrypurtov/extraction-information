import os
import json
from bs4 import BeautifulSoup


class DataLoader:
    def __init__(self):
        self

    def getTextList(self):
        loaded_json = []
        result = []
        path = os.path.dirname(os.path.abspath(__file__)) + "\\" + 'data.json'
        with open(path, encoding='utf-8') as fh:
            loaded_json = json.load(fh)
        for item in loaded_json:
            description = item['description']
            description = BeautifulSoup(description).get_text()
            result.append(description)
        return result


# test = DataLoader()
# textList = test.getTextList()
# print(textList)
