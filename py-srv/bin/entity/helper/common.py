import logging

logging.basicConfig(level=logging.INFO)

def get_abbr(d, key):
    return [ item['desc'] for item in d[key]]

def get_id_notes(d, report_id, day_id, key):
    notes = []
    abbr_key = key + "-abbv"
    abbr = get_abbr(d, abbr_key)
    day = d['projects'][report_id]['reports'][day_id][key]
    abbr_id = day['id']
    id = abbr[abbr_id]
    return abbr_id, id