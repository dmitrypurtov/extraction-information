from dateanalysis.fact import DATE, Parser, DateFact
from ipymarkup import show_markup
from DataLoader import DataLoader


line = DataLoader().getTextList().pop(0) + " 18 июля 2016"
parser = Parser(DATE)
matches = list(parser.findall(line))
spans = [_.span for _ in matches]
show_markup(line, spans)
