var express = require('express');
var bodyParser = require('body-parser');
var handlebars = require('express-handlebars').create({defaultLayout:'main'});
var session = require('express-session');
var mysql = require('./pool.js')

var app = express();

app.engine('handlebars',handlebars.engine);
app.set('port', 9794);
app.set('view engine','handlebars'); 
app.use(session({secret:'SuperSecretPassword'}));
app.use(bodyParser.urlencoded({extended:false}));
app.use(bodyParser.json());
app.use(express.static('public'));

mysql.pool.getConnection(function(error){
  if (error){
    console.log(error);
  }else{
    console.log("connected to mysql")
    mysql.pool.query('CREATE TABLE IF NOT EXISTS commentData(id INT AUTO_INCREMENT, name VARCHAR(20), content TEXT, postedAt DATE, PRIMARY KEY (id))', function(err, rows){
      if (err){
        console.log(err)
        throw err
      }else{
        console.log("Database is primed");
      }
    });
  }
});

app.get('/', function(req,res){
  if (!req.session.pageVisit){
    req.session.pageVisit = [{name:"Example 1",visit:0}, {name:"Example 2",visit:0}, {name:"Example 3",visit:0},{name:"Example 4",visit:0}];
  }
  req.session.pageVisit[0].visit += 1;
  res.render("homepage");
});

app.get('/second-page', function(req,res){
  if (!req.session.pageVisit){
    req.session.pageVisit = [{name:"Example 1",visit:0}, {name:"Example 2",visit:0}, {name:"Example 3",visit:0},{name:"Example 4",visit:0}];
  }
  req.session.pageVisit[1].visit += 1;
  res.render("secondpage");
});

app.get('/third-page', function(req,res,next){
  var context = {};
  mysql.pool.query('SELECT * FROM commentData', function(err, rows, fields){
    if (err){
      next(err);
      return;
    }else{
      var arr = [];
      Array.from(rows).forEach( function (x){
        var obj = JSON.parse(JSON.stringify(x));
        arr.unshift(obj);  // in order to have the most recent comments on top
      })
      context.comment = arr
      if (!req.session.pageVisit){
        req.session.pageVisit = [{name:"Example 1",visit:0}, {name:"Example 2",visit:0}, {name:"Example 3",visit:0},{name:"Example 4",visit:0}];
      }
      req.session.pageVisit[2].visit += 1;
      res.render("thirdpage", context)
    }
  })
});

app.post('/third-page', function(req,res,next){
  var context = req.body;
  var date =  new Date();
  var dat = date.getFullYear() +"-"+`${date.getMonth() + 1}`+"-"+date.getDate();
  //var index = dat.indexOf('T');
  //dat = dat.slice(0,index + 1);
  //console.log(dat);
  //include name if time 
  mysql.pool.query("INSERT INTO commentData (`name`, `content`, `postedAt`) VALUES (?,?,?)", [context.name || "Anon", context.comment || "I <3 Space.", dat],
   function(error, result){
     if (error){
       next(error);
     }else{ 
      res.send(JSON.stringify(req.body));  
     }
   }); 
});

app.get('/fourth-page', function(req,res){
  context = {};
  if (!req.session.pageVisit){
    req.session.pageVisit = [{name:"Example 1",visit:0}, {name:"Example 2",visit:0}, {name:"Example 3",visit:0},{name:"Example 4",visit:0}];
  }
  req.session.pageVisit[3].visit += 1;
  context.pageVisit = req.session.pageVisit;
  res.render("fourthpage", context);
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