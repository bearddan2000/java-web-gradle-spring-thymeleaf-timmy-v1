import logging

from entity.helper.children import Report, Element
from entity.helper.week import Week
from entity.helper.legend import Legend
from entity.helper.stats.main import Stats

logging.basicConfig(level=logging.INFO)

class Project():
    def __init__(self, report_id, d):
        self.reports = [ Report(report_id, i, d) for i in range(0, 5)]
        self.bedtime_lst = [item.bedtime.num_id for item in self.reports]
        self.sleep_lst = [item.sleep.num_id for item in self.reports]
        self.eat_lst = [item.eat.num_id for item in self.reports]
        self.morning_lst = [item.morning.num_id for item in self.reports]
        self.bus_lst = [item.bus.num_id for item in self.reports]
        self.hygien_lst = [item.hygien.num_id for item in self.reports]
        self.create_stats()

    def create_stats(self):
        self.bedtime_stat = self._get_stats(self.bedtime_lst)
        
        self.sleep_stat = self._get_stats(self.sleep_lst)
        
        self.eat_stat = self._get_stats(self.eat_lst)
        
        self.morning_stat = self._get_stats(self.morning_lst)

    def _get_stats(self, lst: list):
        o = Stats()
        return o.get_stats(lst)
