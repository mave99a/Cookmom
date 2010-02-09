$(document).ready(function() {
	$('form.comment').ajaxForm({
            resetForm: true,
            beforeSubmit: function(formData, jqForm, options) {
                formData.push({ name: 'isAjax', value: '1' })    
            }, 
			success: function(data) {
                $('.comments_list table').prepend(data)
			}
		}
	)
})