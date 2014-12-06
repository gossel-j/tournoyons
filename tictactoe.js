var _ = require("underscore");
var Answer = require("./answer");

var winPos = [
  [0, 1, 2],
  [3, 4, 5],
  [6, 7, 8],
  [0, 3, 6],
  [1, 4, 7],
  [2, 5, 8],
  [0, 4, 8],
  [2, 4, 6]
];

function nodeValue(map) {
  for (n in winPos) {
    var val = _.map(winPos[n], function(v) {return map[v]});
    if (_.isEqual(val, [1, 1, 1])) return Infinity;
    if (_.isEqual(val, [2, 2, 2])) return -Infinity;
  }
  return 0;
}

function getEmptyPos(map) {
  var pos = [];
  _.each(map, function(p, n) {
    if (p == 0) pos.push(n);
  });
  return pos;
}

function minimaxMe(node, emptyPos, test) {
  var val = nodeValue(node);
  if (emptyPos.length <= 0 || val != 0)
    return {val: val};
  var best = {val: -Infinity};
  for (var n = 0; n < emptyPos.length; n++) {
    var newTray = _.clone(node);
    var newEmptyPos = _.clone(emptyPos);
    var p = newEmptyPos.splice(n, 1)[0];
    newTray[p] = 1;
    var turn = minimaxOpp(newTray, newEmptyPos);
    if (test)
      console.log(turn);
    if (turn.val == Infinity)
      return {val: val, pos: p};
    if (turn.val > best.val)
      best = {val: val, pos: p};
  }
  return best;
}

function minimaxOpp(node, emptyPos) {
  var val = nodeValue(node);
  if (emptyPos.length <= 0 || val != 0)
    return {val: val};
  var best = {val: Infinity};
  for (var n = 0; n < emptyPos.length; n++) {
    var newTray = _.clone(node);
    var newEmptyPos = _.clone(emptyPos);
    var p = newEmptyPos.splice(n, 1)[0];
    newTray[p] = 2;
    var turn = minimaxMe(newTray, newEmptyPos);
    if (turn.val == -Infinity)
      return {val: val, pos: p};
    if (turn.val < best.val)
      best = {val: val, pos: p};
  }
  return best;
}

function handler(req, res, next) {
  var answer = new Answer(req.query);
  var tray = _.map(req.query.Tray, Number);
  var turn = Number(req.query.Turn);
  if (turn % 2 == 0) tray = _.map(tray, function(v) {return [0, 2, 1][v]});
  if (turn == 1) {
    answer.send(_.sample([1, 3, 7, 9]));
  } else {
    var ret = minimaxMe(tray, getEmptyPos(tray), true);
    console.log(ret);
    answer.send(ret.pos + 1);
  }
  res.end("TicTacToe");
}

module.exports = handler;
