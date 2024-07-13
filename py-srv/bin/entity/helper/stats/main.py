import logging
import math
import numpy as np
from statistics import mean, median, mode, stdev, variance

from entity.helper.stats.common import math_ceil, math_round

logging.basicConfig(level=logging.INFO)

class Stats():
    def get_stats(self, lst: list):
        r = {}
        std = math_round(lst, stdev)
        var = math_round(lst, variance)
        r['max'] = max(lst)
        r['min'] = min(lst)
        r['range'] = r['max'] - r['min']
        r['mean'] = math_round(lst, mean)
        r['mode'] = mode(lst)
        r['median'] = median(lst)
        r['std_dev'] = std
        r['variance'] = var
        
        return r
