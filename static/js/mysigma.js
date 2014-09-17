function loadData(){
	var jsonstuff = document.getElementById("jsondata").textContent;
	var jsonstuff1 = document.getElementById("jsondata").textContent;
	//console.log(jsonstuff);
	return jsonstuff;
	
}

function makeGraph(){
	//var devs = loadData();
	//console.log(devs);
	sigma.parsers.json("devs", {container: 'sigma-container'});
	
}

$(document).ready(makeGraph);
