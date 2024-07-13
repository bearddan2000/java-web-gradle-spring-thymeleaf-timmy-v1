from common import switch_lst

SERVICE = "/trends"

def fetch_trends(PREV_SERVICE: str, lst: list):
    for graph_type in ['basic','linear', 'expo', 'log']:
        catagory = f'{PREV_SERVICE}{SERVICE}/{graph_type}'
        switch_lst(lst, catagory)