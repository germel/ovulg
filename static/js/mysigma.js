function makeGraph(){
    //var devs = loadData();
    //console.log(devs);

    //s = new sigma({graph: 'devs', renderer: {type: 'canvas', container: 'sigma-container'} });
    s = new sigma({graph: 'devs', renderer: {type: 'canvas'} });
    sigma.parsers.json('devs', {container: 'sigma-container', settings: {defaultNodeColor: '#ec5148'}});
    var dragListener = sigma.plugins.dragNodes(s, s.renderers[0]);
    dragListener.bind('startdrag', function(event) {console.log(event);});
    dragListener.bind('drag', function(event) {console.log(event);});
    dragListener.bind('drop', function(event) {console.log(event);});
    dragListener.bind('dragend', function(event) {console.log(event);});
}

$(document).ready(makeGraph);
