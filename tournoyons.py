#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

from flask import Flask
app = Flask(__name__)
from flask import request

from chifoumi import ChifoumiKiller
from tictactoe import TictactoeKiller


@app.route("/chifoumi")
def chifoumi():
    killer = ChifoumiKiller(request.args)
    return killer.run()


@app.route("/tictactoe")
def tictactoe():
    killer = TictactoeKiller(request.args)
    return killer.run()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
