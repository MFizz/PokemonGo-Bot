from utils import coord2merc, merc2coord
from networkx.algorithms.clique import find_cliques

import networkx as nx
import numpy as np


class FindBiggestClusterWorker(object):
    def __init__(self, bot):
        self.bot = bot

    def work(self):
        forts = self.bot.get_forts()
        radius = 100



def find_biggest_cluster(radius, points):
    graph = nx.Graph()
    for fort in points:
            merc = coord2merc(fort['latitude'], fort['longitude'])
            graph.add_node(merc)
            for node in graph.nodes():
                if node != merc and np.linalg.norm(np.array(merc) - np.array(node)) <= radius*2:
                    graph.add_edge(merc, node)

    max_clique = max(list(find_cliques(graph)), key=len)
    clique_x, clique_y = zip(*max_clique)
    best_point = np.mean(clique_x), np.mean(clique_y)
    return merc2coord(best_point)