$(document).ready(function(){
	
	/**************************************************************************\
		Image preview functionality
	\**************************************************************************/	
	var timer = null;
	function update_preview(delay){
		if (timer != null){
			clearTimeout(timer);
		}
		timer = setTimeout(function(){
			var url	  = $('#preview').attr('src');
			var text  = $('#id_text').val();
			var font  = $('#id_font').val();
			var size  = $('#id_font_size').val();
			var fg	  = $('#id_color_font').val();
			var bg	  = $('#id_color_bg').val();
			var src	  = url +
				'?text=' + escape(text) +
				'&size=' + escape(size) +
				'&fg=' + escape(fg) +
				'&bg=' + escape(bg) +
				'&font=' + escape(font);
			
			$('#image-preview').attr('src', src);
			$('#image-download').attr('href', src+'&download=true');
			
			
		}, delay);
	}
	update_preview(0);
	$('#id_text').keyup(function(){update_preview(750);});
	$('#id_font').change(function(){update_preview(0);});
	$('#id_font_size').change(function(){update_preview(0);});
	$('#id_color_font').change(function(){update_preview(0);});
	$('#id_color_bg').change(function(){update_preview(0);});
	
	
	
	/**************************************************************************\
		Slide Scheme Widget
		- would/should normally add this in a separate file as form media
		  using the widget class, but widget isn't being released as it's
		  own piece, so it's all good
	\**************************************************************************/
	$('.scheme').each(function(){
		
		var hex = function(rgbString){
			var parts = rgbString.match(/^rgb\((\d+),\s*(\d+),\s*(\d+)\)$/);
			if(!parts){
				if(rgbString.match(/^#\S{3,6}$/))
					return rgbString.substr(1);
				return 'ff33ff'; //you'll know it's an error
			}
			delete (parts[0]);
			for (var i = 1; i <= 3; ++i) {
				parts[i] = parseInt(parts[i]).toString(16);
				if (parts[i].length == 1) parts[i] = '0' + parts[i];
			}
			return parts.join(''); // "0070ff			 
		}
		
		var s = $(this);
		var bg = hex(s.css('background-color'));
		var color = hex(s.css('color'));
		s.click(function(e){
			e.preventDefault();
			$('#id_color_bg').val(bg);
			$('#id_color_font').val(color);
			update_preview(0);
		});
		
	});
	
	

});