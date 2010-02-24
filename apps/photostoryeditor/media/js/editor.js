
$(document).ready(function() {

	$('#editor').click(function() {
		$('#editor-panel').show();
		$('#preview-panel').hide();
		$('#editor').parent('li').addClass('active')
		$('#preview').parent('li').removeClass('active')
	}); 
	
	$('#preview').click(function() {
		$('#editor-panel').hide();
		$('#preview-panel').show();	
		$('#preview').parent('li').addClass('active')
		$('#editor').parent('li').removeClass('active')
		$('#preview-panel').html('Saving...')
		
		$('#preview-panel').html('Loading...')
		$('#preview-panel').load('/article/ajax/preview/11/')
	});

});