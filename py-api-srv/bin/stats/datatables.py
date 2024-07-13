from common import switch_lst

def fetch_datatables(SERVICE, lst: list):
    catagory = "datatable"
    switch_lst(lst, f'{SERVICE}/{catagory}')