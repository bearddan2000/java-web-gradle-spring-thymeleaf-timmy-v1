import logging
from entity.helper.common import get_abbr

logging.basicConfig(level=logging.INFO)

class Legend():
    def __init__(self, d):
        self.bedtime_lst = get_abbr(d, 'bedtime-abbv')
        self.sleep_lst = get_abbr(d, 'sleep-abbv')
        self.eat_lst = get_abbr(d, 'eat-abbv')
        self.morning_lst = get_abbr(d, 'morning-abbv')