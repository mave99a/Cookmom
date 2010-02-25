$(document).ready(function() {
	$('a.ajax_action').click(function() {
			var button = $(this)
			$.getJSON($(this).attr('href'), 
					  function(data) {
					  	if (data.success) {
					  		button.hide()
					  	}
					  	else {
					  		// failed
					  	}
					  })
			return false;
		});
})