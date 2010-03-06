// start the queue if the queue is already disabled
$('#upload').click(function(){
	$('.swfupload-control').swfupload('startUpload');
});

$(function(){
	$('.swfupload-control').swfupload({
			upload_url: "/image/upload/",
			file_size_limit : "10240",
			file_types : "*.*",
			file_types_description : "All Files",
			file_upload_limit : "0",
			flash_url : $('.swfupload-control').attr('flashurl'),
			button_width : 200,
			button_height : 30,
			button_placeholder : $('#spanButtonPlaceholder', this)[0],
			button_window_mode: SWFUpload.WINDOW_MODE.TRANSPARENT,
			button_cursor: SWFUpload.CURSOR.HAND, 
			debug: false,
		});

    // assign our event handlers
    $('.swfupload-control')
        .bind('fileQueued', function(event, file){
            // start the upload once a file is queued
            $(this).swfupload('startUpload');
        })
        .bind('uploadComplete', function(event, file){
            // start the upload (if more queued) once an upload is complete
            $(this).swfupload('startUpload');
        })
        .bind('uploadError', function(event, file, errorCode, message){

        })
        .bind('uploadSuccess', function(event, file, serverData){
        });	
});