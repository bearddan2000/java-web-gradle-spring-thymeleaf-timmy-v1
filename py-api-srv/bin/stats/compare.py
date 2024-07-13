from common import switch_lst

from graph.compare import create_other_week, create_other_weekday, \
    create_other_month, create_other_month_weekday, \
    create_other_quarter, create_other_quarter_weekday

def fetch_other(SERVICE, lst):
    create_other_week(lst, f'{SERVICE}/compare/other')
    create_other_weekday(lst, f'{SERVICE}/compare/other')
    create_other_month(lst, f'{SERVICE}/compare/other')
    create_other_month_weekday(lst, f'{SERVICE}/compare/other')
    create_other_quarter(lst, f'{SERVICE}/compare/other')
    create_other_quarter_weekday(lst, f'{SERVICE}/compare/other')