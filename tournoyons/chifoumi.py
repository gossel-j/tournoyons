# -*- coding: utf-8 -*-

from random import randint
from urllib import urlencode

from twisted.web.client import getPage


class ChifoumiKiller(object):
    def __init__(self, args):
        self.referee = args.get("Referee")
        self.moveId = args.get("MoveId")
        self.game = args.get("Game")

    def render(self):
        if self.referee is not None:
            getPage("%s?%s" % (self.referee, urlencode({"MoveId": self.moveId, "Game": self.game, "Value": randint(1, 3)})))
        return "Chifoumi"
