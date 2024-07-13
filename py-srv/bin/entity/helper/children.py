import logging

from entity.helper.common import get_id_notes, get_abbr

logging.basicConfig(level=logging.INFO)

class Element():
    def __init__(self, report_id, day_id, d, key):
        self.notes = []
        self.num_id, self.id = get_id_notes(d, report_id, day_id, key)
        #day_id = int(day_id)-1
        for note in d['projects'][report_id]['reports'][day_id][key]['notes']:
            data = d[f'{key}-notes']
            res = data[note]
            self.notes.append(res['desc'])

class Other():
    def __init__(self, report_id, day_id, d):
        self.notes = []
        abbr = get_abbr(d, 'notes-abbv')
        lst = d['projects'][report_id]['reports'][day_id]['notes']
        for item in lst:
            note = abbr[item]
            self.notes.append(note)

class Report():
    def __init__(self, report_id, day_id, d):
        day_lst = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
        self.day = day_lst[day_id]
        self.bedtime = Element(report_id, day_id, d, 'bedtime')
        self.sleep = Element(report_id, day_id, d, 'sleep')
        self.eat = Element(report_id, day_id, d, 'eat')
        self.morning = Element(report_id, day_id, d, 'morning')
        self.bus = Element(report_id, day_id, d, 'bus')
        self.hygien = Element(report_id, day_id, d, 'hygien')
        self.other = Other(report_id, day_id, d)