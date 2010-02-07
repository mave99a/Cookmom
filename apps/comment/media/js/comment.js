$(document).ready(function() {
	$('form.comment').ajaxForm({
			dataType:  'json', 
            resetForm: true,
			success: function(data) {
				alert('comment posted')
			}
		}
	)
})