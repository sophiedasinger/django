$('.likes').click(function () {
	var postid;
	postid = $(this).attr("data-postid");
	$.get('/like/', {post_id: postid}, function(data) {
		$('#like_count').html(data);
		$('#likes').hide();
	});
});