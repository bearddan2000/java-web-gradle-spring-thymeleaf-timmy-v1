from common import add_list

def fetch_eat(SERVICE: str, lst: list, _type):
    add_list(lst, SERVICE, f'{_type}/eat/morning')

def fetch_sleep(SERVICE: str, lst: list, _type):
    add_list(lst, SERVICE, f'{_type}/sleep/eat')
    add_list(lst, SERVICE, f'{_type}/sleep/morning')
    fetch_eat(SERVICE, lst, _type)

def fetch_bedtime(SERVICE: str, lst: list, _type):
    add_list(lst, SERVICE, f'{_type}/bedtime/sleep')
    add_list(lst, SERVICE, f'{_type}/bedtime/eat')
    add_list(lst, SERVICE, f'{_type}/bedtime/morning')
    fetch_sleep(SERVICE, lst, _type)

def fetch_relation(PREV_SERVICE, lst):
    SERVICE = f'{PREV_SERVICE}/relations'
    graph_type = [
        'bar', 'scatter', 'histogram', 
        'cluster', 'heat', 'violin',
        'csd', "stack"
    ]
    for _type in graph_type:
        fetch_bedtime(SERVICE, lst, _type)