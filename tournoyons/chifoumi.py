# -*- coding: utf-8 -*-

from random import randint

from killer import Killer


class ChifoumiKiller(Killer):
    def __init__(self, args):
        self.referee = args.get("Referee")
        self.moveId = args.get("MoveId")
        self.game = args.get("Game")

    def render(self):
        if self.referee is not None:
            self.sendResponse(self.referee, {"MoveId": self.moveId, "Game": self.game, "Value": randint(1, 3)})
        return "Chifoumi"
