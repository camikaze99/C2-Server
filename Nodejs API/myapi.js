var http = require('http');
var express = require('express');
var os = require('os');

var app = express();

var inputs = [	{ pin: '11', gpio: '17', value: 1},
				{ pin: '12', gpio: '18', value: 0},
				{ arch: '%s'}]

	var architecture = os.arch;

	console.log('- CPU Architecture: ' + os.arch());
	console.log('- Total Memory: ' + os.totalmem());
	console.log('- Operating system name: ' + os.type());
	console.log('- Operating system platform: ' + os.platform()); 
	console.log('- OS Release: ' + os.release());


app.use(express['static'](__dirname));

//Express route for incoming requests for a customer name
app.get('/inputs/:id', function(req, res) {
	res.status(200).send(inputs[req.params.id]);
});

//Express route for any other unrecognized incoming requests
app.get('*', function(req, res) {
	res.status(404).send('Unrecognized API call');
});

//Express route to handle errors
app.use(function(err, req, res, next) {
	if (req.xhr) {
		res.status(500).send('Oops, Something went wrong!');
} else{
	next(err);
}
});

app.listen(3000);
console.log('App Server running at port 3000');
