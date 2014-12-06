var path = require("path");
var express = require("express");
var morgan = require("morgan");
var bodyParser = require("body-parser");
var jade = require("jade");
var tictactoe = require("./tictactoe");
var chifoumi = require("./chifoumi");

var app = express();

app.engine('jade', jade.__express);
app.set("views", path.join(__dirname, "views"));

if (app.get("env") === 'development') {
  app.set("trust proxy");
  app.set("json spaces", 2);
  app.use(morgan("dev"));
} else {
  app.set("trust proxy", "loopback");
  app.use(morgan("combined"));
}

app.use(require("compression")());
app.use(bodyParser.urlencoded({extended: true}));
app.use(bodyParser.json());

app.use("/static/", express.static(path.join(__dirname, "static")));

app.get("/", function(req, res, next) {
  res.render("index.jade", function(err, html) {
    if (err) return next(err);
    res.end(html);
  });
});

app.get("/tictactoe", tictactoe);
app.get("/chifoumi", chifoumi);

if (app.get("env") === 'development') {
  app.use(require("errorhandler")());
}

app.listen(3000, function() {
  console.log("Server is listening on port 3000");
});
