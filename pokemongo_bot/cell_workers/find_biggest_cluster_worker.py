from utils import coord2merc, merc2coord
from networkx.algorithms.clique import find_cliques

import networkx as nx
import numpy as np


class FindBiggestClusterWorker(object):
    def __init__(self, bot):
        self.bot = bot

    def work(self):
        forts = self.bot.get_forts()
        G = nx.Graph()
        r = 100
        test = []

        for fort in forts:
            merc = coord2merc(fort['latitude'], fort['longitude'])
            test.append(((fort['latitude'], fort['longitude']), merc2coord(merc)))
            G.add_node(merc)
            for node in G.nodes():
                if node != merc and np.linalg.norm(np.array(merc) - np.array(node)) <= r*2:
                    G.add_edge(merc, node)

        max_clique = max(list(find_cliques(G)), key=len)
        clique_x, clique_y = zip(*max_clique)
        best_point = np.mean(clique_x, clique_y)

        merc2coord(best_point)