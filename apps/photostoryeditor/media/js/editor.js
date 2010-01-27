function getPhotoStoryJSON()
{	
	var json = '[';
	$('table#editor tr.row').each(function() {
			row = $(this);
			json += '{\'content\':\'' + row.find('textarea').val() + '\', \'images\':[' + row.find('input.imageslist').val()+']},'
		});
	
	json+=']';
	return json;
}

function attachPhotoStoryEditorEvents()
{
	$('textarea').elastic();
	
	$('.movedown').click(function() {
		row = $(this).parents('tr')
		row.hide()
		row.insertAfter(row.next()).show()
		row.show()
	})
	
	$('.moveup').click(function() {
		row = $(this).parents('tr')
		row.hide()
		row.insertBefore(row.prev()).show()
		row.show()
	})
	
	
	$('span.addrow').click(function() {
		row = $(this).parents('tr')
		$('#template-row').clone().insertBefore(row).show()
		//attachEvents();
	});
	
	$('a#save').click(function(){
		alert('save');
	});

	$('a#preview').click(function(){
		alert(getPhotoStoryJSON());
	});
	
	$('a#publish').click(function(){
		alert('publish');
	});		
	
}
