#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

from twisted.web.resource import Resource
from twisted.web.server import Site
from twisted.web.static import File
from twisted.internet import reactor
from twisted.web.client import Agent

from chifoumi import ChifoumiKiller
from tictactoe import TictactoeKiller


if __name__ == "__main__":
    r = Resource()
    agent = Agent(reactor)
    for path, obj in [
            ('tictactoe', TictactoeKiller),
            ('chifoumi', ChifoumiKiller)]:
        r.putChild(path, obj(agent))
    r.putChild('static', File('./static'))
    reactor.listenTCP(8000, Site(r))
    print "Serving on port 8000"
    reactor.run()
