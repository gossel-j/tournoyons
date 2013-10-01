# -*- coding: utf-8 -*-

from urllib import urlencode

from twisted.internet import reactor
from twisted.web.client import Agent


class Killer(object):
    _agent = Agent(reactor)

    def sendResponse(self, referee, data={}):
        return self._agent.request("%s?%s" % (referee, urlencode(data)))
