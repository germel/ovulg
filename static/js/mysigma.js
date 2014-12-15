function makeGraph(){
	//var devs = loadData();
	//console.log(devs);
	sigma.parsers.json("devs", {container: 'sigma-container', settings: {defaultNodeColor: '#ec5148'}});
}

$(document).ready(makeGraph);
