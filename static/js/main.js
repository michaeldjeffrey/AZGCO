$(document).ready(function(){
	$.getJSON('/static/json/cars.json', function(data){
		for(var i = 0; i < data.length; i++){
			$("#make").append('<option value='+i+'>'+data[i].title+'</option>');
		}
	});
	$("#make").live("change", function(){
		self = this;
		
		$.getJSON('/static/json/cars.json', function(data){
			$("#model").empty().append('<option>select model</option>');
			for(var k = 0; k < data[self.value].models.length; k++){
				$("#model").append('<option value='+data[self.value].models[k].title+'>'+data[self.value].models[k].title+'</option>');
			}
		});
	});
});