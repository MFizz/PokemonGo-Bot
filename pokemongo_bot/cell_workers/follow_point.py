from pokemongo_bot.step_walker import StepWalker
from pokemongo_bot.cell_workers import find_biggest_cluster


class FollowPoint(object):
    def __init__(self, bot):
        self.bot = bot
        self.is_at_destination = False
        self.dest = None

    def work(self):
        worker = [x for x in self.bot.workers if type(x) == find_biggest_cluster.FindBiggestCluster][0]

        if worker.dest is not None:
            self.dest = worker.dest
        print (str(self.bot.position))
        print(str(self.dest))
        if self.dest is not None:

            lat = self.dest['latitude']
            lng = self.dest['longitude']
            print (str(self.bot.position))

            if not self.is_at_destination:

                if self.bot.config.walk > 0:
                    step_walker = StepWalker(
                        self.bot,
                        self.bot.config.walk,
                        lat,
                        lng
                    )

                    is_at_destination = False
                    if step_walker.step():
                        is_at_destination = True

                else:
                    self.bot.api.set_position(lat, lng)
        else:
            lat = self.bot.position[0]
            lng = self.bot.position[1]

        return [lat, lng]


