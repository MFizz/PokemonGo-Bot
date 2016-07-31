from pokemongo_bot.step_walker import StepWalker
from pokemongo_bot.cell_workers import FindBiggestCluster


class PointNavigator(object):
    def __init__(self, bot):
        self.bot = bot
        self.is_at_destination = False

    def take_step(self):
        print (str(self.bot.position))
        worker = [x for x in self.bot.workers if type(x) == FindBiggestCluster][0]
        dest = worker.dest
        if dest is not None:
            lat = dest['latitude']
            lng = dest['longitude']
            print(str(dest))
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


