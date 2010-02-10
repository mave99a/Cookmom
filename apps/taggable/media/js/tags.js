/*
*  Initialize
*/
function attach_tags_handlers()
{
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
}

$(document).ready(function() {
  if (typeof(_JS_MODULE_TAG) != 'undefined') {
	
	attach_tags_handlers()
	
	$('.tags form').ajaxForm({
            beforeSubmit: function(formData, jqForm, options) {
                formData.push({ name: 'isAjax', value: '1' })    
            }, 	
            resetForm: true,
			success: function(data) {
				$('span.tagscontainer').html(data)
				attach_tags_handlers()
			}
		}
	)		   
  }
});

