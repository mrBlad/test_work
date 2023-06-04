$(document).ready( function() {
    $(".file-uploader input[type=file]").change(function(){
         var filename = $(this).val().replace(/.*\\/, "");
         $("#filename").val(filename);
    });
});