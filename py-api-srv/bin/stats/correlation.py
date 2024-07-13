from common import add_list

def fetch_correlations(SERVICE, lst: list):
    catagory = "correlation"
    add_list(lst, f'{SERVICE}/{catagory}', 'coefficents')
    add_list(lst, f'{SERVICE}/{catagory}', 'pvalues')