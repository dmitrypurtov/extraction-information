import os
import json
from bs4 import BeautifulSoup

class DataLoader:
    def __init__(self):
        self

    def getTextList(self):
        loaded_json = []
        result = []
        path = os.path.dirname(os.path.abspath(__file__)) + "\\" + 'data.txt'

        with open(path, encoding='utf-8') as fh:
            data = json.load(fh)

        print(data)


>> > markup = '<a href="http://example.com/">\nI linked to <i>example.com</i>\n</a>'
>> > soup = BeautifulSoup(markup)
>> > soup.get_text()
u'\nI linked to example.com\n'


        with open(path, "r", encoding="utf8") as myfile:
            text = myfile.readlines()

        with open(path) as json_file:
            loaded_json = json.loads(json_file)
            for p in loaded_json['items']:
                result.insert(p['description'])
        return result


test = DataLoader()
textList = test.getTextList()

print(textList)
