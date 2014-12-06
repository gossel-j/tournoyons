var Answer = require("./answer");

function handler(req, res, next) {
  var answer = new Answer(req.query);
  answer.send(Math.floor(Math.random() * 3) + 1);
  res.end("Chifoumi");
}

module.exports = handler;
