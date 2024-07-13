from common import switch_lst, FEATURES

def add_suffixed_lst(lst, service, suffix):
    dist = []
    switch_lst(dist, service)
    for i in dist:
        if "current" in i or "prev" in i:
            lst.append(i)
        else:
            lst.append(f'{i}/{suffix}')

def lst_suffixs(lst, service):
    for suffix in FEATURES:
        add_suffixed_lst(lst, service, suffix)

def fetch_distribution(SERVICE, lst: list):
    catagory = "distribution"
    frequency = f'{SERVICE}/{catagory}/frequency'
    normal = f'{SERVICE}/{catagory}/normal'
    poisson = f'{SERVICE}/{catagory}/poisson'

    add_suffixed_lst(lst, frequency, 'none')
    lst_suffixs(lst, normal)
    lst_suffixs(lst, poisson)