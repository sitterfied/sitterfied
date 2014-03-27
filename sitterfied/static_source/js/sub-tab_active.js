jQuery(function() {
			if(jQuery('.tab_content .subtab_select li:nth-child(2)').hasClass('active')) { 
					jQuery('.tab_content .subtab_select').removeClass('movebg2 movebg3 movebg4 movebg5 movebg6').addClass('movebg');
		        } else if(jQuery('.tab_content .subtab_select li:nth-child(3)').hasClass('active')) {
					jQuery('.tab_content .subtab_select').removeClass('movebg3 movebg4 movebg5 movebg6').addClass('movebg movebg2');
		        } else if(jQuery('.tab_content .subtab_select li:nth-child(4)').hasClass('active')) {
					jQuery('.tab_content .subtab_select').removeClass('movebg2 movebg4 movebg5 movebg6').addClass('movebg movebg3');
		        } else if(jQuery('.tab_content .subtab_select li:nth-child(5)').hasClass('active')) {
					jQuery('.tab_content .subtab_select').removeClass('movebg3 movebg2 movebg5 movebg6').addClass('movebg movebg4');
		        } else if(jQuery('.tab_content .subtab_select li:nth-child(6)').hasClass('active')) {
					jQuery('.tab_content .subtab_select').removeClass('movebg3 movebg4 movebg2 movebg6').addClass('movebg movebg5');
		        } else if(jQuery('.tab_content .subtab_select li:nth-child(7)').hasClass('active')) {
					jQuery('.tab_content .subtab_select').removeClass('movebg3 movebg4 movebg5 movebg2').addClass('movebg movebg6');
		        } else {
					jQuery('.tab_content .subtab_select').removeClass('movebg movebg2 movebg3 movebg4 movebg5 movebg6');
		        }; 
				
				
});