var request = require("request");
var Q = require("q");

var Answer = function(query) {
  this.MoveId = query.MoveId;
  this.Game = query.Game;
  this.Referee = query.Referee;
}

Answer.prototype.send = function(value) {
  var d = Q.defer();
  if (this.Referee) {
    request
      .get({
        url: this.Referee,
        qs: {
          MoveId: this.MoveId,
          Game: this.Game,
          Value: value
        }
      })
      .on("error", d.reject)
      .on("response", d.resolve);
  } else {
    setImmediate(function() {
      d.reject(new Error("No referee"));
    });
  }
  return d.promise;
};

module.exports = Answer;
