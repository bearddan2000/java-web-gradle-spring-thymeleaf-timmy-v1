import logging

logging.basicConfig(level=logging.INFO)

class Week():
    def __init__(self, d, index=0):
        self.num = len(d['week-abbv'])-index
        self.to = d['week-abbv'][index]['to']
        self._from = d['week-abbv'][index]['from']