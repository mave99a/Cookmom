/*
*  Initialize
*/
$(document).ready(function() {
  if (typeof(_JS_MODULE_TAG) != 'undefined') {
  	$('a.tag span.remove').click(function() {
  				$(this).parent().addClass('deletedtag').removeClass('tag').blur();
  				$.get($(this).attr('href'));
				return false; // cancel event 
	})
   	$('a.tag span.undo').click(function() {
  				$(this).parent().addClass('tag').removeClass('deletedtag').blur();
  				$.get($(this).attr('href'));
				return false; // cancel event 
	}) 		
	
	$('.tags form').ajaxForm({
			dataType:  'json', 
			success: function(data) {
			  $.each(data, function(i, tag) {
			  			
			  	})
			}
		}
	)		   
  }
});

