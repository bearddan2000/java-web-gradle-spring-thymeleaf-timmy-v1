from common import switch_lst

SERVICE = '/types'

def fetch_graph_type(PREV_SERVICE: str, lst: list):
    _type = [
        'scatter', '3dscatter', '3dscattercurve', 'stem', '3dstem', 
        'polar', "angle", "stair",
        'line', '3dline', 'bar', '3dbar', 'hbar', 'count', 
        'dis', 'ecdf', 'box', 'violin', 'specgram',
        '3dwireframe', '3dcontour', '3dsurface',
        '3dpolygon'
    ]
    for graph_type in _type:
        switch_lst(lst, f'{PREV_SERVICE}{SERVICE}/{graph_type}')

def fetch_graph_distribution(PREV_SERVICE: str, lst: list):
    _type = [
        'normal', 'poisson'
    ]
    for graph_type in _type: 
        switch_lst(lst, f'{PREV_SERVICE}{SERVICE}/{graph_type}')
