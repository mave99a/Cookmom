$(document).ready(function() {
	$('form.comment').ajaxForm({
            resetForm: true,
			success: function(data) {
                alert('post ok')
			}
		}
	)
})