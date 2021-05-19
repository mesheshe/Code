var express = require('express');
var bodyParser = require('body-parser');
var handlebars = require('express-handlebars').create({defaultLayout:'main'});
var session = require('express-session');
var request = require('request');

//http://api.openweathermap.org/data/2.5/weather?q=${cityInput.value},${stateInput.value},us&units=metric,&appid=${apiKey}
var apiKey = 'fa7d80c48643dfadde2cced1b1be6ca1';
var app = express();

app.engine('handlebars',handlebars.engine);
app.set('port', 9794);
app.set('view engine','handlebars');
app.set('views','./D/views');
app.use(session({secret:'SuperSecretPassword'}));
app.use(bodyParser.urlencoded({extended:false}));
app.use(bodyParser.json());
app.use(express.static('D/supportingFiles'));

app.get('/', function(req,res){
  res.render('home');
});

app.get('/other-page', function(req,res){
  res.render('other-page');
});

app.get('/weather', function(req, res, next){
  var context = {};
  request(`http://api.openweathermap.org/data/2.5/weather?q=Seattle,WA,us&units=metric,&appid=${apiKey}`, function (error, response, body){
    if (!error && response.statusCode < 400){
      context.data1 = body;
      var payload = {c:"a", d:"c", e:"f"};
      var send = {"url":"http://flip3.engr.oregonstate.edu:9794/?candy=Hershey", "method": "POST", "headers": {"Content-Type": "application/JSON"}, "body":JSON.stringify(payload)};
      request(send, function(error, response, body){
        if (!error && response.statusCode < 400){
          context.data2 = body;
          res.render('weather', context);
        }else{
          if (response){
            console.log(response.statusCode);
          }
          next(error);
        }
      });
    }else{
      console.log(error);
      if (response){
        console.log(response.statusCode);
      }
      next(error);
    }
  })  
})

app.get('/counter', function(req, res){
  var returnObj = {};
  returnObj.count = req.session.count || 0; // saves the previous session count 
  req.session.count = returnObj.count + 1; // increments it since you have visited 
  res.render('counter', returnObj);  // gives the previously saved session counter
});

app.post('/counter', function(req,res){
  var returnObj = {};
  if (req.body.content === "resetSess"){
    req.session.count = 0;
  }
  returnObj.count = req.session.count || 0;
  req.session.count = returnObj.count + 1;
  res.render('counter', returnObj);
})

function generate(){
  var rando = {};
  rando.random = Math.random();
  return rando;
}

app.get('/generate-random-number', function(req,res){
  res.render('generate-random-number', generate())
});

app.use(function(req,res){
  res.status(404);
  res.render('404');
});

app.use(function(error,req,res,next){
  console.error(error.stack);
  res.status(500);
  res.send('500');
});

app.listen(app.get('port'), function(){
  console.log('Express started on http://localhost:' + app.get('port') + '; press Ctrl-C to terminate.');
});


