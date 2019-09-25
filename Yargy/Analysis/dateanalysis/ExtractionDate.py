from .fact import DATE, Parser, DateFact
import datetime
import json

class ExtractionDate:
    text = ""

    def __init__(self):
        self

    def setText(self, text):
        self.text = text

    def getDate(self):
        parser = Parser(DATE)
        DateFact = parser.find(self.text)
        if DateFact:
            return datetime.date(DateFact.fact.year, DateFact.fact.month, DateFact.fact.day)
        return None

    def getJson(self):
        data = {
            "name": "John",
            "age": 30,
            "city": "New York"
        }
        return json.dumps(data)