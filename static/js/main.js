$(document).ready(function(){
		$('#make').chosen();
		$('#model').chosen();

	var scheduleAppointmentAvailable = false;

	$.getJSON('/static/json/cars.json', function(data){
		for(var i = 0; i < data.length; i++){
			$('#make').append('<option data-number='+i+
				' value='+data[i].title+
				'>'+data[i].title+'</option>').trigger('liszt:updated');
		}
	});
//==============================================================
	$('#make').on('change', function(){
		self = this;
		var selected = $(self).find('option:selected');
		var make = selected.data('number');
		dbMake = selected.val();

		$.getJSON('/static/json/cars.json', function(data){
			$('#model').empty();
			for(var k = 0; k < data[make].models.length; k++){
				$('#model')
					.append('<option value="'+data[make].models[k].title+'">'+data[make].models[k].title+'</option>')
					.val('')
					.trigger('liszt:updated')
			}
		});
	});
//==============================================================
	$('#btnQuote').on('click', function(){
		if($('#year').val() != ''){
			if(scheduleAppointmentAvailable == false){
				var randQuote = Math.floor(Math.random() * (800 - 200 + 1)) + 200;
				$('#quoteDisplay').html(randQuote+'.00');
				$('#quoteHidden').val(randQuote+'.00');
				scheduleAppointmentAvailable = true;
				$("#scheduleAppointment").removeClass('secondary').addClass('success');
			}
		}
	});
//==============================================================
	$('#scheduleAppointment').on('click',function(e){
		if(scheduleAppointmentAvailable == false){
			e.stopPropagation();
			e.preventDefault();
		}
	});

	$('#finalCheck').on('click', function(){
		$('#dbCheckMake').html($('[name=make]').val());
		$('#dbCheckModel').html($('[name=model]').val());
		$('#dbCheckYear').html($('[name=year]').val());
		$('#dbCheckServiceType').html($('[name=serviceType]').val());
		$('#dbCheckLocation').html($('[name=location]').val());
		$('#dbCheckName').html($('[name=name]').val());
		$('#dbCheckEmail').html($('[name=email]').val());
		$('#dbCheckPhone').html($('[name=phone]').val());
		$('#dbCheckContactMethod').html($('[name=contactMethod]').val());
		$('#dbCheckAppointmentTime').html($('[name=appointmentTime]').val());
	});
//==============================================================
	var currentOpenField;
		$('.buttonHiddenInfo').on('click', function(){
			if(currentOpenField != $(this).attr('id')){
				$(".hiddenInfo").slideUp();
			}
			currentOpenField = $(this).attr('id');
			$("#"+currentOpenField+"info").slideToggle();
		});

	
});