function makeGraph(){
	//var dev = loadData();
	//console.log(dev);
	sigma.parsers.json("devs", {container: 'sigma-container'});
}

$(document).ready(makeGraph);
