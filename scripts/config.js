var hum_limits = [0, 100]
var temp_limits = [18, 25]
var light_limits = [0, 1200]

class Config{ 
	constructor(hum,temp,light){
		this.hum = hum;
		this.temp= temp;
		this.light = light;
	}
}

var radish = new Config(70, 18, 1000);
var bean = new Config(70, 22, 1200);
var paprica = new Config(50, 20, 1200);

const url = "config.php";

var TempJson;
function presetHandler(name){
	
 /*switch(name){
	 case 'radish': TempJson = JSON.stringify(radish); break;
	 case 'bean': TempJson = JSON.stringify(bean); break;
	 case 'paprica': TempJson = JSON.stringify(paprica); break;
 }*/
 document.getElementById('hum').value =name.hum;
 document.getElementById('temp').value =name.temp;
 document.getElementById('light').value =name.light;
 TempJson = JSON.stringify(name);
 sendData(url, TempJson);
}
function saveHandler(){
	
	let temp_hum = parseInt(document.getElementById('hum').value);
	if(temp_hum > hum_limits[1]) {temp_hum = hum_limits[1];}
	else if(temp_hum<hum_limits[0]) {temp_hum=hum_limits[0];}
	
	let temp_temp = parseInt(document.getElementById('temp').value);
	if(temp_temp > temp_limits[1]) {temp_temp = temp_limits[1];}
	else if(temp_temp<temp_limits[0]) {temp_temp=temp_limits[0];}
	
	let temp_light = parseInt(document.getElementById('light').value);
	if(temp_light > light_limits[1]) {temp_light = light_limits[1];}
	else if(temp_light<light_limits[0]) {temp_light=light_limits[0];}
	
	temp = new Config(temp_hum, temp_temp,temp_light);
	
	TempJson = JSON.stringify(temp);
 sendData(url, TempJson);
}

function sendData(rurl, rdata){
	$.ajax({
		url: rurl,
		data: {data : rdata},
		type: 'POST',
		dataType: 'text/json',
		success: function(response){console.log(response);},
		failure: function(response){console.log(response);}
		});
	
	
}
