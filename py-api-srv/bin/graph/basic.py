from graph.ml import fetch_machine_learning
from graph.graph_type import fetch_graph_type, fetch_graph_distribution
from graph.regression import fetch_regression_type
from graph.compare import fetch_compare
from graph.relations import fetch_relation
from graph.distribution import fetch_distribution

SERVICE = 'graph'

def fetch_graphs(lst: list):
    fetch_machine_learning(SERVICE, lst)
    fetch_graph_type(SERVICE, lst)
    fetch_regression_type(SERVICE, lst)
    fetch_compare(SERVICE, lst)
    fetch_relation(SERVICE, lst)
    fetch_distribution(SERVICE, lst)