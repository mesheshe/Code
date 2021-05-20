var mysql = require('mysql');
var creden = require('./credentials.js')
var pool = mysql.createPool({
    connectionLimit: 10,
    host: 'localhost',
    user : 'root',
    password: creden.mysqlpw,
    database: 'dcb',
    port: '3306',
    debug: false
})

module.exports.pool = pool;