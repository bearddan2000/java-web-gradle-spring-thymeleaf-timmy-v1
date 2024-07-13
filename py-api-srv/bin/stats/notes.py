from common import switch_lst, WEEKS, FEATURES

def fetch_notes(SERVICE, lst):
    for week in FEATURES:
        switch_lst(lst, f'{SERVICE}/notes/frequency/{week}')
    for week in range(WEEKS):
        lst.append(f'{SERVICE}/notes/historical/week/{week}')