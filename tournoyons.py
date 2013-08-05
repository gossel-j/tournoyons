#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

from twisted.web.server import Site
from twisted.web.static import File
from twisted.internet import reactor
from twisted.web.script import ResourceScript


class Renderer(File):
    processors = {'.rpy': ResourceScript}


class MySite(Site):
    displayTracebacks = False


if __name__ == "__main__":
    r = Renderer('./scripts/', ignoredExts=('.rpy',))
    r.putChild('static', File('./static'))
    reactor.listenTCP(8000, MySite(r))
    print "Serving on port 8000"
    reactor.run()
