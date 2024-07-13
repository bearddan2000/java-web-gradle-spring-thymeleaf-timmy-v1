from common import switch_lst
from stats.compare import fetch_other
from stats.distribution import fetch_distribution
from stats.correlation import fetch_correlations
from stats.trends import fetch_trends
from stats.datatables import fetch_datatables
from stats.notes import fetch_notes

SERVICE = 'stats'

def fetch_stats(lst: list):
    fetch_datatables(SERVICE, lst)
    switch_lst(lst, SERVICE)
    fetch_correlations(SERVICE, lst)

    fetch_trends(SERVICE, lst)
    fetch_distribution(SERVICE, lst)
    switch_lst(lst, f'{SERVICE}/compare/self')
    fetch_other(SERVICE, lst)
    fetch_notes(SERVICE, lst)