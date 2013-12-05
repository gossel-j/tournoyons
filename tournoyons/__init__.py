# -*- coding: utf-8 -*-

from flask import Flask, render_template, url_for, abort, request
app = Flask(__name__)

from tictactoe import TictactoeKiller
from chifoumi import ChifoumiKiller


@app.route('/')
def root():
    return render_template(
        'index.html',
        avatar_url=url_for('static', filename='avatar.png')
    )


@app.route('/<game>/')
def killer_page(game):
    killers = {
        'tictactoe': TictactoeKiller,
        'chifoumi': ChifoumiKiller
    }
    if game in killers:
        return killers[game](request.args)()
    else:
        abort(404)
