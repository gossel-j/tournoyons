# -*- coding: utf-8 -*-

from random import randint

import requests


class ChifoumiKiller(object):
    def __init__(self, args):
        self.game = args.get("Game")
        self.moveId = args.get("MoveId")
        self.referee = args.get("Referee")

    def run(self):
        if self.referee is not None:
            requests.get(self.referee, params={
                "MoveId": self.moveId,
                "Game": self.game,
                "Value": randint(1, 3)
            })
        return "Chifoumi"
