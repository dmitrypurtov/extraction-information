from yargy import Parser
from fulldate import FULL_DATE_PARSER, FullDateFact
from ipymarkup import show_markup
from dataloader import DataLoader

line = DataLoader().getTextList().pop(0) + " 18 июля 2016"
parser = Parser(FULL_DATE_PARSER)
matches = list(parser.findall(line))
spans = [_.span for _ in matches]
show_markup(line, spans)