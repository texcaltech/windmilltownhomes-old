// Init 
$(function() {
	initTabs();
});

// Init header tabs
function initTabs() {
	// Get tab and search for relevant html tag
	var tab = location.pathname;
	var tag = $('#tabs a[href="' + tab + '"]');
	tag.addClass('selected');
}