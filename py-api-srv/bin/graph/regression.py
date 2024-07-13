from common import switch_lst

def fetch_regression_type(PREV_SERVICE: str, lst: list):
    reg_lst = [
        'linear', 'expo', 'log', 'cubic', 'quad',
        'sin', 'cos', 'tan',
        'arcsin', 'arccos', 'arctan'
    ]
    for graph_type in reg_lst:
        switch_lst(lst, f'{PREV_SERVICE}/regression/{graph_type}')