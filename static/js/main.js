$(document).ready(function(){
	$.getJSON('/static/json/cars.json', function(data){
		for(var i = 0; i < data.length; i++){
			$("#make").append('<option data-number='+i+' value='+data[i].title+'>'+data[i].title+'</option>');
		}
	});
	$("#make").live("change", function(){
		self = this;
		var selected = $(self).find('option:selected');
		var make = selected.data('number');
		
		$.getJSON('/static/json/cars.json', function(data){
			$("#model").empty().append('<option>select model</option>');
			for(var k = 0; k < data[make].models.length; k++){
				$("#model").append('<option value="'+data[make].models[k].title+'">'+data[make].models[k].title+'</option>');
			}
		});
	});
});