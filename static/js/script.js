$(document).ready(function(){
    
    /**************************************************************************\
        Form Elements
    \**************************************************************************/
    $('#id_event_start, #id_event_end').datepicker({
        duration: 0,
        showTime: true
    });
	$('#id_display_start,#id_display_end').datepicker({duration: 0});
	$('.button, button').button();
	
	/**************************************************************************\
		Image preview functionality
	\**************************************************************************/
	var timer = null;
	var update_preview = function(delay){
		if (timer != null){
			clearTimeout(timer);
		}
		timer = setTimeout(function(){
			var url   = $('#preview').attr('src');
			var text  = $('#id_text').val();
			var size  = $('#id_font_size').val();
			var fg    = 'EBB700';
			$('#ImagePreview').attr('src', url + '?fg=' + fg + '&text=' + escape(text) + '&size=' + size);
		}, delay);
		
	}
	
	update_preview(0); //Update on page load
	$('#id_text').keyup(function(){
		update_preview(500);
	});
	$('#id_font_size').change(function(){
		update_preview(0);
	});
     
    /**************************************************************************\
        Pretty UI messages
    \**************************************************************************/
    jQuery.fn.message = function(style) {
        this.each(function() {
            var message = $(this);
            if(message.html()===undefined || !message.html() || message.html().length<1){
                return this;
            }
        
            var icon = {
                highlight : 'info',
                error     : 'alert',
                success   : 'check'
            };
        
            var html = "";
            if(message.find('p,h3,h4,h5').length > 0){
                html = '<div class="message"><div class="ui-state-' + style + ' ui-corner-all"> '
                        + message.html()
                        + '</div></div>';
        
            } else {
                html = '<div class="message"><div class="ui-state-' + style + ' ui-corner-all"> '
                        + '<p><span class="ui-icon ui-icon-' + icon[style] + '"></span>'
                        + message.html()
                        + '</p></div></div>';
            }
            message.html(html);
        });
        return this;
    };
    $('.highlight').message('highlight');
    $('.error').message('error');
    $('.success').message('success');
    
    /**************************************************************************\
         Django Error
     \**************************************************************************/
    $('.errorlist li').addClass('error');
    


});