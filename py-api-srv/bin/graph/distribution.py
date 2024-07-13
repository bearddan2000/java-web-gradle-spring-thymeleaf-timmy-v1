from common import switch_lst

SERVICE = "/distribution"

def fetch_distribution(PREV_SERVICE: str, lst: list):
    switch_lst(lst, f'{PREV_SERVICE}{SERVICE}/histogram/bar')
    switch_lst(lst, f'{PREV_SERVICE}{SERVICE}/3dhistogram/none')
    switch_lst(lst, f'{PREV_SERVICE}{SERVICE}/cumulative/bar')
    switch_lst(lst, f'{PREV_SERVICE}{SERVICE}/3dcumulative/none')