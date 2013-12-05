# -*- coding: utf-8 -*-

import requests


class Killer(object):
    _session = requests.Session()

    def sendResponse(self, referee, data={}):
        return self._session.get(referee, params=data)
