var express = require('express');
var bodyParser = require('body-parser');
var handlebars = require('express-handlebars').create({defaultLayout:'main'});
var mysql = require('./pool.js');

var app = express();

app.engine('handlebars', handlebars.engine);
app.set('port', 9794);
app.set('view engine', 'handlebars');
app.use(bodyParser.urlencoded({extended:false}));
app.use(bodyParser.json());
app.use(express.static('public'));

mysql.pool.getConnection(function(error){
    if (error){
        console.log(error);
    }else{
        console.log("connecting");
        mysql.pool.query("CREATE TABLE IF NOT EXISTS weightTracker(id INT PRIMARY KEY AUTO_INCREMENT, name VARCHAR(255) NOT NULL, reps INT, weight INT, date DATE, lbs BOOLEAN)", function(err){
            if (err){
                console.log(err);
            }else{
                console.log("connected");
            }
        })
    }
});
// Need to implement a clear table function
app.get('/', function(req,res, next){
    if (req.query.clear == "true"){
        mysql.pool.query("DELETE FROM weightTracker", function(err,rows,fields){
            if (err){
                next(err);
            }else{
                var context = {};
                context.clear = "true";
                res.send(JSON.stringify(JSON.stringify(context)));
            }
        });
        return;
    }
    res.render('body');
});

app.get('/update', function(req, res){
    res.redirect('/');
})

app.post('/update', function(req,res){
    mysql.pool.query("SELECT * FROM weightTracker WHERE id=?", [req.body.id], function(err1,rows,fields){
        if (err1){
            next(err1);
            return;
        }else{
            var context = {};
            context.results = JSON.parse(JSON.stringify(rows));
            var date = context.results[0].date;
            if (date != null){
                date = date.substring(0,date.indexOf("T"));
            }
            context.results[0].date = date;
            res.render('update', context);
        }
    })
});

app.post('/', function(req, res, next){
    if (req.body.content == "add"){
        if (req.body.name == ''){
            res.send(JSON.stringify({"results":"null"}));
            return;       
        }else{
            mysql.pool.query("INSERT INTO weightTracker (name, reps, weight, date, lbs) VALUES (?,?,?,?,?)", 
            [req.body.name, req.body.reps || null, req.body.weight || null, req.body.date || null, req.body.unit], function(err, result){
                if (err){
                    next(err);
                    return;
                }else{
                    mysql.pool.query("SELECT * FROM weightTracker where id =" + result.insertId, function(err1, rows, fields){
                        if (err1){
                            next(err1);
                            return;
                        }else{
                            var context = {};
                            context.results = JSON.stringify(rows[0]);
                            res.send(JSON.stringify(context));
                        }
                    });
                }
            });
        }
    }
    if (req.body.content == "loadItAll"){
        mysql.pool.query("SELECT * FROM weightTracker", function(err1, rows, fields){
            if (err1){
                next(err1);
                return;
            }else{
                var context = {};
                context.results = JSON.stringify(rows);
                res.send(JSON.stringify(context));
            }
        });
    }
    if (req.body.content == "delete"){
        mysql.pool.query("DELETE FROM weightTracker WHERE id=?", [req.body.id], function(err1){
            if (err1){
                next(err1);
                return;
            }else{
                var context = {};
                context.results = {'delete':'true'};
                res.send(JSON.stringify(context));
            }
        });
    }
    if (req.body.content == 'update' && req.body.name != ''){
        mysql.pool.query("UPDATE weightTracker SET name=?,reps=?,weight=?,date=?,lbs=? WHERE id=?", 
        [req.body.name, req.body.reps || null, req.body.weight || null, req.body.date || null, req.body.unit, req.body.id], function(err1){
            if (err1){
                next(err1);
                return;
            }else{
                var context = {};
                context.results = {'update':'true'};
                res.send(JSON.stringify(context));
            }
        });
    }
});

app.use(function(req, res){
    res.status(404);
    res.render('404');
});

app.use(function(error,req,res,next){
    console.error(error.stack);
    res.status(500);
    res.render('505');
});

app.listen(app.get('port'), function(){
    console.log('Express started on http://localhost:' + app.get('port') + '; press Ctrl-C to terminate.');
});


