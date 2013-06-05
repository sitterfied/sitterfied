define(['jquery', 'jqueryui', 'chosen'], function($){
    $(function() {

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
		    return false;
	    });

	    // Menu trigger
	    $('.menu_trigger').on('click', function(){
		    $('.header nav').fadeToggle();
	    });

	    // Select/datapicker styling
	    $("select").chosen();
	    $( "#datepicker" ).datepicker({
		    numberOfMonths: 2,
		    showOtherMonths: true,
		    selectOtherMonths: true,
		    dateFormat: 'D, dd M yy'
	    });

	    // Filter block hide/show
	    $(".sort_filter .filter a").on('click', function(){
		    $(".sort_filter .filter").hide();
		    $(".filter_block").show();
		    return false;
	    });
	    $(".filter_block form + p a").on('click', function(){
		    $(".filter_block").hide();
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

	    // For mobile
		// Header ico
	    $('.header .top_info .ico > ul > li').on('click', function(){
		    $(this).toggleClass('active');
		    $("> ul", this).slideToggle();
	    });
		// Tabs
	    if( $(window).width() < 959)
	    {
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
