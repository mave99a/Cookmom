$(document).ready(function() {
	$('form.comment').ajaxForm({
            resetForm: true,
			success: function(data) {
                $('.comments_list table').prepend(data)
			}
		}
	)
})