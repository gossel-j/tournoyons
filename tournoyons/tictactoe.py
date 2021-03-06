# -*- coding: utf-8 -*-

from random import choice as rchoice

from killer import Killer


class TictactoeKiller(Killer):
    winPos = [
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6)
    ]

    def __init__(self, args):
        self.referee = args.get("Referee")
        self.moveId = args.get("MoveId")
        self.game = args.get("Game")
        self.tray = map(int, args.get("Tray", []))
        self.turn = int(args.get("Turn", 0))
        self.me = 1 if self.turn % 2 else 2
        self.opp = 2 if self.turn % 2 else 1

    def respond(self, pos):
        if self.referee is not None:
            self.sendResponse(self.referee, {"MoveId": self.moveId, "Game": self.game, "Value": pos + 1})

    def tryComplete(self, me, tray):
        r = []
        for pos in self.winPos:
            c = 0
            s = -1
            for n in pos:
                if tray[n] == 0:
                    s = n
                elif tray[n] == me:
                    c += 1
            if c == 2 and s != -1:
                r.append(s)
        return r

    def tryWin(self):
        r = self.tryComplete(self.me, self.tray)
        if r:
            print "##### WIN #####"
            self.respond(rchoice(r))
            return True
        return False

    def tryBlock(self):
        r = self.tryComplete(self.opp, self.tray)
        if r:
            print "##### BLOCK #####"
            self.respond(rchoice(r))
            return True
        return False

    def testFork(self, me, otray):
        t = []
        for n, v in enumerate(otray):
            if v == 0:
                tray = otray[:]
                tray[n] = me
                r = self.tryComplete(me, tray)
                if len(r) >= 2:
                    t.append(n)
        return t

    def tryFork(self):
        r = self.testFork(self.me, self.tray)
        if r:
            print "##### FORK #####"
            self.respond(rchoice(r))
            return True
        return False

    def tryBlockFork(self):
        tmp = self.testFork(self.opp, self.tray)
        if len(tmp) == 0:
            return False
        if len(tmp) == 1:
            print "##### BLOCK FORK 1 #####"
            self.respond(tmp[0])
            return True
        g = []
        for n, v in enumerate(self.tray):
            if v == 0:
                tray = self.tray[:]
                tray[n] = self.me
                r = self.tryComplete(self.me, tray)
                if r:
                    l = self.testFork(self.opp, tray)
                    if l and r[0] not in l:
                        g.append(n)
        if g:
            print "##### BLOCK FORK 2 #####"
            self.respond(rchoice(g))
            return True
        return False

    def firstTurn(self):
        if self.turn == 1:
            print "##### FIRST TURN #####"
            self.respond(rchoice([0, 2, 6, 8]))
            return True
        return False

    def specialThirdTurn(self):
        if self.turn == 3:
            opp_case = self.tray.index(self.opp)
            my_case = self.tray.index(self.me)
            if opp_case == 4:
                for m, pos in [
                        (0, 8),
                        (2, 6),
                        (6, 2),
                        (8, 0)]:
                    if my_case == m:
                        print "##### THIRD TURN 1 #####"
                        self.respond(pos)
                        return True
            elif opp_case in (0, 2, 6, 8):
                pos = [0, 2, 6, 8]
                pos.remove(opp_case)
                pos.remove(my_case)
                print "##### THIRD TURN 2 #####"
                self.respond(rchoice(pos))
                return True
        return False

    def center(self):
        if self.tray[4] == 0:
            print "##### CENTER #####"
            self.respond(4)
            return True
        return False

    def oppositeCorner(self):
        r = []
        corners = [
            (0, 8),
            (2, 6),
            (8, 0),
            (6, 2)
        ]
        for a, b in corners:
            if self.tray[a] == self.opp and self.tray[b] == 0:
                r.append(b)
        if r:
            print "##### OPPOSITE CORNER #####"
            self.respond(rchoice(r))
            return True
        return False

    def emptyCorner(self):
        r = []
        corners = [0, 2, 8, 6]
        for n in corners:
            if self.tray[n] == 0:
                r.append(n)
        if r:
            print "##### CORNER #####"
            self.respond(rchoice(r))
            return True
        return False

    def emptySide(self):
        r = []
        sides = [1, 5, 7, 3]
        for n in sides:
            if self.tray[n] == 0:
                r.append(n)
        if r:
            print "##### SIDE #####"
            self.respond(rchoice(r))
            return True
        return False

    def __call__(self):
        actions = [
            self.tryWin,
            self.tryBlock,
            self.tryFork,
            self.tryBlockFork,
            self.firstTurn,
            self.specialThirdTurn,
            self.center,
            self.oppositeCorner,
            self.emptyCorner,
            self.emptySide
        ]
        if self.referee is not None:
            for action in actions:
                if action():
                    return "TicTacToe"
        return "NoTicTacToe"
