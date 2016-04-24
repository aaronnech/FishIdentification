var Scraper = require ('images-scraper')
  , bing = new Scraper.Bing();

var args = process.argv.slice(2);

var num = parseInt(args[0]);
args.shift();
var searchTerm = args.join(' ');

bing.list({
	keyword: searchTerm,
	num: num,
	detail: true
})
.then(function (res) {
	console.log(res.map(function(x) { return x.url; }).join('\n'));
}).catch(function(err) {
	console.log('err',err);
})