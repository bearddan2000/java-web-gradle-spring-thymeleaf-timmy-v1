from common import switch_lst, FEATURES, WEEKS

SERVICE = "/compare"

def create_other_week(lst, week_url):
    for i in range(0, WEEKS):
        for j in range(i+1, WEEKS):
            lst.append(f'{week_url}/week/{i}/{j}')

def create_other_weekday(lst, weekday_url):
    for i in range(0, 5):
        for j in range(i+1, 5):
            lst.append(f'{weekday_url}/weekday/{i}/{j}')

def create_other_month(lst, month_url):
    for i in range(1, 5):
        for j in range(i+1, 5):
            lst.append(f'{month_url}/month/{i}/{j}')

def create_other_month_weekday(lst, month_url):
    for i in range(1, 5):
        for j in range(i, 5):
            for k in range(0, 5):
                lst.append(f'{month_url}/month/weekday/{i}/{j}/{k}')

def create_other_quarter(lst, quarter_url):
    lst.append(f'{quarter_url}/quarter/3/4')

def create_other_quarter_weekday(lst, quarter_url):
    for i in range(0, 5):
        lst.append(f'{quarter_url}/quarter/weekday/3/4/{i}')

def fetch_compare(PREV_SERVICE: str, lst: list):
    for graph_type in ['line', '3dbar', 'bar', 'barh', '3dscatter',
        'scatter', 'pie', 'box', 'violin', 'stack', 'stair']:
        switch_lst(lst, f'{PREV_SERVICE}{SERVICE}/self/{graph_type}')

    for graph_type in ['line', '3dbar', 'bar', 'barh', '3dscatter',
        'scatter', 'pie', 'box', 'violin', 'stack', 'stair']:
        for feature in FEATURES:
            url=f'{PREV_SERVICE}{SERVICE}/other/{graph_type}/{feature}'
            create_other_week(lst, url)
            create_other_weekday(lst, url)
            create_other_month(lst, url)
            create_other_month_weekday(lst, url)
            create_other_quarter(lst, url)
            create_other_quarter_weekday(lst, url)