# -*- coding: utf-8 -*-

from random import randint
from urllib import urlencode

from twisted.web.resource import Resource


class ChifoumiKiller(Resource):
    isLeaf = True

    def __init__(self, agent):
        self.agent = agent

    def render_GET(self, req):
        referee = req.args.get("Referee", [None])[0]
        moveId = req.args.get("MoveId", [None])[0]
        game = req.args.get("Game", [None])[0]
        if referee is not None:
            self.agent.request('GET', '%s?%s' % (referee, urlencode({"MoveId": moveId, "Game": game, "Value": randint(1, 3)})))
        print "Chifoumi"
        return "Chifoumi"
