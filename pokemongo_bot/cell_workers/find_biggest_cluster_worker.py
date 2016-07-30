from utils import coord2merc
from nearpy import Engine
from nearpy.distances import EuclideanDistance
from nearpy.filters import DistanceThresholdFilter

from nearpy.hashes import RandomBinaryProjections, HashPermutationMapper


class FindBiggestClusterWorker(object):
    def __init__(self, bot):
        self.bot = bot

    def work(self):
        permutations = HashPermutationMapper('permut')
        rbp_perm = RandomBinaryProjections('rbp_perm', 14)
        # rbp_conf = {'num_permutation':25,'beam_size':5,'num_neighbour':50}
        permutations.add_child_hash(rbp_perm)

        engine_perm = Engine(2, lshashes=[permutations], distance=EuclideanDistance(),
                         vector_filters=[DistanceThresholdFilter(10)])
        forts = self.bot.get_forts()

        for fort in forts:
            engine_perm.store_vector(coord2merc(fort['latitude'], fort['longitude']), fort['id'])
        