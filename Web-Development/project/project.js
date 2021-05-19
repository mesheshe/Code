var express = require('express');
var bodyParser = require('body-parser');
var handlebars = require('express-handlebars').create({defaultLayout:'main'});
var session = require('express-session');
var request = require('request');
const { response } = require('express');

var app = express();

app.engine('handlebars',handlebars.engine);
app.set('port', 9794);
app.set('view engine','handlebars'); 
app.use(session({secret:'SuperSecretPassword'}));
app.use(bodyParser.urlencoded({extended:false}));
app.use(bodyParser.json());
app.use(express.static('public'));

app.get('/', function(req,res){
  if (req.query != null && req.query.page == "second-page"){
    res.render("secondpage");
  }else{
    res.render("homepage");
  }
  req.query.page = null;
});

app.get('/second-page', function(req,res){
  res.render("secondpage");
  req.query.page = null;
});

app.get('/third-page', function(req,res){
  res.render("secondpage");
  req.query.page = null;
});
app.get('/fourth-page', function(req,res){
  res.render("secondpage");
  req.query.page = null;
});

app.use(function(req,res){
    res.status(404);
    res.render('404');
  });
  
  app.use(function(error,req,res,next){
    console.error(error.stack);
    res.status(500);
    res.render('500');
  });
  
  app.listen(app.get('port'), function(){
    console.log('Express started on http://localhost:' + app.get('port') + '; press Ctrl-C to terminate.');
  });