function myfunction(){
	var jsonstuff = document.getElementById("jsondata");
	//jsonstuff = '{"devices":{"device":"172.16.40.1","neighbors":[{"device_ip":"172.16.10.1","device_name":"AK1-4507","local_if":"No info","remote_if":"GigabitEthernet1/1"},{"device_ip":"172.16.10.1","device_name":"AK1-4507","local_if":"No info","remote_if":"GigabitEthernet1/2"},{"device_ip":"172.16.40.10","device_name":"sw-za2-010","local_if":"No info","remote_if":"FastEthernet0/25"},{"device_ip":"172.16.40.11","device_name":"sw-za2-011","local_if":"No info","remote_if":"FastEthernet0/25"}]}}';
	//console.log(jsonstuff.innerHTML.trim());

	var jsondata = JSON.parse(jsonstuff.innerHTML.trim());
	//console.log(jsondata);

	var ww = $(window).width(), hh = $(window).height();
	//console.log("Window width is ", ww, hh);

	var devmap = d3.select("#devmap").
       append("svg:svg").
       attr("width", ww).
       attr("height", hh);

/*
	devmap.append("svg:rect").
       attr("x", 100).
       attr("y", 100).
       attr("height", 100).
  	   attr("width", 800);
*/

	
};

$(document).ready(myfunction);

/*
devmap.append("svg:rect").
  attr("x", 100).
  attr("y", 100).
  attr("height", 100).
  attr("width", 200);
 */