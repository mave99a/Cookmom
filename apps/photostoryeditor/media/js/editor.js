//  Insert a text to the current cursor location of a textarea
//  code borrowed from: http://alexking.org/blog/2004/06/03/js-quicktags-under-lgpl
function edInsertContent(myField, myValue) {
	//IE support
	if (document.selection) {
		myField.focus();
		sel = document.selection.createRange();
		sel.text = myValue;
		myField.focus();
	}
	//MOZILLA/NETSCAPE support
	else if (myField.selectionStart || myField.selectionStart == '0') {
		var startPos = myField.selectionStart;
		var endPos = myField.selectionEnd;
		var scrollTop = myField.scrollTop;
		myField.value = myField.value.substring(0, startPos)
		              + myValue 
                      + myField.value.substring(endPos, myField.value.length);
		myField.focus();
		myField.selectionStart = startPos + myValue.length;
		myField.selectionEnd = startPos + myValue.length;
		myField.scrollTop = scrollTop;
	} else {
		myField.value += myValue;
		myField.focus();
	}
}

function attach_image_handles()
{
	$('img.image_handle').click(function() {
		editor = $('textarea#editor').get(0)
		edInsertContent(editor, '[' + $(this).attr('id')+ ']')
	})
}

var pageDirty = false;
var msg = 'you have not yet save it!'
	
$(document).ready(function() {
	if (typeof(EDITOR_PAGE) != 'undefined') {

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
			$('#preview-panel').load('/article/ajax/preview/11/', 
				function() {
			        if (typeof(FB) != 'undefined') {
			            // make sure newly added FBML get displayed correctly
			            FB.XFBML.Host.parseDomElement($('#preview-panel').get(0));
			        }
			    }
			)
			
		});
		
		attach_image_handles();
		
	    window.onbeforeunload = function(){
	        if(pageDirty){
	            return msg;
	        }
	    };
	}
});