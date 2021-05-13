var express = require('express');

var app = express();
var handlebars = require('express-handlebars').create({defaultLayout:'main'});
var bodyParser = require('body-parser');

app.set('port', 9794);
app.engine('handlebars', handlebars.engine);
app.set('view engine', 'handlebars');
app.set('views','./D/views');
app.use(bodyParser.urlencoded({extended:false}));
app.use(bodyParser.json());

app.get('/',function(req,res){
  var ret = {}
  var arr = [];
  for(var p in req.query){
    arr.push({'name':p,'value':req.query[p]});
  }
  ret.data = arr;
  res.render('data-get',ret);
});

app.post('/',function(req,res){
  var ret = {};
  var arr = [];
  var arr2 = [];
  for(var p in req.body){
    arr.push({'name':p,'value':req.body[p]});
  }
  if (req.query != null){
    for (var q in req.query){
      arr2.push({'name':q,'value':req.query[q]});
    }
  }
  ret.dataBody = arr;
  ret.dataQuery = arr2;
  res.render('data-post',ret);
});

app.use(function(req, res){
  res.status(404);
  res.render('404');
});

app.use(function(error,req,res,next){
  console.error(error.stack);
  res.status(500);
  res.render('500');
});

app.listen(app.get('port'),function(){
  console.log('Express started on http://localhost:' + app.get('port') + '; press Ctrl-C to terminate.');
});
