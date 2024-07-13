
def fetch_machine_learning(PREV_SERVICE: str, lst: list):
    SERVICE = "/ml"
    for graph_type in ['forecast', 'trend']:
        for _type in ['3','7', '30']:
            lst.append(f'{PREV_SERVICE}{SERVICE}/{graph_type}/{_type}')
