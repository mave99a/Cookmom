/*
*  Initialize
*/
$(document).ready(function() {
  if (typeof(_JS_MODULE_TAG) != 'undefined') {
  	$('a.tag span.remove').click(function() {
  				$(this).parent().addClass('deletedtag').removeClass('tag');
  				$.get($(this).attr('href'));
				return false; // cancel event 
			})
   	$('a.tag span.undo').click(function() {
  				$(this).parent().addClass('tag').removeClass('deletedtag');
  				$.get($(this).attr('href'));
				return false; // cancel event 
			}) 					   
  }
});

