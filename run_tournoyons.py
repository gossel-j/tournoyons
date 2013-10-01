#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

from twisted.web.wsgi import WSGIResource
from twisted.web.server import Site
from twisted.internet import reactor

from tournoyons import app


if __name__ == "__main__":
    siteresource = WSGIResource(reactor, reactor.getThreadPool(), app)
    sitefactory = Site(siteresource)
    reactor.listenTCP(8000, sitefactory)
    reactor.run()
