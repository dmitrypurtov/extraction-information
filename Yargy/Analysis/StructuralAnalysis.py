from dateanalysis import ExtractionDate
import datetime
import json

JSON_RESULT = ""

extractionDate = ExtractionDate()
extractionDate.setText("18 июля 2016")
date = extractionDate.getDate()

print(date)
