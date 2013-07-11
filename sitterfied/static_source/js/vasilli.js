define(['jquery', 'jqueryui', 'select2', 'fancybox'], function($){
    $(function() {
	// Logo hover
		    $('.logo img').hover(function(){
		          $(this).attr('src', ('images/logo_h.png'));
		    });
		    $('.logo img').mouseout(function(){
		          $(this).attr('src', ('images/logo.png'));
		    });

	// Tabs
			$('.tabs_wrap .tab_content').hide();
			$('.tabs_wrap .tab_content:first').show();
			$('.tabs_wrap .tab_select li:first').addClass('active');
			$('.tabs_wrap .tab_select li a').click(function(){
				$('.tabs_wrap .tab_select li').removeClass('active');
				$(this).parent().addClass('active');
				var currentTab = $(this).attr('href');
				$('.tabs_wrap .tab_content').hide();
				$(currentTab).show();
				return false;
			});

	// Sub Tabs
			$('.tab_content .subtab_content').hide();
			$('.tab_content .subtab_content:first').show();
			$('.tab_content .subtab_select li:first').addClass('active');
			$('.tab_content .subtab_select li a').click(function(){
				$('.tab_content .subtab_select li').removeClass('active');
				$(this).parent().addClass('active');
				var currentTab = $(this).attr('href');
				$('.tab_content .subtab_content').hide();
				$(currentTab).show();
				if($('.tab_content .subtab_select li:nth-child(2)').hasClass('active')) {
					$('.tab_content .subtab_select').removeClass('movebg2 movebg3 movebg4 movebg5 movebg6').addClass('movebg');
		        } else if($('.tab_content .subtab_select li:nth-child(3)').hasClass('active')) {
					$('.tab_content .subtab_select').removeClass('movebg3 movebg4 movebg5 movebg6').addClass('movebg movebg2');
		        } else if($('.tab_content .subtab_select li:nth-child(4)').hasClass('active')) {
					$('.tab_content .subtab_select').removeClass('movebg2 movebg4 movebg5 movebg6').addClass('movebg movebg3');
		        } else if($('.tab_content .subtab_select li:nth-child(5)').hasClass('active')) {
					$('.tab_content .subtab_select').removeClass('movebg3 movebg2 movebg5 movebg6').addClass('movebg movebg4');
		        } else if($('.tab_content .subtab_select li:nth-child(6)').hasClass('active')) {
					$('.tab_content .subtab_select').removeClass('movebg3 movebg4 movebg2 movebg6').addClass('movebg movebg5');
		        } else if($('.tab_content .subtab_select li:nth-child(7)').hasClass('active')) {
					$('.tab_content .subtab_select').removeClass('movebg3 movebg4 movebg5 movebg2').addClass('movebg movebg6');
		        } else {
					$('.tab_content .subtab_select').removeClass('movebg movebg2 movebg3 movebg4 movebg5 movebg6');
		        };
				return false;
			});

	// Menu trigger
			$('.menu_trigger').on('click', function(){
				$(this).toggleClass('active');
				$('.header nav').fadeToggle();
			});

	// Select/datapicker styling
			$("select").select2();
			$( "#datepicker, #datepicker2, #datepicker3" ).datepicker({
				numberOfMonths: 2,
				showOtherMonths: true,
				selectOtherMonths: true,
				dateFormat: 'D, dd M yy',
				minDate: '0'
			});

	// Overnight/Multiday hide/show
			$('#check').click(function(){
				if($('#check').is(':checked')) {
					$('.find_form_block').addClass('active');
					$('.header .top_info .find_form_block .over_form').slideDown();
					$('.find_form_block form > ul > li:nth-child(2) label:first-child').html('From');
					$('.find_form_block form > ul > li:nth-child(3) label').html('');
		        } else {
					$('.find_form_block').removeClass('active');
					$('.header .top_info .find_form_block .over_form').slideUp();
					$('.find_form_block form > ul > li:nth-child(2) label:first-child').html('When');
					$('.find_form_block form > ul > li:nth-child(3) label').html('From');
		        };
			});

	// Bookmark and heart state
			$('.bookmark').on('click', function(){
				$(this).toggleClass('active');
			});
			$('.heart').on('click', function(){
				$(this).toggleClass('active');
			});

	// Filter block hide/show
			$(".sort_filter .filter a").on('click', function(){
				$(".sort_filter .filter").hide();
				$(".filter_block").slideDown();
				return false;
			});
			$(".filter_block form + p a").on('click', function(){
				$(".filter_block").slideUp();
				$(".sort_filter .filter").show();
				return false;
			});

	// Find form block hide/show
			$(".find_form_block .hide a").on('click', function(){
				$(".find_form_block .hide").hide();
				$(".find_form_block form").slideUp();
				$(".find_form_block .show").show();
				return false;
			});
			$(".find_form_block .show a").on('click', function(){
				$(".find_form_block .show").hide();
				$(".find_form_block form").slideDown();
				$(".find_form_block .hide").show();
				return false;
			});

	// Edit page show/hide note
			$('.booking_list .desc .note_wrap a').on('click', function(){
				$(this).toggleClass('hide_text');
				$(this).parent().parent().parent().find('.note_desc').slideToggle();
				return false;
			});

   	// Top image popup

   	// recommend_popup

	// guest_top_info list hide/show
			$(".guest_top_info .hide a").on('click', function(){
				$(".guest_top_info .hide").hide();
				$(".guest_top_info ul").slideUp();
				$(".guest_top_info .show").show();
				return false;
			});
			$(".guest_top_info .show a").on('click', function(){
				$(".guest_top_info .show").hide();
				$(".guest_top_info ul").slideDown();
				$(".guest_top_info .hide").show();
				return false;
			});

    // show/hide input value
			$('input[type="text"]').each(function(){
				var valtxt = $(this).attr('value');
				$(this).focus(function() { if ($(this).val() == valtxt) {$(this).val('');} });
				$(this).blur(function() { if ($(this).val() == '') {$(this).val(valtxt);} });
			});

    // top_info full_desc show/hide
			$('.header .top_info .desc .read_more').on('click', function(){
				$('.header .top_info').addClass('show_full_desc');
				$('.header .top_info .desc .full_desc').fadeIn();
				return false;
			});
			$('.header .top_info .desc .full_desc').on('click', function(){
				$('.header .top_info').removeClass('show_full_desc');
				$('.header .top_info .desc .full_desc').fadeOut();
			});

	// Fixed my_tabs_style block
			// var top = $('#fixed_tabs').offset().top - parseFloat($('#fixed_tabs').css('margin-top').replace(/auto/, 0));
			// 	$(window).scroll(function () {
			// 		var y = $(window).scrollTop();
			// 		if (y >= top) {
			// 			$('#fixed_tabs').addClass('fixed');
			// 		} else {
			// 			$('#fixed_tabs').removeClass('fixed');
			// 		}
			// });

	// Keep headers color while editing input/select/textarea fields
			$('.parent_book_block > ul > li > ul > li input[type="text"], .profile_block .form_style > ul > li > ul > li input[type="text"]').focus(function(){
				$(this).parent().parent().parent().addClass('focus');
			});
			$('.parent_book_block > ul > li > ul > li p input[type="text"], .profile_block .form_style > ul > li > ul > li p input[type="text"]').focus(function(){
				$(this).parent().parent().parent().parent().addClass('focus');
			});
			$('.parent_book_block > ul > li > ul > li input[type="checkbox"], .profile_block .form_style > ul > li > ul > li input[type="checkbox"]').click(function(){
				$(this).parent().parent().parent().addClass('focus');
			});
			$('.parent_book_block > ul > li > ul > li p input[type="checkbox"], .profile_block .form_style > ul > li > ul > li p input[type="checkbox"]').click(function(){
				$(this).parent().parent().parent().parent().addClass('focus');
			});
			$('.parent_book_block > ul > li > ul > li select + div input').focus(function(){
				$(this).parent().parent().parent().parent().parent().parent().addClass('focus');
			});
			$('.profile_block .form_style > ul > li > ul > li select + div input').focus(function(){
				$(this).parent().parent().parent().parent().parent().parent().parent().addClass('focus');
			});
			$('.profile_block .form_style > ul > li > ul > li p textarea').focus(function(){
				$(this).parent().parent().parent().parent().addClass('focus');
			});
			$('.parent_book_block > ul > li > ul > li .edit_button, .profile_block .form_style > ul > li > ul > li .button').on('click', function(){
				$(this).parent().parent().parent().removeClass('focus');
				$(this).parent().parent().parent().parent().removeClass('focus');
				return false;
			});

	// Request edit/save button
			$(".booking_list li .price .edit_button").click(function() {
				$(this).parent().toggleClass('active');
				if($(this).parent().hasClass('active')) {
					$(this).parent().find('input').focus();
		        };
				return false;
			});

	// Multiple sitters block
			$('.sort_filter .multiple_select a').on('click', function(){
				$(this).parent().hide();
				$('.multiple_sitters_block').slideDown();
				$('.sitter_tabs_wrap .select_wrap').show();
				$('.btns > a').hide();
				return false;
			});
			$('.multiple_sitters_block .close').on('click', function(){
				$('.multiple_sitters_block').slideUp();
				$('.sort_filter .multiple_select').show();
				$('.sitter_tabs_wrap .select_wrap').hide();
				$('.btns > a').show();
				return false;
			});
			$('.sitter_tabs_wrap .my_sitter_team li .btns .select_wrap input:checkbox').on('click', function(){
				var name = $(this).parent().parent().parent().find('.tit a').html();
				var link = $(this).parent().parent().parent().find('.tit a').attr('href');
				var nameid = $(this).attr('id');
			    if ($(this).is(":checked")) {
			    	$('.multiple_sitters_block ul li:last-child').before('<li class="team ' + nameid + '"><a href="' + link + '">' + name + '</a><span class="remove"><a href="#" class="' + nameid + '">&nbsp;</a></span></li>');
			    } else {
					if($('.multiple_sitters_block ul li').hasClass(nameid)) {
						$(this).parent().parent().parent().parent().parent().parent().parent().parent().find('.multiple_sitters_block li').each(function(){
							if($(this).hasClass(nameid)) {
								$(this).hide();
					        };
						});
			        };
			    };
				$('.multiple_sitters_block ul li .remove a').on('click', function(){
					var cname = $(this).attr('class');
					if($('.sitter_tabs_wrap .my_sitter_team li .btns .select_wrap input:checkbox').hasClass(cname)) {
						$(this).parent().parent().parent().parent().parent().parent().parent().find('.my_sitter_team li .btns .select_wrap input:checkbox').each(function(){
							if($(this).hasClass(cname)) {
								$(this).prop("checked", false);
					        };
						});
			        };
					$(this).parent().parent().hide();
					return false;
				});
			});
			$('.sitter_tabs_wrap .my_friends_sitters li .btns .select_wrap input:checkbox').on('click', function(){
				var name = $(this).parent().parent().parent().find('.tit a').html();
				var link = $(this).parent().parent().parent().find('.tit a').attr('href');
				var nameid = $(this).attr('id');
			    if ($(this).is(":checked")) {
			    	$('.multiple_sitters_block ul li:last-child').before('<li class="friends ' + nameid + '"><a href="' + link + '">' + name + '</a><span class="remove"><a href="#" class="' + nameid + '">&nbsp;</a></span></li>');
			    } else {
					if($('.multiple_sitters_block ul li').hasClass(nameid)) {
						$(this).parent().parent().parent().parent().parent().parent().parent().parent().find('.multiple_sitters_block li').each(function(){
							if($(this).hasClass(nameid)) {
								$(this).hide();
					        };
						});
			        };
			    };
				$('.multiple_sitters_block ul li .remove a').on('click', function(){
					var cname = $(this).attr('class');
					if($('.sitter_tabs_wrap .my_friends_sitters li .btns .select_wrap input:checkbox').hasClass(cname)) {
						$(this).parent().parent().parent().parent().parent().parent().parent().find('.my_friends_sitters li .btns .select_wrap input:checkbox').each(function(){
							if($(this).hasClass(cname)) {
								$(this).prop("checked", false);
					        };
						});
			        };
					$(this).parent().parent().hide();
					return false;
				});
			});
			$('.sitter_tabs_wrap .my_local_sitters li .btns .select_wrap input:checkbox').on('click', function(){
				var name = $(this).parent().parent().parent().find('.tit a').html();
				var link = $(this).parent().parent().parent().find('.tit a').attr('href');
				var nameid = $(this).attr('id');
			    if ($(this).is(":checked")) {
			    	$('.multiple_sitters_block ul li:last-child').before('<li class="local ' + nameid + '"><a href="' + link + '">' + name + '</a><span class="remove"><a href="#" class="' + nameid + '">&nbsp;</a></span></li>');
			    } else {
					if($('.multiple_sitters_block ul li').hasClass(nameid)) {
						$(this).parent().parent().parent().parent().parent().parent().parent().parent().find('.multiple_sitters_block li').each(function(){
							if($(this).hasClass(nameid)) {
								$(this).hide();
					        };
						});
			        };
			    };
				$('.multiple_sitters_block ul li .remove a').on('click', function(){
					var cname = $(this).attr('class');
					if($('.sitter_tabs_wrap .my_local_sitters li .btns .select_wrap input:checkbox').hasClass(cname)) {
						$(this).parent().parent().parent().parent().parent().parent().parent().find('.my_local_sitters li .btns .select_wrap input:checkbox').each(function(){
							if($(this).hasClass(cname)) {
								$(this).prop("checked", false);
					        };
						});
			        };
					$(this).parent().parent().hide();
					return false;
				});
			});
			$('.multiple_sitters_block ul li .remove a').on('click', function(){
				var cname = $(this).attr('class');
				if($('.sitter_tabs_wrap li .btns .select_wrap input:checkbox').hasClass(cname)) {
					$(this).parent().parent().parent().parent().parent().parent().parent().find('li .btns .select_wrap input:checkbox').each(function(){
						if($(this).hasClass(cname)) {
							$(this).prop("checked", false);
				        };
					});
		        };
				$(this).parent().parent().hide();
				return false;
			});
			$('.multiple_sitters_block ul li:last-child p .add_sitters').on('click', function(){
				$('.sitter_tabs_wrap .my_friends_sitters li .btns .select_wrap input:checkbox').each(function(){
					var name = $(this).parent().parent().parent().find('.tit a').html();
					var link = $(this).parent().parent().parent().find('.tit a').attr('href');
					var nameid = $(this).attr('id');
			    	$('.multiple_sitters_block ul li:last-child').before('<li class="friends ' + nameid + '"><a href="' + link + '">' + name + '</a><span class="remove"><a href="#" class="' + nameid + '">&nbsp;</a></span></li>');
					$(this).prop("checked", true);
			    });
				$('.multiple_sitters_block ul li .remove a').on('click', function(){
					var cname = $(this).attr('class');
					if($('.sitter_tabs_wrap .my_friends_sitters li .btns .select_wrap input:checkbox').hasClass(cname)) {
						$(this).parent().parent().parent().parent().parent().parent().parent().find('.my_friends_sitters li .btns .select_wrap input:checkbox').each(function(){
							if($(this).hasClass(cname)) {
								$(this).prop("checked", false);
					        };
						});
			        };
					$(this).parent().parent().hide();
					return false;
				});
				return false;
			});
			$('.multiple_sitters_block ul li:last-child p .remove_team').on('click', function(){
				$('.multiple_sitters_block ul li.team').hide();
				$('.sitter_tabs_wrap .my_sitter_team li .btns .select_wrap input:checkbox').prop("checked", false);
				return false;
			});





	// For mobile
			if( $(window).width() < 959)
			{
				// Header ico
						$('.header .top_info .ico > ul > li').on('click', function(){
							$(this).toggleClass('active');
							$("> ul", this).slideToggle();
						});
				// Tabs
						$('.tab_content .snapshot_block').hide();
						$('.tab_content .about_details_block').show();

						$('.parent_book_block > ul > li > ul').hide();
						$('.parent_book_block > ul > li > div').on('click', function(){
							$(this).toggleClass('active');
							$("+ ul", this).slideToggle();
						});
			};
			$('.mob_tab_trigger').on('click', function(){
				$(this).toggleClass('active');
				$("+ .subtab_content", this).slideToggle();
				$("+ .tab_content", this).slideToggle();
			});
});
})
