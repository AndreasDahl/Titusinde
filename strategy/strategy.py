__author__ = 'Andreas Dahl'


class Strategy(object):
    """
    Interface for a titusinde strategy
    """

    # noinspection PyMethodMayBeStatic
    def handle_roll(self, game_round):
        raise NotImplemented