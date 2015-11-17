jQuery = require('../../bower_components/jquery/dist/jquery.min.js');
require('../../bower_components/bootstrap/dist/js/bootstrap.min.js');
$ = jQuery.noConflict();
$(function(){
	$(".del").on("click",function(){
		$.get("/backend/del/?id="+$(this).data("id"),function(data){
			location.href = location.href;
		});
	});
});
