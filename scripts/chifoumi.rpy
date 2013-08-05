# -*- coding: utf-8 -*-

from random import randint
from urllib import urlencode

from twisted.web.client import Agent
from twisted.web.resource import Resource
from twisted.internet import reactor


class ChifoumiKiller(Resource):
    def render_GET(self, req):
        referee = req.args.get("Referee", [None])[0]
        moveId = req.args.get("MoveId", [None])[0]
        game = req.args.get("Game", [None])[0]
        if referee is not None:
            agent = Agent(reactor)
            agent.request('GET', '%s?%s' % (referee, urlencode({"MoveId": moveId, "Game": game, "Value": randint(1, 3)})))
        print "Chifoumi"
        return "Chifoumi"


resource = ChifoumiKiller()
