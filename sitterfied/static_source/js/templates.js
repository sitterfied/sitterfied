define(['ember'], function(Ember){Ember.TEMPLATES["topNote"] = Ember.Handlebars.template(function anonymous(Handlebars,depth0,helpers,partials,data) {
this.compilerInfo = [3,'>= 1.0.0-rc.4'];
helpers = helpers || Ember.Handlebars.helpers; data = data || {};
  


  data.buffer.push("	  Hi Alex, you have 6 free months\n	  <div>\n		<p>Invite more frıends</p>\n		<span>&nbsp;</span>\n	  </div>\n");
  
});
Ember.TEMPLATES["parent"] = Ember.Handlebars.template(function anonymous(Handlebars,depth0,helpers,partials,data) {
this.compilerInfo = [3,'>= 1.0.0-rc.4'];
helpers = helpers || Ember.Handlebars.helpers; data = data || {};
  


  data.buffer.push("<div class=\"container clear\">\n  <div class=\"wraper\">\n\n	<!-- network_block -->\n	<div class=\"network_block\">\n	  <ul class=\"soc_psg_list soc_psg_list_single clear\">\n		<li>\n		  <ul>\n			<li>Mutual Parent Friends (4)</li>\n			<li><a href=\"#\"><img src=\"/static/images/demo/img15.jpg\" alt=\"\" /></a><a href=\"#\">Mika Pinna</a></li>\n			<li><a href=\"#\"><img src=\"/static/images/demo/img15.jpg\" alt=\"\" /></a><a href=\"#\">Lakeisha Powanda</a></li>\n			<li><a href=\"#\"><img src=\"/static/images/demo/img15.jpg\" alt=\"\" /></a><a href=\"#\">Connie Takach</a></li>\n			<li><a href=\"#\"><img src=\"/static/images/demo/img15.jpg\" alt=\"\" /></a><a href=\"#\">Jane Eyre</a></li>\n		  </ul>\n		</li>\n		<li>\n		  <ul>\n			<li>Mutual Sitter Friends (3)</li>\n			<li><a href=\"#\"><img src=\"/static/images/demo/img15.jpg\" alt=\"\" /></a><a href=\"#\">Lakeisha Powanda</a></li>\n			<li><a href=\"#\"><img src=\"/static/images/demo/img15.jpg\" alt=\"\" /></a><a href=\"#\">Connie Takach</a></li>\n			<li><a href=\"#\"><img src=\"/static/images/demo/img15.jpg\" alt=\"\" /></a><a href=\"#\">Jane Eyre</a></li>\n		  </ul>\n		</li>\n		<li>\n		  <ul>\n			<li>Mutual Groups (3)</li>\n			<li><a href=\"#\">Hoboken Catholic Church</a> <a href=\"#\" class=\"delete\">&nbsp;</a></li>\n			<li><a href=\"#\">St Francis Prep School</a> <a href=\"#\" class=\"delete\">&nbsp;</a></li>\n			<li><a href=\"#\">Hoboken Mommies</a> <a href=\"#\" class=\"delete\">&nbsp;</a></li>\n		  </ul>\n		</li>\n	  </ul>\n	</div>\n	<!-- /network_block -->\n\n  </div>\n</div>");
  
});
Ember.TEMPLATES["parent/top"] = Ember.Handlebars.template(function anonymous(Handlebars,depth0,helpers,partials,data) {
this.compilerInfo = [3,'>= 1.0.0-rc.4'];
helpers = helpers || Ember.Handlebars.helpers; data = data || {};
  var buffer = '', stack1, stack2, hashContexts, hashTypes, options, self=this, helperMissing=helpers.helperMissing;

function program1(depth0,data) {
  
  
  data.buffer.push("Back to search results");
  }

  hashContexts = {'class': depth0};
  hashTypes = {'class': "STRING"};
  options = {hash:{
    'class': ("back")
  },inverse:self.noop,fn:self.program(1, program1, data),contexts:[depth0],types:["ID"],hashContexts:hashContexts,hashTypes:hashTypes,data:data};
  stack2 = ((stack1 = helpers.linkTo),stack1 ? stack1.call(depth0, "search", options) : helperMissing.call(depth0, "linkTo", "search", options));
  if(stack2 || stack2 === 0) { data.buffer.push(stack2); }
  data.buffer.push("\n<!-- top info -->\n<div class=\"top_info clear\">\n  <div class=\"member_since guest\"></div>\n  <div class=\"photo\">\n	<div class=\"photo_edit_wrap\">\n	  <img src=\"/static/images/demo/img2.jpg\" alt=\"\" />\n	  <p><span class=\"icon_pen\">&nbsp;</span><a href=\"#edit_photo_popup\">Edit Photo</a></p>\n	</div>\n  </div>\n  <div class=\"guest_top_info\">\n	<p>Alex Patrick</p>\n	<p>1 Child &nbsp;|&nbsp; New York, NY</p>\n	<div class=\"know\">\n	  <p>Do you know Jane?</p>\n	  <p>Connect with this person via Facebook or Gmail to have them automatically added to your Sitterfied network. <a href=\"#\">Learn more</a>.</p>\n	</div>\n  </div>\n</div>\n<!-- /top info -->\n<!-- quick_info_list -->\n<div class=\"quick_info_list clear\" id=\"fixed_tabs\">\n  <ul>\n	<li><strong>114</strong> friends</li>\n	<li><strong>5</strong>groups</li>\n  </ul>\n</div>\n<!-- /quick_info_list -->");
  return buffer;
  
});
Ember.TEMPLATES["done"] = Ember.Handlebars.template(function anonymous(Handlebars,depth0,helpers,partials,data) {
this.compilerInfo = [3,'>= 1.0.0-rc.4'];
helpers = helpers || Ember.Handlebars.helpers; data = data || {};
  var buffer = '', stack1, stack2, hashTypes, hashContexts, options, escapeExpression=this.escapeExpression, self=this, helperMissing=helpers.helperMissing;

function program1(depth0,data) {
  
  
  data.buffer.push("Go to bookings");
  }

  data.buffer.push("\n<div class=\"container clear\">\n	<div class=\"wraper notify_wraper\">\n		<p>Etiam at risus et justo dignissim congue. Donec congue lacinia dui, a porttitor lectus condimentum laoreet. Nunc eu ullamcorper orci. Quisque eget odio ac lectus vestibulum faucibus eget in metus. In pellentesque.</p>\n		<ul>\n			<li><span class=\"icon_date\">&nbsp;</span>Wednesday 1 August 2012 &nbsp; <span>4:00 pm — 6:00 pm</span></li>\n			<li><span class=\"icon_friends5\">&nbsp;</span>2 Kids</li>\n			<li><span class=\"icon_pin3\">&nbsp;</span>33 Nassau Ave Suite #2 NY, New York</li>\n		</ul>\n		<p><a ");
  hashTypes = {};
  hashContexts = {};
  data.buffer.push(escapeExpression(helpers.action.call(depth0, "edit", {hash:{},contexts:[depth0],types:["STRING"],hashContexts:hashContexts,hashTypes:hashTypes,data:data})));
  data.buffer.push(" class=\"button button_small button_edit\"><span class=\"icon_edit\">&nbsp;</span>Edit</a><a ");
  hashTypes = {};
  hashContexts = {};
  data.buffer.push(escapeExpression(helpers.action.call(depth0, "cancel", {hash:{},contexts:[depth0],types:["STRING"],hashContexts:hashContexts,hashTypes:hashTypes,data:data})));
  data.buffer.push(" class=\"button button_small button_cancel\"><span class=\"icon_cancel\">&nbsp;</span>Cancel</a></p>\n\n        <p>");
  hashContexts = {'class': depth0};
  hashTypes = {'class': "STRING"};
  options = {hash:{
    'class': ("button")
  },inverse:self.noop,fn:self.program(1, program1, data),contexts:[depth0],types:["ID"],hashContexts:hashContexts,hashTypes:hashTypes,data:data};
  stack2 = ((stack1 = helpers.linkTo),stack1 ? stack1.call(depth0, "book", options) : helperMissing.call(depth0, "linkTo", "book", options));
  if(stack2 || stack2 === 0) { data.buffer.push(stack2); }
  data.buffer.push("</p>\n	</div>\n</div>\n");
  return buffer;
  
});
Ember.TEMPLATES["done/top"] = Ember.Handlebars.template(function anonymous(Handlebars,depth0,helpers,partials,data) {
this.compilerInfo = [3,'>= 1.0.0-rc.4'];
helpers = helpers || Ember.Handlebars.helpers; data = data || {};
  


  data.buffer.push("	<div class=\"top_notify clear\">\n			<p class=\"sent\">Request Sent!</p>\n	</div>");
  
});
Ember.TEMPLATES["emptysearch"] = Ember.Handlebars.template(function anonymous(Handlebars,depth0,helpers,partials,data) {
this.compilerInfo = [3,'>= 1.0.0-rc.4'];
helpers = helpers || Ember.Handlebars.helpers; data = data || {};
  


  data.buffer.push("<div class=\"container clear\">\n  <div class=\"wraper\">\n\n	<!-- tabs_wrap -->\n	<div class=\"tabs_wrap my_tabs_style tabs_no_results\">\n	  <ul class=\"tab_select\" id=\"fixed_tabs\">\n		<li><a href=\"#tab-1\">sitter<br />team<span>0</span></a></li>\n		<li><a href=\"#tab-2\">friends<br />sitters<span>0</span></a></li>\n		<li><a href=\"#tab-3\">local<br />sitters<span>0</span></a></li>\n	  </ul>\n\n	  <!-- my_sitter_team -->\n	  <div class=\"mob_tab_trigger my_mob_tab\">sitter<br />team<span>0</span></div>\n	  <div class=\"tab_content my_sitter_team\" id=\"tab-1\">\n		<!-- sitter team 0 -->\n	  </div>\n	  <!-- /my_sitter_team -->\n\n	  <!-- my_friends_sitters -->\n	  <div class=\"mob_tab_trigger my_mob_tab\">friends<br />sitters<span>0</span></div>\n	  <div class=\"tab_content friends_block my_friends_sitters\" id=\"tab-2\">\n		<!-- friends sitters 0 -->\n	  </div>\n	  <!-- /my_friends_sitters -->\n\n	  <!-- my_local_sitters -->\n	  <div class=\"mob_tab_trigger my_mob_tab\">local<br />sitters<span>0</span></div>\n	  <div class=\"tab_content my_local_sitters\" id=\"tab-3\">\n		<!-- local sitters 0 -->\n	  </div>\n	  <!-- /my_local_sitters -->\n\n	</div>\n	<!-- /tabs_wrap -->\n\n	<!-- no_results -->\n	<div class=\"no_results clear\">\n	  <p>We’re not in your neighborhood just yet.</p>\n	  <p>Here are a few things you can do right now.</p>\n	  <ul>\n		<li>\n		  <p><a href=\"#\" class=\"button\">Invite</a></p>\n		  <p>Invite your friends and discover great sitters together. We’ll even reward you and your friends with free months as they join Sitterfied</p>\n		</li>\n		<li>\n		  <p><a href=\"#\" class=\"button\">Connect</a></p>\n		  <p>Connect with your existing social networks to find great sitters through your friends</p>\n		</li>\n		<li>\n		  <p><a href=\"#\" class=\"button\">Sign Up</a></p>\n		  <p>Sign up to follow our progress and we’ll let you know when great sitters are added to your area</p>\n		</li>\n	  </ul>\n	</div>\n	<!-- /no_results -->\n\n  </div>\n</div>\n");
  
});
Ember.TEMPLATES["search"] = Ember.Handlebars.template(function anonymous(Handlebars,depth0,helpers,partials,data) {
this.compilerInfo = [3,'>= 1.0.0-rc.4'];
helpers = helpers || Ember.Handlebars.helpers; data = data || {};
  


  data.buffer.push("<div class=\"container clear\">\n  <div class=\"wraper\">\n\n	<!-- sitter_tabs_wrap -->\n	<div class=\"sitter_tabs_wrap my_tabs_style\">\n	  <div class=\"stabs_block\" id=\"fixed_tabs\">\n		<nav>\n		  <ul class=\"tab_select\">\n			<li class=\"active\"><a href=\"#tab-1\">sitter<br />team<span>7</span></a></li>\n			<li><a href=\"#tab-2\">friends'<br />sitters<span>42</span></a></li>\n			<li><a href=\"#tab-3\">local<br />sitters<span>519</span></a></li>\n		  </ul>\n		</nav>\n		<div class=\"friends_block my_friends_sitters\">\n		  <div class=\"multiple_sitters_block clear\">\n			<a href=\"#\" class=\"close\">&nbsp;</a>\n			<ul>\n			  <li class=\"team select1\"><a href=\"#\">Ellen Vukelich</a><span class=\"remove\"><a href=\"#\" class=\"select1\">&nbsp;</a></span></li>\n			  <li>\n				<p>+ <a href=\"#\" class=\"add_sitters\">ADD ALL FRIENDS’ SITTERS</a></p>\n				<p>- &nbsp;<a href=\"#\" class=\"remove_team\">REMOVE SITTER TEAM</a></p>\n			  </li>\n			</ul>\n			<p>Select from the available sitters below. <a href=\"#\" class=\"button button_small\"><span class=\"icon_ok2\">&nbsp;</span>submit</a></p>\n		  </div>\n		  <div class=\"filter_block\">\n			<p><a href=\"#\">Reset Filters</a></p>\n			<form method=\"post\" action=\"#\">\n			  <ul class=\"clear\">\n				<li><select data-placeholder=\"Choose languages\" multiple tabindex=\"1\"><option>test</option><option>test2</option></select></li>\n				<li><select data-placeholder=\"Education level\" multiple tabindex=\"2\"><option>test</option></select></li>\n				<li><select data-placeholder=\"Training/Certifications\" multiple tabindex=\"3\"><option>test</option></select></li>\n				<li><select data-placeholder=\"Level of Experience\" multiple tabindex=\"4\"><option>test</option></select></li>\n				<li><select data-placeholder=\"Type of Experience\" multiple tabindex=\"5\"><option>test</option></select></li>\n				<li><select data-placeholder=\"Other\" multiple tabindex=\"6\"><option>test</option></select></li>\n			  </ul>\n			</form>\n			<p><a href=\"#\">Hide Filters</a></p>\n		  </div>\n		  <div class=\"sort_filter clear\">\n			<div class=\"sort\"><a href=\"#\">Sort by</a></div>\n			<div class=\"multiple_select\"><a href=\"#\">Select multiple sitters</a></div>\n			<div class=\"filter\"><a href=\"#\">Filter</a> my sitters</div>\n		  </div>\n		</div>\n	  </div>\n\n	  <!-- my_sitter_team -->\n	  <section id=\"tab-1\">\n		<div class=\"mob_tab_trigger my_mob_tab\">sitter<br />team<span>7</span></div>\n		<div class=\"my_sitter_team\">\n		  <div class=\"sitter_title\">\n			<p><span><span class=\"icon_heart2\">&nbsp;</span>sitter<br />team</span><strong>7</strong></p>\n		  </div>\n		  <ul class=\"clear\">\n			<li>\n			  <div class=\"tit\">\n				<span><strong>$15</strong> /hr</span>\n				<a href=\"#\">Ellen Vukelich</a>\n			  </div>\n			  <div class=\"img\">\n				<a href=\"#\"><img src=\"/static/images/demo/img13.jpg\" alt=\"\" /></a>\n			  </div>\n			  <ul>\n				<li><span class=\"icon_plus_box\">&nbsp;</span>Last hired: <span>April 23, 2013</span></li>\n				<li><span class=\"icon_reload\">&nbsp;</span>4 jobs <span class=\"friends_span\"><span class=\"icon_friends4\">&nbsp;</span><a href=\"#\">24 sitter friends</a></span></li>\n			  </ul>\n			  <div class=\"btns clear\">\n				<div class=\"select_wrap\"><input type=\"checkbox\" checked=\"\" class=\"select1\" id=\"select1\" /><label for=\"select1\">Select</label></div>\n				<a class=\"button\" href=\"#\">BOOK</a>\n				<p><a href=\"#\">REMOVE FROM SITTER TEAM</a></p>\n			  </div>\n			</li>\n			<li>\n			  <div class=\"tit\">\n				<span><strong>$15</strong> /hr</span>\n				<a href=\"#\">Amy Randall</a>\n			  </div>\n			  <div class=\"img\">\n				<a href=\"#\"><img src=\"/static/images/demo/img13.jpg\" alt=\"\" /></a>\n			  </div>\n			  <ul>\n				<li><span class=\"icon_plus_box\">&nbsp;</span>Last hired: <span>April 23, 2013</span></li>\n				<li><span class=\"icon_reload\">&nbsp;</span>4 jobs <span class=\"friends_span\"><span class=\"icon_friends4\">&nbsp;</span><a href=\"#\">24 sitter friends</a></span></li>\n			  </ul>\n			  <div class=\"btns clear\">\n				<div class=\"select_wrap\"><input type=\"checkbox\" class=\"select2\" id=\"select2\" /><label for=\"select2\">Select</label></div>\n				<a class=\"button\" href=\"#\">BOOK</a>\n				<p><a href=\"#\">REMOVE FROM SITTER TEAM</a></p>\n			  </div>\n			</li>\n		  </ul>\n		</div>\n	  </section>\n	  <!-- /my_sitter_team -->\n\n	  <!-- my_friends_sitters -->\n	  <section id=\"tab-2\">\n		<div class=\"mob_tab_trigger my_mob_tab\">friends'<br />sitters<span>42</span></div>\n		<div class=\"friends_block my_friends_sitters\">\n		  <div class=\"sitter_title\">\n			<p><span><span class=\"icon_heart2\">&nbsp;</span>friends’<br />sitters</span><strong>42</strong></p>\n		  </div>\n		  <ul class=\"clear\">\n			<li>\n			  <div class=\"bookmark\"></div>\n			  <div class=\"tit\">\n				<span><strong>$15</strong> /hr</span>\n				<a href=\"#\">Sandy Thompson</a>\n			  </div>\n			  <div class=\"img\">\n				<div class=\"heart\"></div>\n				<a href=\"#\"><img src=\"/static/images/demo/img13.jpg\" alt=\"\" /></a>\n				<span>Background Cleared</span>\n			  </div>\n			  <ul>\n				<li><span class=\"icon_friends3\">&nbsp;</span>5 mutual friends\n				<ul>\n				  <li>Friends you have in common</li>\n				  <li><a href=\"#\"><img src=\"/static/images/demo/img3.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n				  <li><a href=\"#\"><img src=\"/static/images/demo/img4.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n				  <li><a href=\"#\"><img src=\"/static/images/demo/img5.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n				  <li><a href=\"#\"><img src=\"/static/images/demo/img6.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n				  <li><a href=\"#\"><img src=\"/static/images/demo/img7.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n				  <li><a href=\"#\"><img src=\"/static/images/demo/img8.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n				  <li><a href=\"#\"><img src=\"/static/images/demo/img9.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n				  <li><a href=\"#\"><img src=\"/static/images/demo/img10.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n				</ul>\n				</li>\n				<li><span class=\"icon_recommend2\">&nbsp;</span>4 recommends\n				<ul>\n				  <li>Recommendations</li>\n				  <li><a href=\"#\"><img src=\"/static/images/demo/img3.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n				  <li><a href=\"#\"><img src=\"/static/images/demo/img4.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n				  <li><a href=\"#\"><img src=\"/static/images/demo/img5.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n				  <li><a href=\"#\"><img src=\"/static/images/demo/img6.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n				  <li><a href=\"#\"><img src=\"/static/images/demo/img7.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n				  <li><a href=\"#\"><img src=\"/static/images/demo/img8.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n				  <li><a href=\"#\"><img src=\"/static/images/demo/img9.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n				  <li><a href=\"#\"><img src=\"/static/images/demo/img10.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n				</ul>\n				</li>\n				<li><span class=\"icon_team3\">&nbsp;</span>9 sitter teams\n				<ul>\n				  <li>Added to sitter teams and repeatedly hired</li>\n				  <li><a href=\"#\"><img src=\"/static/images/demo/img3.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n				  <li><a href=\"#\"><img src=\"/static/images/demo/img4.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n				  <li><a href=\"#\"><img src=\"/static/images/demo/img5.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n				  <li><a href=\"#\"><img src=\"/static/images/demo/img6.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n				  <li><a href=\"#\"><img src=\"/static/images/demo/img7.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n				  <li><a href=\"#\"><img src=\"/static/images/demo/img8.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n				  <li><a href=\"#\"><img src=\"/static/images/demo/img9.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n				  <li><a href=\"#\"><img src=\"/static/images/demo/img10.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n				</ul>\n				</li>\n				<li><span class=\"icon_reviews\">&nbsp;</span>11 reviews\n				<ul>\n				  <li class=\"rev clear\">\n					<a href=\"#\"><img src=\"/static/images/demo/img3.jpg\" alt=\"\" /></a>\n					<div>\n					  <p>Ellen has been a sitter for my children fore more than a year and I couldn’t be happier! She arrives on time and my kids light up when they see her!</p>\n					  <p><a href=\"#\">Read more reviews </a></p>\n					</div>\n				  </li>\n				</ul>\n				</li>\n			  </ul>\n			  <div class=\"btns clear\">\n				<div class=\"select_wrap\"><input type=\"checkbox\" class=\"select3\" id=\"select3\" /><label for=\"select3\">Select</label></div>\n				<a class=\"button\" href=\"#\">BOOK</a><a class=\"button button2\" href=\"#\">INTERVIEW</a>\n				<p><a href=\"#\">ADD TO SITTER TEAM</a></p>\n				<p><a href=\"#\">BOOKMARK</a></p>\n			  </div>\n			</li>\n			<li>\n			  <div class=\"bookmark\"></div>\n			  <div class=\"tit\">\n				<span><strong>$15</strong> /hr</span>\n				<a href=\"#\">Erica Sanders</a>\n			  </div>\n			  <div class=\"img\">\n				<div class=\"heart\"></div>\n				<a href=\"#\"><img src=\"/static/images/demo/img13.jpg\" alt=\"\" /></a>\n				<span>Background Cleared</span>\n			  </div>\n			  <ul>\n				<li><span class=\"icon_friends3\">&nbsp;</span>5 mutual friends\n				<ul>\n				  <li>Friends you have in common</li>\n				  <li><a href=\"#\"><img src=\"/static/images/demo/img3.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n				  <li><a href=\"#\"><img src=\"/static/images/demo/img4.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n				  <li><a href=\"#\"><img src=\"/static/images/demo/img5.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n				  <li><a href=\"#\"><img src=\"/static/images/demo/img6.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n				  <li><a href=\"#\"><img src=\"/static/images/demo/img7.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n				  <li><a href=\"#\"><img src=\"/static/images/demo/img8.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n				  <li><a href=\"#\"><img src=\"/static/images/demo/img9.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n				  <li><a href=\"#\"><img src=\"/static/images/demo/img10.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n				</ul>\n				</li>\n				<li><span class=\"icon_recommend2\">&nbsp;</span>4 recommends\n				<ul>\n				  <li>Recommendations</li>\n				  <li><a href=\"#\"><img src=\"/static/images/demo/img3.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n				  <li><a href=\"#\"><img src=\"/static/images/demo/img4.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n				  <li><a href=\"#\"><img src=\"/static/images/demo/img5.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n				  <li><a href=\"#\"><img src=\"/static/images/demo/img6.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n				  <li><a href=\"#\"><img src=\"/static/images/demo/img7.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n				  <li><a href=\"#\"><img src=\"/static/images/demo/img8.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n				  <li><a href=\"#\"><img src=\"/static/images/demo/img9.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n				  <li><a href=\"#\"><img src=\"/static/images/demo/img10.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n				</ul>\n				</li>\n				<li><span class=\"icon_team3\">&nbsp;</span>9 sitter teams\n				<ul>\n				  <li>Added to sitter teams and repeatedly hired</li>\n				  <li><a href=\"#\"><img src=\"/static/images/demo/img3.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n				  <li><a href=\"#\"><img src=\"/static/images/demo/img4.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n				  <li><a href=\"#\"><img src=\"/static/images/demo/img5.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n				  <li><a href=\"#\"><img src=\"/static/images/demo/img6.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n				  <li><a href=\"#\"><img src=\"/static/images/demo/img7.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n				  <li><a href=\"#\"><img src=\"/static/images/demo/img8.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n				  <li><a href=\"#\"><img src=\"/static/images/demo/img9.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n				  <li><a href=\"#\"><img src=\"/static/images/demo/img10.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n				</ul>\n				</li>\n				<li><span class=\"icon_reviews\">&nbsp;</span>11 reviews\n				<ul>\n				  <li class=\"rev clear\">\n					<a href=\"#\"><img src=\"/static/images/demo/img3.jpg\" alt=\"\" /></a>\n					<div>\n					  <p>Ellen has been a sitter for my children fore more than a year and I couldn’t be happier! She arrives on time and my kids light up when they see her!</p>\n					  <p><a href=\"#\">Read more reviews </a></p>\n					</div>\n				  </li>\n				</ul>\n				</li>\n			  </ul>\n			  <div class=\"btns clear\">\n				<div class=\"select_wrap\"><input type=\"checkbox\" class=\"select4\" id=\"select4\" /><label for=\"select4\">Select</label></div>\n				<a class=\"button\" href=\"#\">BOOK</a><a class=\"button button2\" href=\"#\">INTERVIEW</a>\n				<p><a href=\"#\">ADD TO SITTER TEAM</a></p>\n				<p><a href=\"#\">BOOKMARK</a></p>\n			  </div>\n			</li>\n		  </ul>\n		</div>\n	  </section>\n	  <!-- /my_friends_sitters -->\n\n	  <!-- my_local_sitters -->\n	  <section id=\"tab-3\">\n		<div class=\"mob_tab_trigger my_mob_tab\">local<br />sitters<span>519</span></div>\n		<div class=\"friends_block my_local_sitters\">\n		  <div class=\"sitter_title\">\n			<p><span><span class=\"icon_pin2\">&nbsp;</span>local<br />sitters</span><strong>519</strong></p>\n		  </div>\n		  <ul class=\"clear\">\n			<li>\n			  <div class=\"bookmark\"></div>\n			  <div class=\"tit\">\n				<span><strong>$15</strong> /hr</span>\n				<a href=\"#\">Amelia Hart</a>\n			  </div>\n			  <div class=\"img\">\n				<div class=\"heart\"></div>\n				<a href=\"#\"><img src=\"/static/images/demo/img13.jpg\" alt=\"\" /></a>\n				<span>Background Cleared</span>\n			  </div>\n			  <ul>\n				<li><span class=\"icon_recommend2\">&nbsp;</span>4 recommends\n				<ul>\n				  <li>Recommendations</li>\n				  <li><a href=\"#\"><img src=\"/static/images/demo/img3.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n				  <li><a href=\"#\"><img src=\"/static/images/demo/img4.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n				  <li><a href=\"#\"><img src=\"/static/images/demo/img5.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n				  <li><a href=\"#\"><img src=\"/static/images/demo/img6.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n				  <li><a href=\"#\"><img src=\"/static/images/demo/img7.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n				  <li><a href=\"#\"><img src=\"/static/images/demo/img8.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n				  <li><a href=\"#\"><img src=\"/static/images/demo/img9.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n				  <li><a href=\"#\"><img src=\"/static/images/demo/img10.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n				</ul>\n				</li>\n				<li><span class=\"icon_team3\">&nbsp;</span>9 sitter teams\n				<ul>\n				  <li>Added to sitter teams and repeatedly hired</li>\n				  <li><a href=\"#\"><img src=\"/static/images/demo/img3.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n				  <li><a href=\"#\"><img src=\"/static/images/demo/img4.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n				  <li><a href=\"#\"><img src=\"/static/images/demo/img5.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n				  <li><a href=\"#\"><img src=\"/static/images/demo/img6.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n				  <li><a href=\"#\"><img src=\"/static/images/demo/img7.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n				  <li><a href=\"#\"><img src=\"/static/images/demo/img8.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n				  <li><a href=\"#\"><img src=\"/static/images/demo/img9.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n				  <li><a href=\"#\"><img src=\"/static/images/demo/img10.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n				</ul>\n				</li>\n				<li><span class=\"icon_reviews\">&nbsp;</span>11 reviews\n				<ul>\n				  <li class=\"rev clear\">\n					<a href=\"#\"><img src=\"/static/images/demo/img3.jpg\" alt=\"\" /></a>\n					<div>\n					  <p>Ellen has been a sitter for my children fore more than a year and I couldn’t be happier! She arrives on time and my kids light up when they see her!</p>\n					  <p><a href=\"#\">Read more reviews </a></p>\n					</div>\n				  </li>\n				</ul>\n				</li>\n			  </ul>\n			  <div class=\"btns clear\">\n				<div class=\"select_wrap\"><input type=\"checkbox\" class=\"select5\" id=\"select5\" /><label for=\"select5\">Select</label></div>\n				<a class=\"button\" href=\"#\">BOOK</a><a class=\"button button2\" href=\"#\">INTERVIEW</a>\n				<p><a href=\"#\">ADD TO SITTER TEAM</a></p>\n				<p><a href=\"#\">BOOKMARK</a></p>\n			  </div>\n			</li>\n			<li>\n			  <div class=\"bookmark\"></div>\n			  <div class=\"tit\">\n				<span><strong>$15</strong> /hr</span>\n				<a href=\"#\">Dora Cruz</a>\n			  </div>\n			  <div class=\"img\">\n				<div class=\"heart\"></div>\n				<a href=\"#\"><img src=\"/static/images/demo/img13.jpg\" alt=\"\" /></a>\n				<span>Background Cleared</span>\n			  </div>\n			  <ul>\n				<li><span class=\"icon_recommend2\">&nbsp;</span>4 recommends\n				<ul>\n				  <li>Recommendations</li>\n				  <li><a href=\"#\"><img src=\"/static/images/demo/img3.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n				  <li><a href=\"#\"><img src=\"/static/images/demo/img4.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n				  <li><a href=\"#\"><img src=\"/static/images/demo/img5.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n				  <li><a href=\"#\"><img src=\"/static/images/demo/img6.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n				  <li><a href=\"#\"><img src=\"/static/images/demo/img7.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n				  <li><a href=\"#\"><img src=\"/static/images/demo/img8.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n				  <li><a href=\"#\"><img src=\"/static/images/demo/img9.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n				  <li><a href=\"#\"><img src=\"/static/images/demo/img10.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n				</ul>\n				</li>\n				<li><span class=\"icon_team3\">&nbsp;</span>9 sitter teams\n				<ul>\n				  <li>Added to sitter teams and repeatedly hired</li>\n				  <li><a href=\"#\"><img src=\"/static/images/demo/img3.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n				  <li><a href=\"#\"><img src=\"/static/images/demo/img4.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n				  <li><a href=\"#\"><img src=\"/static/images/demo/img5.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n				  <li><a href=\"#\"><img src=\"/static/images/demo/img6.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n				  <li><a href=\"#\"><img src=\"/static/images/demo/img7.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n				  <li><a href=\"#\"><img src=\"/static/images/demo/img8.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n				  <li><a href=\"#\"><img src=\"/static/images/demo/img9.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n				  <li><a href=\"#\"><img src=\"/static/images/demo/img10.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n				</ul>\n				</li>\n				<li><span class=\"icon_reviews\">&nbsp;</span>11 reviews\n				<ul>\n				  <li class=\"rev clear\">\n					<a href=\"#\"><img src=\"/static/images/demo/img3.jpg\" alt=\"\" /></a>\n					<div>\n					  <p>Ellen has been a sitter for my children fore more than a year and I couldn’t be happier! She arrives on time and my kids light up when they see her!</p>\n					  <p><a href=\"#\">Read more reviews </a></p>\n					</div>\n				  </li>\n				</ul>\n				</li>\n			  </ul>\n			  <div class=\"btns clear\">\n				<div class=\"select_wrap\"><input type=\"checkbox\" class=\"select6\" id=\"select6\" /><label for=\"select6\">Select</label></div>\n				<a class=\"button\" href=\"#\">BOOK</a><a class=\"button button2\" href=\"#\">INTERVIEW</a>\n				<p><a href=\"#\">ADD TO SITTER TEAM</a></p>\n				<p><a href=\"#\">BOOKMARK</a></p>\n			  </div>\n			</li>\n			<li>\n			  <div class=\"bookmark\"></div>\n			  <div class=\"tit\">\n				<span><strong>$15</strong> /hr</span>\n				<a href=\"#\">Jane Wayne</a>\n			  </div>\n			  <div class=\"img\">\n				<div class=\"heart\"></div>\n				<a href=\"#\"><img src=\"/static/images/demo/img13.jpg\" alt=\"\" /></a>\n				<span>Background Cleared</span>\n			  </div>\n			  <ul>\n				<li><span class=\"icon_recommend2\">&nbsp;</span>4 recommends\n				<ul>\n				  <li>Recommendations</li>\n				  <li><a href=\"#\"><img src=\"/static/images/demo/img3.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n				  <li><a href=\"#\"><img src=\"/static/images/demo/img4.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n				  <li><a href=\"#\"><img src=\"/static/images/demo/img5.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n				  <li><a href=\"#\"><img src=\"/static/images/demo/img6.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n				  <li><a href=\"#\"><img src=\"/static/images/demo/img7.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n				  <li><a href=\"#\"><img src=\"/static/images/demo/img8.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n				  <li><a href=\"#\"><img src=\"/static/images/demo/img9.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n				  <li><a href=\"#\"><img src=\"/static/images/demo/img10.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n				</ul>\n				</li>\n				<li><span class=\"icon_team3\">&nbsp;</span>9 sitter teams\n				<ul>\n				  <li>Added to sitter teams and repeatedly hired</li>\n				  <li><a href=\"#\"><img src=\"/static/images/demo/img3.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n				  <li><a href=\"#\"><img src=\"/static/images/demo/img4.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n				  <li><a href=\"#\"><img src=\"/static/images/demo/img5.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n				  <li><a href=\"#\"><img src=\"/static/images/demo/img6.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n				  <li><a href=\"#\"><img src=\"/static/images/demo/img7.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n				  <li><a href=\"#\"><img src=\"/static/images/demo/img8.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n				  <li><a href=\"#\"><img src=\"/static/images/demo/img9.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n				  <li><a href=\"#\"><img src=\"/static/images/demo/img10.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n				</ul>\n				</li>\n				<li><span class=\"icon_reviews\">&nbsp;</span>11 reviews\n				<ul>\n				  <li class=\"rev clear\">\n					<a href=\"#\"><img src=\"/static/images/demo/img3.jpg\" alt=\"\" /></a>\n					<div>\n					  <p>Ellen has been a sitter for my children fore more than a year and I couldn’t be happier! She arrives on time and my kids light up when they see her!</p>\n					  <p><a href=\"#\">Read more reviews </a></p>\n					</div>\n				  </li>\n				</ul>\n				</li>\n			  </ul>\n			  <div class=\"btns clear\">\n				<div class=\"select_wrap\"><input type=\"checkbox\" class=\"select7\" id=\"select7\" /><label for=\"select7\">Select</label></div>\n				<a class=\"button\" href=\"#\">BOOK</a><a class=\"button button2\" href=\"#\">INTERVIEW</a>\n				<p><a href=\"#\">ADD TO SITTER TEAM</a></p>\n				<p><a href=\"#\">BOOKMARK</a></p>\n			  </div>\n			</li>\n			<li>\n			  <div class=\"bookmark\"></div>\n			  <div class=\"tit\">\n				<span><strong>$15</strong> /hr</span>\n				<a href=\"#\">Ellen Vukelich</a>\n			  </div>\n			  <div class=\"img\">\n				<div class=\"heart\"></div>\n				<a href=\"#\"><img src=\"/static/images/demo/img13.jpg\" alt=\"\" /></a>\n				<span>Background Cleared</span>\n			  </div>\n			  <ul>\n				<li><span class=\"icon_recommend2\">&nbsp;</span>4 recommends\n				<ul>\n				  <li>Recommendations</li>\n				  <li><a href=\"#\"><img src=\"/static/images/demo/img3.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n				  <li><a href=\"#\"><img src=\"/static/images/demo/img4.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n				  <li><a href=\"#\"><img src=\"/static/images/demo/img5.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n				  <li><a href=\"#\"><img src=\"/static/images/demo/img6.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n				  <li><a href=\"#\"><img src=\"/static/images/demo/img7.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n				  <li><a href=\"#\"><img src=\"/static/images/demo/img8.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n				  <li><a href=\"#\"><img src=\"/static/images/demo/img9.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n				  <li><a href=\"#\"><img src=\"/static/images/demo/img10.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n				</ul>\n				</li>\n				<li><span class=\"icon_team3\">&nbsp;</span>9 sitter teams\n				<ul>\n				  <li>Added to sitter teams and repeatedly hired</li>\n				  <li><a href=\"#\"><img src=\"/static/images/demo/img3.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n				  <li><a href=\"#\"><img src=\"/static/images/demo/img4.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n				  <li><a href=\"#\"><img src=\"/static/images/demo/img5.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n				  <li><a href=\"#\"><img src=\"/static/images/demo/img6.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n				  <li><a href=\"#\"><img src=\"/static/images/demo/img7.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n				  <li><a href=\"#\"><img src=\"/static/images/demo/img8.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n				  <li><a href=\"#\"><img src=\"/static/images/demo/img9.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n				  <li><a href=\"#\"><img src=\"/static/images/demo/img10.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n				</ul>\n				</li>\n				<li><span class=\"icon_reviews\">&nbsp;</span>11 reviews\n				<ul>\n				  <li class=\"rev clear\">\n					<a href=\"#\"><img src=\"/static/images/demo/img3.jpg\" alt=\"\" /></a>\n					<div>\n					  <p>Ellen has been a sitter for my children fore more than a year and I couldn’t be happier! She arrives on time and my kids light up when they see her!</p>\n					  <p><a href=\"#\">Read more reviews </a></p>\n					</div>\n				  </li>\n				</ul>\n				</li>\n			  </ul>\n			  <div class=\"btns clear\">\n				<div class=\"select_wrap\"><input type=\"checkbox\" class=\"select8\" id=\"select8\" /><label for=\"select8\">Select</label></div>\n				<a class=\"button\" href=\"#\">BOOK</a><a class=\"button button2\" href=\"#\">INTERVIEW</a>\n				<p><a href=\"#\">ADD TO SITTER TEAM</a></p>\n				<p><a href=\"#\">BOOKMARK</a></p>\n			  </div>\n			</li>\n		  </ul>\n		</div>\n	  </section>\n	  <!-- /my_local_sitters -->\n\n	</div>\n	<!-- /sitter_tabs_wrap -->\n\n  </div>\n</div>");
  
});
Ember.TEMPLATES["search/top"] = Ember.Handlebars.template(function anonymous(Handlebars,depth0,helpers,partials,data) {
this.compilerInfo = [3,'>= 1.0.0-rc.4'];
helpers = helpers || Ember.Handlebars.helpers; data = data || {};
  


  data.buffer.push("<!-- /top note -->\n<a href=\"#\" class=\"back\">Back to search results</a>\n<!-- top info -->\n<div class=\"top_info clear\">\n  <div class=\"find_form_block\">\n    <p>Where and when do you need your sitter?</p>\n    <form method=\"post\" action=\"#\">\n      <ul class=\"clear\">\n        <li>\n          <label for=\"where\">Where</label>\n          <input id=\"where\" type=\"text\" value=\"Enter town or zipcode\" />\n        </li>\n        <li>\n          <label for=\"when\">When</label>\n          <input type=\"text\" class=\"datepicker\" id=\"datepicker\" value=\"Choose date\" />\n          <p><input type=\"checkbox\" id=\"check\" name=\"check\" /><label for=\"check\">Overnight / Multiday booking?</label></p>\n        </li>\n        <li>\n          <label for=\"from\">From</label>\n          <select id=\"from\" data-placeholder=\"\" tabindex=\"8\"><option>6:00 PM</option><option>7:00 PM</option></select>\n        </li>\n        <li>\n          <label for=\"to\">To</label>\n          <select id=\"to\" data-placeholder=\"\" tabindex=\"9\"><option>11:00 PM</option><option>12:00 PM</option></select>\n        </li>\n        <li>\n          <label>&nbsp;</label>\n          <select data-placeholder=\"\" tabindex=\"10\"><option>2 Kids</option><option>3 Kids</option></select>\n        </li>\n        <li class=\"clear_pad over_form\">\n          <label>To</label>\n          <input type=\"text\" class=\"datepicker\" id=\"datepicker3\" value=\"Choose date\" />\n        </li>\n        <li class=\"over_form\">\n          <label>&nbsp;</label>\n          <select id=\"to2\" data-placeholder=\"\" tabindex=\"92\"><option>11:00 PM</option><option>12:00 PM</option></select>\n        </li>\n        <li><input type=\"submit\" value=\"FIND MY SITTER\" /></li>\n      </ul>\n    </form>\n    <p class=\"hide\"><a href=\"#\">Hide Search Bar</a></p>\n    <p class=\"show\"><a href=\"#\">Show Search Bar</a></p>\n  </div>\n</div>");
  
});
Ember.TEMPLATES["book/top"] = Ember.Handlebars.template(function anonymous(Handlebars,depth0,helpers,partials,data) {
this.compilerInfo = [3,'>= 1.0.0-rc.4'];
helpers = helpers || Ember.Handlebars.helpers; data = data || {};
  var buffer = '', stack1, stack2, hashContexts, hashTypes, options, self=this, helperMissing=helpers.helperMissing, escapeExpression=this.escapeExpression;

function program1(depth0,data) {
  
  
  data.buffer.push("Back to search results");
  }

  hashContexts = {'class': depth0};
  hashTypes = {'class': "STRING"};
  options = {hash:{
    'class': ("back")
  },inverse:self.noop,fn:self.program(1, program1, data),contexts:[depth0],types:["ID"],hashContexts:hashContexts,hashTypes:hashTypes,data:data};
  stack2 = ((stack1 = helpers.linkTo),stack1 ? stack1.call(depth0, "search", options) : helperMissing.call(depth0, "linkTo", "search", options));
  if(stack2 || stack2 === 0) { data.buffer.push(stack2); }
  data.buffer.push("\n<!-- top note form -->\n<div class=\"top_note_form clear\">\n  <div class=\"add_note\"><span class=\"icon_note\">&nbsp;</span>Add a note</div>\n  <textarea></textarea>\n  <p>\n    <span>If everything looks good below, send away!</span>\n    <a class=\"button button_small button_cancel\" ");
  hashTypes = {};
  hashContexts = {};
  data.buffer.push(escapeExpression(helpers.action.call(depth0, "cancel", {hash:{},contexts:[depth0],types:["STRING"],hashContexts:hashContexts,hashTypes:hashTypes,data:data})));
  data.buffer.push(">\n      <span class=\"icon_cancel\">&nbsp;</span>\n      CANCEL\n    </a>\n    <a class=\"button button_small\" ");
  hashTypes = {};
  hashContexts = {};
  data.buffer.push(escapeExpression(helpers.action.call(depth0, "book", {hash:{},contexts:[depth0],types:["STRING"],hashContexts:hashContexts,hashTypes:hashTypes,data:data})));
  data.buffer.push(">\n      <span class=\"icon_ok2\">&nbsp;</span>\n      SEND\n    </a>\n  </p>\n</div>\n<!-- /top note form -->\n<!-- top_personal_info -->\n<div id=\"fixed_tabs\">\n  <div class=\"top_personal_info clear\">\n	<div class=\"img_name\">\n	  <img src=\"/static/images/demo/img14.jpg\" alt=\"\" />\n	  <span>Book Ellen</span>\n	</div>\n	<ul>\n	  <li><span class=\"icon_date\">&nbsp;</span>Wednesday 1 August 2012 &nbsp; <span>4:00 pm — 6:00 pm</span></li>\n	  <li><span class=\"icon_friends5\">&nbsp;</span>2 Kids</li>\n	  <li><span class=\"icon_pin3\">&nbsp;</span>33 Nassau Ave Suite #2 NY, New York</li>\n	  <li><span class=\"icon_phone\">&nbsp;</span>1258 986 89</li>\n	</ul>\n  </div>\n</div>");
  return buffer;
  
});
Ember.TEMPLATES["book"] = Ember.Handlebars.template(function anonymous(Handlebars,depth0,helpers,partials,data) {
this.compilerInfo = [3,'>= 1.0.0-rc.4'];
helpers = helpers || Ember.Handlebars.helpers; data = data || {};
  var buffer = '', hashTypes, hashContexts, escapeExpression=this.escapeExpression;


  data.buffer.push("<div class=\"container clear\">\n  <div class=\"wraper\">\n\n	<!-- parent_book_block -->\n	<form action=\"#\" method=\"post\" class=\"form_style\">\n	  <div class=\"parent_book_block clear\">\n		<ul>\n		  <li><div><span class=\"icon_date2\">&nbsp;</span>Schedule</div>\n		  <ul>\n			<li><span class=\"icon_date2\">&nbsp;</span>Schedule</li>\n			<li><p><input type=\"text\" class=\"datepicker\" id=\"datepicker\" /></p></li>\n			<li>\n			  <p><label for=\"from\">FROM</label><select id=\"from\" data-placeholder=\"\" tabindex=\"8\"><option>6:00 PM</option><option>7:00 PM</option></select></p>\n			  <p><label for=\"to\">TO</label><select id=\"to\" data-placeholder=\"\" tabindex=\"9\"><option>11:00 PM</option><option>12:00 PM</option></select></p>\n			  <p><input type=\"checkbox\" id=\"check\" /><label for=\"check\">Overnight/Multiday booking</label></p>\n			</li>\n			<li>&nbsp;</li>\n		  </ul>\n		  </li>\n		  <li class=\"lng\"><div><span class=\"icon_pin4\">&nbsp;</span>Location</div>\n		  <ul>\n			<li><span class=\"icon_pin4\">&nbsp;</span>Location</li>\n			<li>\n			  <p><input type=\"text\" value=\"33 Nassau Ave\" /> <input type=\"text\" value=\"Suite#2\" class=\"small\" /></p>\n			  <p><input type=\"text\" value=\"10007\" class=\"small\" /> <select data-placeholder=\"Hoboken\" tabindex=\"1\"><option>Hoboken</option><option>Hoboken</option></select> <select class=\"small\" data-placeholder=\"NJ\" tabindex=\"2\"><option>NJ</option><option>NJ</option></select></p>\n			</li>\n			<li>&nbsp;</li>\n		  </ul>\n		  </li>\n		  <li><div><span class=\"icon_friends6\">&nbsp;</span># of kids</div>\n		  <ul>\n			<li><span class=\"icon_friends6\">&nbsp;</span>Number of kids</li>\n			<li><p><select data-placeholder=\"\" tabindex=\"10\"><option>2 Kids</option><option>3 Kids</option></select></p></li>\n			<li>&nbsp;</li>\n			<li>&nbsp;</li>\n		  </ul>\n		  </li>\n		  <li class=\"lng\"><div><span class=\"icon_phone2\">&nbsp;</span>Emergency Contact</div>\n		  <ul>\n			<li><span class=\"icon_phone2\">&nbsp;</span>Emergency Contact</li>\n			<li><p><input type=\"text\" value=\"(123)\" class=\"small\" /> <input type=\"text\" value=\"456-7890\" /></p></li>\n			<li>&nbsp;</li>\n		  </ul>\n		  </li>\n		</ul>\n		<p>\n          <a class=\"button button_small button_cancel\" ");
  hashTypes = {};
  hashContexts = {};
  data.buffer.push(escapeExpression(helpers.action.call(depth0, "cancel", {hash:{},contexts:[depth0],types:["STRING"],hashContexts:hashContexts,hashTypes:hashTypes,data:data})));
  data.buffer.push(">\n            <span class=\"icon_cancel\">&nbsp;</span>\n            CANCEL\n          </a>\n          <a class=\"button button_small\" ");
  hashTypes = {};
  hashContexts = {};
  data.buffer.push(escapeExpression(helpers.action.call(depth0, "book", {hash:{},contexts:[depth0],types:["STRING"],hashContexts:hashContexts,hashTypes:hashTypes,data:data})));
  data.buffer.push(">\n            <span class=\"icon_ok2\">&nbsp;</span>\n            SEND\n          </a>\n        </p>\n	  </div>\n	</form>\n	<!-- /parent_book_block -->\n  </div>\n</div>");
  return buffer;
  
});
Ember.TEMPLATES["book/multiple"] = Ember.Handlebars.template(function anonymous(Handlebars,depth0,helpers,partials,data) {
this.compilerInfo = [3,'>= 1.0.0-rc.4'];
helpers = helpers || Ember.Handlebars.helpers; data = data || {};
  


  data.buffer.push("<div class=\"container clear\">\n  <div class=\"wraper\">\n\n	<!-- parent_book_block -->\n	<form action=\"#\" method=\"post\" class=\"form_style\">\n	  <div class=\"parent_book_block clear\">\n		<ul>\n		  <li><div><span class=\"icon_heart\">&nbsp;</span>Recipients</div>\n		  <ul>\n			<li><span class=\"icon_heart\">&nbsp;</span>Recipients</li>\n			<li><select data-placeholder=\"Names\" multiple tabindex=\"1\"><option>Ellen Vukelich</option><option>Sandy Thompson</option><option>Amy Randall</option><option>Amelia Hart</option><option>Erica Sanders</option></select></li>\n			<li>&nbsp;</li>\n		  </ul>\n		  </li>\n		  <li><div><span class=\"icon_date2\">&nbsp;</span>Schedule</div>\n		  <ul>\n			<li><span class=\"icon_date2\">&nbsp;</span>Schedule</li>\n			<li><p><input type=\"text\" class=\"datepicker\" id=\"datepicker\" /></p></li>\n			<li>\n			  <p><label for=\"from\">FROM</label><select id=\"from\" data-placeholder=\"\" tabindex=\"8\"><option>6:00 PM</option><option>7:00 PM</option></select></p>\n			  <p><label for=\"to\">TO</label><select id=\"to\" data-placeholder=\"\" tabindex=\"9\"><option>11:00 PM</option><option>12:00 PM</option></select></p>\n			  <p><input type=\"checkbox\" id=\"check\" /><label for=\"check\">Overnight/Multiday booking</label></p>\n			</li>\n			<li>&nbsp;</li>\n		  </ul>\n		  </li>\n		  <li class=\"lng\"><div><span class=\"icon_pin4\">&nbsp;</span>Location</div>\n		  <ul>\n			<li><span class=\"icon_pin4\">&nbsp;</span>Location</li>\n			<li>\n			  <p><input type=\"text\" value=\"33 Nassau Ave\" /> <input type=\"text\" value=\"Suite#2\" class=\"small\" /></p>\n			  <p><input type=\"text\" value=\"10007\" class=\"small\" /> <select data-placeholder=\"Hoboken\" tabindex=\"1\"><option>Hoboken</option><option>Hoboken</option></select> <select class=\"small\" data-placeholder=\"NJ\" tabindex=\"2\"><option>NJ</option><option>NJ</option></select></p>\n			</li>\n			<li>&nbsp;</li>\n		  </ul>\n		  </li>\n		  <li><div><span class=\"icon_friends6\">&nbsp;</span># of kids</div>\n		  <ul>\n			<li><span class=\"icon_friends6\">&nbsp;</span>Number of kids</li>\n			<li><p><select data-placeholder=\"\" tabindex=\"10\"><option>2 Kids</option><option>3 Kids</option></select></p></li>\n			<li>&nbsp;</li>\n			<li>&nbsp;</li>\n		  </ul>\n		  </li>\n		  <li class=\"lng\"><div><span class=\"icon_phone2\">&nbsp;</span>Emergency Contact</div>\n		  <ul>\n			<li><span class=\"icon_phone2\">&nbsp;</span>Emergency Contact</li>\n			<li><p><input type=\"text\" value=\"(123)\" class=\"small\" /> <input type=\"text\" value=\"456-7890\" /></p></li>\n			<li>&nbsp;</li>\n		  </ul>\n		  </li>\n		</ul>\n		<p><a class=\"button button_small button_cancel\" href=\"#\"><span class=\"icon_cancel\">&nbsp;</span>CANCEL</a><a class=\"button button_small\" href=\"#\"><span class=\"icon_ok2\">&nbsp;</span>SEND</a></p>\n	  </div>\n	</form>\n	<!-- /parent_book_block -->\n\n  </div>\n</div>");
  
});
Ember.TEMPLATES["sitterEdit/network"] = Ember.Handlebars.template(function anonymous(Handlebars,depth0,helpers,partials,data) {
this.compilerInfo = [3,'>= 1.0.0-rc.4'];
helpers = helpers || Ember.Handlebars.helpers; data = data || {};
  var buffer = '', stack1, hashContexts, hashTypes, escapeExpression=this.escapeExpression, self=this, helperMissing=helpers.helperMissing, functionType="function", blockHelperMissing=helpers.blockHelperMissing;

function program1(depth0,data) {
  
  var buffer = '', stack1, stack2, hashTypes, hashContexts, options;
  data.buffer.push("\n		        <li>");
  hashTypes = {};
  hashContexts = {};
  options = {hash:{},inverse:self.noop,fn:self.program(2, program2, data),contexts:[depth0,depth0],types:["ID","ID"],hashContexts:hashContexts,hashTypes:hashTypes,data:data};
  stack2 = ((stack1 = helpers.linkTo),stack1 ? stack1.call(depth0, "parent", "", options) : helperMissing.call(depth0, "linkTo", "parent", "", options));
  if(stack2 || stack2 === 0) { data.buffer.push(stack2); }
  data.buffer.push("</li>\n              ");
  return buffer;
  }
function program2(depth0,data) {
  
  var buffer = '', hashTypes, hashContexts;
  data.buffer.push("<img src=\"/static/images/demo/img15.jpg\" alt=\"\" />");
  hashTypes = {};
  hashContexts = {};
  data.buffer.push(escapeExpression(helpers._triageMustache.call(depth0, "full_name", {hash:{},contexts:[depth0],types:["ID"],hashContexts:hashContexts,hashTypes:hashTypes,data:data})));
  return buffer;
  }

function program4(depth0,data) {
  
  var buffer = '', stack1, stack2, hashTypes, hashContexts, options;
  data.buffer.push("\n		        <li>");
  hashTypes = {};
  hashContexts = {};
  options = {hash:{},inverse:self.noop,fn:self.program(2, program2, data),contexts:[depth0,depth0],types:["ID","ID"],hashContexts:hashContexts,hashTypes:hashTypes,data:data};
  stack2 = ((stack1 = helpers.linkTo),stack1 ? stack1.call(depth0, "sitter", "", options) : helperMissing.call(depth0, "linkTo", "sitter", "", options));
  if(stack2 || stack2 === 0) { data.buffer.push(stack2); }
  data.buffer.push("</li>\n              ");
  return buffer;
  }

function program6(depth0,data) {
  
  var buffer = '', stack1, options, hashTypes, hashContexts;
  data.buffer.push("\n		        <li>");
  options = {hash:{},inverse:self.noop,fn:self.program(7, program7, data),contexts:[],types:[],hashContexts:hashContexts,hashTypes:hashTypes,data:data};
  if (stack1 = helpers.linkTo) { stack1 = stack1.call(depth0, options); }
  else { stack1 = depth0.linkTo; stack1 = typeof stack1 === functionType ? stack1.apply(depth0) : stack1; }
  hashTypes = {};
  hashContexts = {};
  if (!helpers.linkTo) { stack1 = blockHelperMissing.call(depth0, stack1, options); }
  if(stack1 || stack1 === 0) { data.buffer.push(stack1); }
  data.buffer.push("</li><a ");
  hashTypes = {};
  hashContexts = {};
  data.buffer.push(escapeExpression(helpers.action.call(depth0, "deleteGroup", "", {hash:{},contexts:[depth0,depth0],types:["ID","ID"],hashContexts:hashContexts,hashTypes:hashTypes,data:data})));
  data.buffer.push(" class=\"delete\">&nbsp;</a>\n              ");
  return buffer;
  }
function program7(depth0,data) {
  
  var buffer = '', hashTypes, hashContexts;
  data.buffer.push("<img src=\"/static/images/demo/img15.jpg\" alt=\"\" />");
  hashTypes = {};
  hashContexts = {};
  data.buffer.push(escapeExpression(helpers._triageMustache.call(depth0, "name", {hash:{},contexts:[depth0],types:["ID"],hashContexts:hashContexts,hashTypes:hashTypes,data:data})));
  return buffer;
  }

  data.buffer.push("	  <!-- network_block -->\n	  <div class=\"mob_tab_trigger\">Network</div>\n	  <div class=\"tab_content network_block\" id=\"tab-4\">\n		<div class=\"soc_list clear\">\n		  <p>Find people you know on Sitterfied</p>\n		  <ul>\n			<li>\n			  <p class=\"clear\">\n                <a ");
  hashContexts = {'bubbles': depth0};
  hashTypes = {'bubbles': "BOOLEAN"};
  data.buffer.push(escapeExpression(helpers.action.call(depth0, "facebookConnect", {hash:{
    'bubbles': (false)
  },contexts:[depth0],types:["ID"],hashContexts:hashContexts,hashTypes:hashTypes,data:data})));
  data.buffer.push(">\n                    <img src=\"/static/images/icons/facebook.png\" alt=\"\" />Facebook\n                </a>\n                <a href=\"#\">\n                  <img src=\"/static/images/icons/gmail.png\" alt=\"\" />Gmail\n                </a>\n              </p>\n			  <p>Connect</p>\n			</li>\n			<li>\n			  <p><input type=\"text\" value=\"Search a person or group\" /><input type=\"submit\" value=\"ADD\" /></p>\n			  <p>Search</p>\n			</li>\n			<li>\n			  <p><a href=\"#\">Invite Your Friends</a></p>\n			  <p>Invite</p>\n			</li>\n		  </ul>\n		</div>\n		<ul class=\"soc_psg_list clear\">\n		  <li>\n			<ul>\n			  <li>Parents</li>\n              ");
  hashTypes = {};
  hashContexts = {};
  stack1 = helpers.each.call(depth0, "parents_in_network", {hash:{},inverse:self.noop,fn:self.program(1, program1, data),contexts:[depth0],types:["ID"],hashContexts:hashContexts,hashTypes:hashTypes,data:data});
  if(stack1 || stack1 === 0) { data.buffer.push(stack1); }
  data.buffer.push("\n			</ul>\n		  </li>\n		  <li>\n			<ul>\n			  <li>Sitters</li>\n              ");
  hashTypes = {};
  hashContexts = {};
  stack1 = helpers.each.call(depth0, "sitter_in_network", {hash:{},inverse:self.noop,fn:self.program(4, program4, data),contexts:[depth0],types:["ID"],hashContexts:hashContexts,hashTypes:hashTypes,data:data});
  if(stack1 || stack1 === 0) { data.buffer.push(stack1); }
  data.buffer.push("\n			</ul>\n		  </li>\n		  <li>\n			<ul>\n			  <li>Groups</li>\n              ");
  hashTypes = {};
  hashContexts = {};
  stack1 = helpers.each.call(depth0, "sitter_groups", {hash:{},inverse:self.noop,fn:self.program(6, program6, data),contexts:[depth0],types:["ID"],hashContexts:hashContexts,hashTypes:hashTypes,data:data});
  if(stack1 || stack1 === 0) { data.buffer.push(stack1); }
  data.buffer.push("\n			</ul>\n		  </li>\n		</ul>\n	  </div>\n	  <!-- /network_block -->\n");
  return buffer;
  
});
Ember.TEMPLATES["sitterEdit/schedlue"] = Ember.Handlebars.template(function anonymous(Handlebars,depth0,helpers,partials,data) {
this.compilerInfo = [3,'>= 1.0.0-rc.4'];
helpers = helpers || Ember.Handlebars.helpers; data = data || {};
  var buffer = '', hashTypes, hashContexts, escapeExpression=this.escapeExpression;


  data.buffer.push("	  <!-- schedule_block -->\n	  <div class=\"mob_tab_trigger\">Schedule</div>\n	  <div class=\"tab_content schedule_block\" id=\"tab-2\">\n		<p>Please indicate your typical availability here.\n          <span>\n            <img src=\"/static/images/available.jpg\" alt=\"\" />Available\n            <img src=\"/static/images/unavailable.jpg\" alt=\"\" />Unavailable\n          </span>\n          <a class=\"button button_small\" ");
  hashTypes = {};
  hashContexts = {};
  data.buffer.push(escapeExpression(helpers.action.call(depth0, "saveSchedlue", {hash:{},contexts:[depth0],types:["STRING"],hashContexts:hashContexts,hashTypes:hashTypes,data:data})));
  data.buffer.push("><span class=\"icon_ok2\">&nbsp;</span>Save</a></p>\n		<ul>\n		  <li>\n			<ul>\n			  <li><a ");
  hashTypes = {};
  hashContexts = {};
  data.buffer.push(escapeExpression(helpers.action.call(depth0, "checkAll", {hash:{},contexts:[depth0],types:["STRING"],hashContexts:hashContexts,hashTypes:hashTypes,data:data})));
  data.buffer.push(">Check All</a> | <a ");
  hashTypes = {};
  hashContexts = {};
  data.buffer.push(escapeExpression(helpers.action.call(depth0, "clearAll", {hash:{},contexts:[depth0],types:["STRING"],hashContexts:hashContexts,hashTypes:hashTypes,data:data})));
  data.buffer.push(">Clear All</a></li>\n			  <li>Sun</li>\n			  <li>Mon</li>\n			  <li>Tues</li>\n			  <li>Wed</li>\n			  <li>Thurs</li>\n			  <li>Fri</li>\n			  <li>Sat</li>\n			</ul>\n		  </li>\n		  <li>\n			<ul>\n			  <li><strong>Early Morning</strong> (6am - 9am)<span>6 - 9 AM</span></li>\n			  <li>");
  hashContexts = {'checkedBinding': depth0,'id': depth0};
  hashTypes = {'checkedBinding': "STRING",'id': "STRING"};
  data.buffer.push(escapeExpression(helpers.view.call(depth0, "Ember.Checkbox", {hash:{
    'checkedBinding': ("sun_early_morning"),
    'id': ("sun_1")
  },contexts:[depth0],types:["ID"],hashContexts:hashContexts,hashTypes:hashTypes,data:data})));
  data.buffer.push("<label for=\"sun_1\">&nbsp;</label></li>\n			  <li>");
  hashContexts = {'checkedBinding': depth0,'id': depth0};
  hashTypes = {'checkedBinding': "STRING",'id': "STRING"};
  data.buffer.push(escapeExpression(helpers.view.call(depth0, "Ember.Checkbox", {hash:{
    'checkedBinding': ("mon_early_morning"),
    'id': ("mon_1")
  },contexts:[depth0],types:["ID"],hashContexts:hashContexts,hashTypes:hashTypes,data:data})));
  data.buffer.push("<label for=\"mon_1\">&nbsp;</label></li>\n			  <li>");
  hashContexts = {'checkedBinding': depth0,'id': depth0};
  hashTypes = {'checkedBinding': "STRING",'id': "STRING"};
  data.buffer.push(escapeExpression(helpers.view.call(depth0, "Ember.Checkbox", {hash:{
    'checkedBinding': ("tues_early_morning"),
    'id': ("tues_1")
  },contexts:[depth0],types:["ID"],hashContexts:hashContexts,hashTypes:hashTypes,data:data})));
  data.buffer.push("<label for=\"tues_1\">&nbsp;</label></li>\n			  <li>");
  hashContexts = {'checkedBinding': depth0,'id': depth0};
  hashTypes = {'checkedBinding': "STRING",'id': "STRING"};
  data.buffer.push(escapeExpression(helpers.view.call(depth0, "Ember.Checkbox", {hash:{
    'checkedBinding': ("wed_early_morning"),
    'id': ("wed_1")
  },contexts:[depth0],types:["ID"],hashContexts:hashContexts,hashTypes:hashTypes,data:data})));
  data.buffer.push("<label for=\"wed_1\">&nbsp;</label></li>\n			  <li>");
  hashContexts = {'checkedBinding': depth0,'id': depth0};
  hashTypes = {'checkedBinding': "STRING",'id': "STRING"};
  data.buffer.push(escapeExpression(helpers.view.call(depth0, "Ember.Checkbox", {hash:{
    'checkedBinding': ("thurs_early_morning"),
    'id': ("thurs_1")
  },contexts:[depth0],types:["ID"],hashContexts:hashContexts,hashTypes:hashTypes,data:data})));
  data.buffer.push("<label for=\"thurs_1\">&nbsp;</label></li>\n			  <li>");
  hashContexts = {'checkedBinding': depth0,'id': depth0};
  hashTypes = {'checkedBinding': "STRING",'id': "STRING"};
  data.buffer.push(escapeExpression(helpers.view.call(depth0, "Ember.Checkbox", {hash:{
    'checkedBinding': ("fri_early_morning"),
    'id': ("fri_1")
  },contexts:[depth0],types:["ID"],hashContexts:hashContexts,hashTypes:hashTypes,data:data})));
  data.buffer.push("<label for=\"fri_1\">&nbsp;</label></li>\n			  <li>");
  hashContexts = {'checkedBinding': depth0,'id': depth0};
  hashTypes = {'checkedBinding': "STRING",'id': "STRING"};
  data.buffer.push(escapeExpression(helpers.view.call(depth0, "Ember.Checkbox", {hash:{
    'checkedBinding': ("sat_early_morning"),
    'id': ("sat_1")
  },contexts:[depth0],types:["ID"],hashContexts:hashContexts,hashTypes:hashTypes,data:data})));
  data.buffer.push("<label for=\"sat_1\">&nbsp;</label></li>\n			</ul>\n		  </li>\n		  <li>\n			<ul>\n			  <li><strong>Late Morning</strong> (9am - 12pm)<span>9 - 12 PM</span></li>\n			  <li>");
  hashContexts = {'checkedBinding': depth0,'id': depth0};
  hashTypes = {'checkedBinding': "STRING",'id': "STRING"};
  data.buffer.push(escapeExpression(helpers.view.call(depth0, "Ember.Checkbox", {hash:{
    'checkedBinding': ("sun_late_morning"),
    'id': ("sun_2")
  },contexts:[depth0],types:["ID"],hashContexts:hashContexts,hashTypes:hashTypes,data:data})));
  data.buffer.push("<label for=\"sun_2\">&nbsp;</label></li>\n			  <li>");
  hashContexts = {'checkedBinding': depth0,'id': depth0};
  hashTypes = {'checkedBinding': "STRING",'id': "STRING"};
  data.buffer.push(escapeExpression(helpers.view.call(depth0, "Ember.Checkbox", {hash:{
    'checkedBinding': ("mon_late_morning"),
    'id': ("mon_2")
  },contexts:[depth0],types:["ID"],hashContexts:hashContexts,hashTypes:hashTypes,data:data})));
  data.buffer.push("<label for=\"mon_2\">&nbsp;</label></li>\n			  <li>");
  hashContexts = {'checkedBinding': depth0,'id': depth0};
  hashTypes = {'checkedBinding': "STRING",'id': "STRING"};
  data.buffer.push(escapeExpression(helpers.view.call(depth0, "Ember.Checkbox", {hash:{
    'checkedBinding': ("tues_late_morning"),
    'id': ("tues_2")
  },contexts:[depth0],types:["ID"],hashContexts:hashContexts,hashTypes:hashTypes,data:data})));
  data.buffer.push("<label for=\"tues_2\">&nbsp;</label></li>\n			  <li>");
  hashContexts = {'checkedBinding': depth0,'id': depth0};
  hashTypes = {'checkedBinding': "STRING",'id': "STRING"};
  data.buffer.push(escapeExpression(helpers.view.call(depth0, "Ember.Checkbox", {hash:{
    'checkedBinding': ("wed_late_morning"),
    'id': ("wed_2")
  },contexts:[depth0],types:["ID"],hashContexts:hashContexts,hashTypes:hashTypes,data:data})));
  data.buffer.push("<label for=\"wed_2\">&nbsp;</label></li>\n			  <li>");
  hashContexts = {'checkedBinding': depth0,'id': depth0};
  hashTypes = {'checkedBinding': "STRING",'id': "STRING"};
  data.buffer.push(escapeExpression(helpers.view.call(depth0, "Ember.Checkbox", {hash:{
    'checkedBinding': ("thurs_late_morning"),
    'id': ("thurs_2")
  },contexts:[depth0],types:["ID"],hashContexts:hashContexts,hashTypes:hashTypes,data:data})));
  data.buffer.push("<label for=\"thurs_2\">&nbsp;</label></li>\n			  <li>");
  hashContexts = {'checkedBinding': depth0,'id': depth0};
  hashTypes = {'checkedBinding': "STRING",'id': "STRING"};
  data.buffer.push(escapeExpression(helpers.view.call(depth0, "Ember.Checkbox", {hash:{
    'checkedBinding': ("fri_late_morning"),
    'id': ("fri_2")
  },contexts:[depth0],types:["ID"],hashContexts:hashContexts,hashTypes:hashTypes,data:data})));
  data.buffer.push("<label for=\"fri_2\">&nbsp;</label></li>\n			  <li>");
  hashContexts = {'checkedBinding': depth0,'id': depth0};
  hashTypes = {'checkedBinding': "STRING",'id': "STRING"};
  data.buffer.push(escapeExpression(helpers.view.call(depth0, "Ember.Checkbox", {hash:{
    'checkedBinding': ("sat_late_morning"),
    'id': ("sat_2")
  },contexts:[depth0],types:["ID"],hashContexts:hashContexts,hashTypes:hashTypes,data:data})));
  data.buffer.push("<label for=\"sat_2\">&nbsp;</label></li>\n			</ul>\n		  </li>\n		  <li>\n			<ul>\n			  <li><strong>Early Afternoon</strong> (12pm - 3pm)<span>12 - 3 PM</span></li>\n			  <li>");
  hashContexts = {'checkedBinding': depth0,'id': depth0};
  hashTypes = {'checkedBinding': "STRING",'id': "STRING"};
  data.buffer.push(escapeExpression(helpers.view.call(depth0, "Ember.Checkbox", {hash:{
    'checkedBinding': ("sun_early_afternoon"),
    'id': ("sun_3")
  },contexts:[depth0],types:["ID"],hashContexts:hashContexts,hashTypes:hashTypes,data:data})));
  data.buffer.push("<label for=\"sun_3\">&nbsp;</label></li>\n			  <li>");
  hashContexts = {'checkedBinding': depth0,'id': depth0};
  hashTypes = {'checkedBinding': "STRING",'id': "STRING"};
  data.buffer.push(escapeExpression(helpers.view.call(depth0, "Ember.Checkbox", {hash:{
    'checkedBinding': ("mon_early_afternoon"),
    'id': ("mon_3")
  },contexts:[depth0],types:["ID"],hashContexts:hashContexts,hashTypes:hashTypes,data:data})));
  data.buffer.push("<label for=\"mon_3\">&nbsp;</label></li>\n			  <li>");
  hashContexts = {'checkedBinding': depth0,'id': depth0};
  hashTypes = {'checkedBinding': "STRING",'id': "STRING"};
  data.buffer.push(escapeExpression(helpers.view.call(depth0, "Ember.Checkbox", {hash:{
    'checkedBinding': ("tues_early_afternoon"),
    'id': ("tues_3")
  },contexts:[depth0],types:["ID"],hashContexts:hashContexts,hashTypes:hashTypes,data:data})));
  data.buffer.push("<label for=\"tues_3\">&nbsp;</label></li>\n			  <li>");
  hashContexts = {'checkedBinding': depth0,'id': depth0};
  hashTypes = {'checkedBinding': "STRING",'id': "STRING"};
  data.buffer.push(escapeExpression(helpers.view.call(depth0, "Ember.Checkbox", {hash:{
    'checkedBinding': ("wed_early_afternoon"),
    'id': ("wed_3")
  },contexts:[depth0],types:["ID"],hashContexts:hashContexts,hashTypes:hashTypes,data:data})));
  data.buffer.push("<label for=\"wed_3\">&nbsp;</label></li>\n			  <li>");
  hashContexts = {'checkedBinding': depth0,'id': depth0};
  hashTypes = {'checkedBinding': "STRING",'id': "STRING"};
  data.buffer.push(escapeExpression(helpers.view.call(depth0, "Ember.Checkbox", {hash:{
    'checkedBinding': ("thurs_early_afternoon"),
    'id': ("thurs_3")
  },contexts:[depth0],types:["ID"],hashContexts:hashContexts,hashTypes:hashTypes,data:data})));
  data.buffer.push("<label for=\"thurs_3\">&nbsp;</label></li>\n			  <li>");
  hashContexts = {'checkedBinding': depth0,'id': depth0};
  hashTypes = {'checkedBinding': "STRING",'id': "STRING"};
  data.buffer.push(escapeExpression(helpers.view.call(depth0, "Ember.Checkbox", {hash:{
    'checkedBinding': ("fri_early_afternoon"),
    'id': ("fri_3")
  },contexts:[depth0],types:["ID"],hashContexts:hashContexts,hashTypes:hashTypes,data:data})));
  data.buffer.push("<label for=\"fri_3\">&nbsp;</label></li>\n			  <li>");
  hashContexts = {'checkedBinding': depth0,'id': depth0};
  hashTypes = {'checkedBinding': "STRING",'id': "STRING"};
  data.buffer.push(escapeExpression(helpers.view.call(depth0, "Ember.Checkbox", {hash:{
    'checkedBinding': ("sat_early_afternoon"),
    'id': ("sat_3")
  },contexts:[depth0],types:["ID"],hashContexts:hashContexts,hashTypes:hashTypes,data:data})));
  data.buffer.push("<label for=\"sat_3\">&nbsp;</label></li>\n			</ul>\n		  </li>\n		  <li>\n			<ul>\n			  <li><strong>Late Afternoon</strong> (3pm - 6pm)<span>3 - 6 PM</span></li>\n			  <li>");
  hashContexts = {'checkedBinding': depth0,'id': depth0};
  hashTypes = {'checkedBinding': "STRING",'id': "STRING"};
  data.buffer.push(escapeExpression(helpers.view.call(depth0, "Ember.Checkbox", {hash:{
    'checkedBinding': ("sun_late_afternoon"),
    'id': ("sun_4")
  },contexts:[depth0],types:["ID"],hashContexts:hashContexts,hashTypes:hashTypes,data:data})));
  data.buffer.push("<label for=\"sun_4\">&nbsp;</label></li>\n			  <li>");
  hashContexts = {'checkedBinding': depth0,'id': depth0};
  hashTypes = {'checkedBinding': "STRING",'id': "STRING"};
  data.buffer.push(escapeExpression(helpers.view.call(depth0, "Ember.Checkbox", {hash:{
    'checkedBinding': ("mon_late_afternoon"),
    'id': ("mon_4")
  },contexts:[depth0],types:["ID"],hashContexts:hashContexts,hashTypes:hashTypes,data:data})));
  data.buffer.push("<label for=\"mon_4\">&nbsp;</label></li>\n			  <li>");
  hashContexts = {'checkedBinding': depth0,'id': depth0};
  hashTypes = {'checkedBinding': "STRING",'id': "STRING"};
  data.buffer.push(escapeExpression(helpers.view.call(depth0, "Ember.Checkbox", {hash:{
    'checkedBinding': ("tues_late_afternoon"),
    'id': ("tues_4")
  },contexts:[depth0],types:["ID"],hashContexts:hashContexts,hashTypes:hashTypes,data:data})));
  data.buffer.push("<label for=\"tues_4\">&nbsp;</label></li>\n			  <li>");
  hashContexts = {'checkedBinding': depth0,'id': depth0};
  hashTypes = {'checkedBinding': "STRING",'id': "STRING"};
  data.buffer.push(escapeExpression(helpers.view.call(depth0, "Ember.Checkbox", {hash:{
    'checkedBinding': ("wed_late_afternoon"),
    'id': ("wed_4")
  },contexts:[depth0],types:["ID"],hashContexts:hashContexts,hashTypes:hashTypes,data:data})));
  data.buffer.push("<label for=\"wed_4\">&nbsp;</label></li>\n			  <li>");
  hashContexts = {'checkedBinding': depth0,'id': depth0};
  hashTypes = {'checkedBinding': "STRING",'id': "STRING"};
  data.buffer.push(escapeExpression(helpers.view.call(depth0, "Ember.Checkbox", {hash:{
    'checkedBinding': ("thurs_late_afternoon"),
    'id': ("thurs_4")
  },contexts:[depth0],types:["ID"],hashContexts:hashContexts,hashTypes:hashTypes,data:data})));
  data.buffer.push("<label for=\"thurs_4\">&nbsp;</label></li>\n			  <li>");
  hashContexts = {'checkedBinding': depth0,'id': depth0};
  hashTypes = {'checkedBinding': "STRING",'id': "STRING"};
  data.buffer.push(escapeExpression(helpers.view.call(depth0, "Ember.Checkbox", {hash:{
    'checkedBinding': ("fri_late_afternoon"),
    'id': ("fri_4")
  },contexts:[depth0],types:["ID"],hashContexts:hashContexts,hashTypes:hashTypes,data:data})));
  data.buffer.push("<label for=\"fri_4\">&nbsp;</label></li>\n			  <li>");
  hashContexts = {'checkedBinding': depth0,'id': depth0};
  hashTypes = {'checkedBinding': "STRING",'id': "STRING"};
  data.buffer.push(escapeExpression(helpers.view.call(depth0, "Ember.Checkbox", {hash:{
    'checkedBinding': ("sat_late_afternoon"),
    'id': ("sat_4")
  },contexts:[depth0],types:["ID"],hashContexts:hashContexts,hashTypes:hashTypes,data:data})));
  data.buffer.push("<label for=\"sat_4\">&nbsp;</label></li>\n			</ul>\n		  </li>\n		  <li>\n			<ul>\n			  <li><strong>Early Evening</strong> (6pm - 9pm)<span>6 - 9 PM</span></li>\n			  <li>");
  hashContexts = {'checkedBinding': depth0,'id': depth0};
  hashTypes = {'checkedBinding': "STRING",'id': "STRING"};
  data.buffer.push(escapeExpression(helpers.view.call(depth0, "Ember.Checkbox", {hash:{
    'checkedBinding': ("sun_early_evening"),
    'id': ("sun_5")
  },contexts:[depth0],types:["ID"],hashContexts:hashContexts,hashTypes:hashTypes,data:data})));
  data.buffer.push("<label for=\"sun_5\">&nbsp;</label></li>\n			  <li>");
  hashContexts = {'checkedBinding': depth0,'id': depth0};
  hashTypes = {'checkedBinding': "STRING",'id': "STRING"};
  data.buffer.push(escapeExpression(helpers.view.call(depth0, "Ember.Checkbox", {hash:{
    'checkedBinding': ("mon_early_evening"),
    'id': ("mon_5")
  },contexts:[depth0],types:["ID"],hashContexts:hashContexts,hashTypes:hashTypes,data:data})));
  data.buffer.push("<label for=\"mon_5\">&nbsp;</label></li>\n			  <li>");
  hashContexts = {'checkedBinding': depth0,'id': depth0};
  hashTypes = {'checkedBinding': "STRING",'id': "STRING"};
  data.buffer.push(escapeExpression(helpers.view.call(depth0, "Ember.Checkbox", {hash:{
    'checkedBinding': ("tues_early_evening"),
    'id': ("tues_5")
  },contexts:[depth0],types:["ID"],hashContexts:hashContexts,hashTypes:hashTypes,data:data})));
  data.buffer.push("<label for=\"tues_5\">&nbsp;</label></li>\n			  <li>");
  hashContexts = {'checkedBinding': depth0,'id': depth0};
  hashTypes = {'checkedBinding': "STRING",'id': "STRING"};
  data.buffer.push(escapeExpression(helpers.view.call(depth0, "Ember.Checkbox", {hash:{
    'checkedBinding': ("wed_early_evening"),
    'id': ("wed_5")
  },contexts:[depth0],types:["ID"],hashContexts:hashContexts,hashTypes:hashTypes,data:data})));
  data.buffer.push("<label for=\"wed_5\">&nbsp;</label></li>\n			  <li>");
  hashContexts = {'checkedBinding': depth0,'id': depth0};
  hashTypes = {'checkedBinding': "STRING",'id': "STRING"};
  data.buffer.push(escapeExpression(helpers.view.call(depth0, "Ember.Checkbox", {hash:{
    'checkedBinding': ("thurs_early_evening"),
    'id': ("thurs_5")
  },contexts:[depth0],types:["ID"],hashContexts:hashContexts,hashTypes:hashTypes,data:data})));
  data.buffer.push("<label for=\"thurs_5\">&nbsp;</label></li>\n			  <li>");
  hashContexts = {'checkedBinding': depth0,'id': depth0};
  hashTypes = {'checkedBinding': "STRING",'id': "STRING"};
  data.buffer.push(escapeExpression(helpers.view.call(depth0, "Ember.Checkbox", {hash:{
    'checkedBinding': ("fri_early_evening"),
    'id': ("fri_5")
  },contexts:[depth0],types:["ID"],hashContexts:hashContexts,hashTypes:hashTypes,data:data})));
  data.buffer.push("<label for=\"fri_5\">&nbsp;</label></li>\n			  <li>");
  hashContexts = {'checkedBinding': depth0,'id': depth0};
  hashTypes = {'checkedBinding': "STRING",'id': "STRING"};
  data.buffer.push(escapeExpression(helpers.view.call(depth0, "Ember.Checkbox", {hash:{
    'checkedBinding': ("sat_early_evening"),
    'id': ("sat_5")
  },contexts:[depth0],types:["ID"],hashContexts:hashContexts,hashTypes:hashTypes,data:data})));
  data.buffer.push("<label for=\"sat_5\">&nbsp;</label></li>\n			</ul>\n		  </li>\n		  <li>\n			<ul>\n			  <li><strong>Late Evening</strong> (9pm - 12am)<span>9 - 12 AM</span></li>\n			  <li>");
  hashContexts = {'checkedBinding': depth0,'id': depth0};
  hashTypes = {'checkedBinding': "STRING",'id': "STRING"};
  data.buffer.push(escapeExpression(helpers.view.call(depth0, "Ember.Checkbox", {hash:{
    'checkedBinding': ("sun_late_evening"),
    'id': ("sun_6")
  },contexts:[depth0],types:["ID"],hashContexts:hashContexts,hashTypes:hashTypes,data:data})));
  data.buffer.push("<label for=\"sun_6\">&nbsp;</label></li>\n			  <li>");
  hashContexts = {'checkedBinding': depth0,'id': depth0};
  hashTypes = {'checkedBinding': "STRING",'id': "STRING"};
  data.buffer.push(escapeExpression(helpers.view.call(depth0, "Ember.Checkbox", {hash:{
    'checkedBinding': ("mon_late_evening"),
    'id': ("mon_6")
  },contexts:[depth0],types:["ID"],hashContexts:hashContexts,hashTypes:hashTypes,data:data})));
  data.buffer.push("<label for=\"mon_6\">&nbsp;</label></li>\n			  <li>");
  hashContexts = {'checkedBinding': depth0,'id': depth0};
  hashTypes = {'checkedBinding': "STRING",'id': "STRING"};
  data.buffer.push(escapeExpression(helpers.view.call(depth0, "Ember.Checkbox", {hash:{
    'checkedBinding': ("tues_late_evening"),
    'id': ("tues_6")
  },contexts:[depth0],types:["ID"],hashContexts:hashContexts,hashTypes:hashTypes,data:data})));
  data.buffer.push("<label for=\"tues_6\">&nbsp;</label></li>\n			  <li>");
  hashContexts = {'checkedBinding': depth0,'id': depth0};
  hashTypes = {'checkedBinding': "STRING",'id': "STRING"};
  data.buffer.push(escapeExpression(helpers.view.call(depth0, "Ember.Checkbox", {hash:{
    'checkedBinding': ("wed_late_evening"),
    'id': ("wed_6")
  },contexts:[depth0],types:["ID"],hashContexts:hashContexts,hashTypes:hashTypes,data:data})));
  data.buffer.push("<label for=\"wed_6\">&nbsp;</label></li>\n			  <li>");
  hashContexts = {'checkedBinding': depth0,'id': depth0};
  hashTypes = {'checkedBinding': "STRING",'id': "STRING"};
  data.buffer.push(escapeExpression(helpers.view.call(depth0, "Ember.Checkbox", {hash:{
    'checkedBinding': ("thurs_late_evening"),
    'id': ("thurs_6")
  },contexts:[depth0],types:["ID"],hashContexts:hashContexts,hashTypes:hashTypes,data:data})));
  data.buffer.push("<label for=\"thurs_6\">&nbsp;</label></li>\n			  <li>");
  hashContexts = {'checkedBinding': depth0,'id': depth0};
  hashTypes = {'checkedBinding': "STRING",'id': "STRING"};
  data.buffer.push(escapeExpression(helpers.view.call(depth0, "Ember.Checkbox", {hash:{
    'checkedBinding': ("fri_late_evening"),
    'id': ("fri_6")
  },contexts:[depth0],types:["ID"],hashContexts:hashContexts,hashTypes:hashTypes,data:data})));
  data.buffer.push("<label for=\"fri_6\">&nbsp;</label></li>\n			  <li>");
  hashContexts = {'checkedBinding': depth0,'id': depth0};
  hashTypes = {'checkedBinding': "STRING",'id': "STRING"};
  data.buffer.push(escapeExpression(helpers.view.call(depth0, "Ember.Checkbox", {hash:{
    'checkedBinding': ("sat_late_evening"),
    'id': ("sat_6")
  },contexts:[depth0],types:["ID"],hashContexts:hashContexts,hashTypes:hashTypes,data:data})));
  data.buffer.push("<label for=\"sat_6\">&nbsp;</label></li>\n			</ul>\n		  </li>\n		  <li>\n			<ul>\n			  <li><strong>Overnight</strong> (12am - 6am)<span>12 - 6 AM</span></li>\n			  <li>");
  hashContexts = {'checkedBinding': depth0,'id': depth0};
  hashTypes = {'checkedBinding': "STRING",'id': "STRING"};
  data.buffer.push(escapeExpression(helpers.view.call(depth0, "Ember.Checkbox", {hash:{
    'checkedBinding': ("sun_overnight"),
    'id': ("sun_7")
  },contexts:[depth0],types:["ID"],hashContexts:hashContexts,hashTypes:hashTypes,data:data})));
  data.buffer.push("<label for=\"sun_7\">&nbsp;</label></li>\n			  <li>");
  hashContexts = {'checkedBinding': depth0,'id': depth0};
  hashTypes = {'checkedBinding': "STRING",'id': "STRING"};
  data.buffer.push(escapeExpression(helpers.view.call(depth0, "Ember.Checkbox", {hash:{
    'checkedBinding': ("mon_overnight"),
    'id': ("mon_7")
  },contexts:[depth0],types:["ID"],hashContexts:hashContexts,hashTypes:hashTypes,data:data})));
  data.buffer.push("<label for=\"mon_7\">&nbsp;</label></li>\n			  <li>");
  hashContexts = {'checkedBinding': depth0,'id': depth0};
  hashTypes = {'checkedBinding': "STRING",'id': "STRING"};
  data.buffer.push(escapeExpression(helpers.view.call(depth0, "Ember.Checkbox", {hash:{
    'checkedBinding': ("tues_overnight"),
    'id': ("tues_7")
  },contexts:[depth0],types:["ID"],hashContexts:hashContexts,hashTypes:hashTypes,data:data})));
  data.buffer.push("<label for=\"tues_7\">&nbsp;</label></li>\n			  <li>");
  hashContexts = {'checkedBinding': depth0,'id': depth0};
  hashTypes = {'checkedBinding': "STRING",'id': "STRING"};
  data.buffer.push(escapeExpression(helpers.view.call(depth0, "Ember.Checkbox", {hash:{
    'checkedBinding': ("wed_overnight"),
    'id': ("wed_7")
  },contexts:[depth0],types:["ID"],hashContexts:hashContexts,hashTypes:hashTypes,data:data})));
  data.buffer.push("<label for=\"wed_7\">&nbsp;</label></li>\n			  <li>");
  hashContexts = {'checkedBinding': depth0,'id': depth0};
  hashTypes = {'checkedBinding': "STRING",'id': "STRING"};
  data.buffer.push(escapeExpression(helpers.view.call(depth0, "Ember.Checkbox", {hash:{
    'checkedBinding': ("thurs_overnight"),
    'id': ("thurs_7")
  },contexts:[depth0],types:["ID"],hashContexts:hashContexts,hashTypes:hashTypes,data:data})));
  data.buffer.push("<label for=\"thurs_7\">&nbsp;</label></li>\n			  <li>");
  hashContexts = {'checkedBinding': depth0,'id': depth0};
  hashTypes = {'checkedBinding': "STRING",'id': "STRING"};
  data.buffer.push(escapeExpression(helpers.view.call(depth0, "Ember.Checkbox", {hash:{
    'checkedBinding': ("fri_overnight"),
    'id': ("fri_7")
  },contexts:[depth0],types:["ID"],hashContexts:hashContexts,hashTypes:hashTypes,data:data})));
  data.buffer.push("<label for=\"fri_7\">&nbsp;</label></li>\n			  <li>");
  hashContexts = {'checkedBinding': depth0,'id': depth0};
  hashTypes = {'checkedBinding': "STRING",'id': "STRING"};
  data.buffer.push(escapeExpression(helpers.view.call(depth0, "Ember.Checkbox", {hash:{
    'checkedBinding': ("sat_overnight"),
    'id': ("sat_7")
  },contexts:[depth0],types:["ID"],hashContexts:hashContexts,hashTypes:hashTypes,data:data})));
  data.buffer.push("<label for=\"sat_7\">&nbsp;</label></li>\n			</ul>\n		  </li>\n		</ul>\n		<div><a href=\"#\">Check All</a> | <a href=\"#\">Clear All</a><br /><a class=\"button button_small\" href=\"#\"><span class=\"icon_ok2\">&nbsp;</span>Save</a></div>\n	  </div>\n	  <!-- /schedule_block -->\n");
  return buffer;
  
});
Ember.TEMPLATES["sitterEdit/profile"] = Ember.Handlebars.template(function anonymous(Handlebars,depth0,helpers,partials,data) {
this.compilerInfo = [3,'>= 1.0.0-rc.4'];
helpers = helpers || Ember.Handlebars.helpers; data = data || {};
  var buffer = '', stack1, hashContexts, hashTypes, options, escapeExpression=this.escapeExpression, self=this, functionType="function", blockHelperMissing=helpers.blockHelperMissing;

function program1(depth0,data) {
  
  
  data.buffer.push("<a class=\"button button_smaller button_edit\" href=\"#\"><span class=\"icon_plus\">&nbsp;</span>ADD</a></p>\n				    <a class=\"button button_small\" href=\"#\"><span class=\"icon_ok2\">&nbsp;</span>Save</a>\n                    ");
  }

function program3(depth0,data) {
  
  
  data.buffer.push("<p><span>add school (if not listed above):</span><input type=\"text\" /><a class=\"button button_smaller button_edit\" href=\"#\"><span class=\"icon_plus\">&nbsp;</span>ADD</a></p>");
  }

  data.buffer.push("<!-- profile_block -->\n	  <div class=\"mob_tab_trigger active\">Profile</div>\n	  <div class=\"tab_content profile_block\" id=\"tab-1\">\n		<form class=\"form_style\">\n		  <ul>\n			<li>\n			  <ul>\n				<li><span class=\"icon_bio2\">&nbsp;</span>Biography</li>\n				<li>\n				  <p><i class=\"char\">1100 CHAR</i>");
  hashContexts = {'valueBinding': depth0};
  hashTypes = {'valueBinding': "STRING"};
  data.buffer.push(escapeExpression(helpers.view.call(depth0, "Ember.TextArea", {hash:{
    'valueBinding': ("biography")
  },contexts:[depth0],types:["ID"],hashContexts:hashContexts,hashTypes:hashTypes,data:data})));
  data.buffer.push("</p>\n				  <a class=\"button button_small\" ");
  hashTypes = {};
  hashContexts = {};
  data.buffer.push(escapeExpression(helpers.action.call(depth0, "saveSettings", {hash:{},contexts:[depth0],types:["STRING"],hashContexts:hashContexts,hashTypes:hashTypes,data:data})));
  data.buffer.push("><span class=\"icon_ok2\">&nbsp;</span>Save</a>\n				</li>\n			  </ul>\n			</li>\n			<li>\n			  <ul>\n				<li><span class=\"icon_gender2\">&nbsp;</span>Gender</li>\n				<li>\n				  <p>\n                    ");
  hashContexts = {'id': depth0,'selectionBinding': depth0,'value': depth0,'name': depth0};
  hashTypes = {'id': "STRING",'selectionBinding': "STRING",'value': "STRING",'name': "STRING"};
  data.buffer.push(escapeExpression(helpers.view.call(depth0, "Ember.RadioButton", {hash:{
    'id': ("female"),
    'selectionBinding': ("gender"),
    'value': ("female"),
    'name': ("gender")
  },contexts:[depth0],types:["ID"],hashContexts:hashContexts,hashTypes:hashTypes,data:data})));
  data.buffer.push("\n                    <label for=\"female\">Female</label>\n                    ");
  hashContexts = {'id': depth0,'selectionBinding': depth0,'value': depth0,'name': depth0};
  hashTypes = {'id': "STRING",'selectionBinding': "STRING",'value': "STRING",'name': "STRING"};
  data.buffer.push(escapeExpression(helpers.view.call(depth0, "Ember.RadioButton", {hash:{
    'id': ("male"),
    'selectionBinding': ("gender"),
    'value': ("male"),
    'name': ("gender")
  },contexts:[depth0],types:["ID"],hashContexts:hashContexts,hashTypes:hashTypes,data:data})));
  data.buffer.push("\n                    <label for=\"male\">Male</label>\n                  </p>\n				  <a class=\"button button_small\" ");
  hashTypes = {};
  hashContexts = {};
  data.buffer.push(escapeExpression(helpers.action.call(depth0, "saveSettings", {hash:{},contexts:[depth0],types:["STRING"],hashContexts:hashContexts,hashTypes:hashTypes,data:data})));
  data.buffer.push("><span class=\"icon_ok2\">&nbsp;</span>Save</a>\n				</li>\n			  </ul>\n			</li>\n			<li>\n			  <ul>\n				<li><span class=\"icon_pin4\">&nbsp;</span>Home Address</li>\n				<li>\n				  <p>\n                    ");
  hashContexts = {'placeholder': depth0,'valueBinding': depth0};
  hashTypes = {'placeholder': "STRING",'valueBinding': "STRING"};
  data.buffer.push(escapeExpression(helpers.view.call(depth0, "Ember.TextField", {hash:{
    'placeholder': ("Street address"),
    'valueBinding': ("address1")
  },contexts:[depth0],types:["ID"],hashContexts:hashContexts,hashTypes:hashTypes,data:data})));
  data.buffer.push("\n                    ");
  hashContexts = {'placeholder': depth0,'valueBinding': depth0,'class': depth0};
  hashTypes = {'placeholder': "STRING",'valueBinding': "STRING",'class': "STRING"};
  data.buffer.push(escapeExpression(helpers.view.call(depth0, "Ember.TextField", {hash:{
    'placeholder': ("Apt/Suite"),
    'valueBinding': ("address2"),
    'class': ("small")
  },contexts:[depth0],types:["ID"],hashContexts:hashContexts,hashTypes:hashTypes,data:data})));
  data.buffer.push("\n                  </p>\n				  <p>\n                    ");
  hashContexts = {'placeholder': depth0,'valueBinding': depth0,'class': depth0};
  hashTypes = {'placeholder': "STRING",'valueBinding': "STRING",'class': "STRING"};
  data.buffer.push(escapeExpression(helpers.view.call(depth0, "Ember.TextField", {hash:{
    'placeholder': ("Zip Code"),
    'valueBinding': ("live_zip"),
    'class': ("small")
  },contexts:[depth0],types:["ID"],hashContexts:hashContexts,hashTypes:hashTypes,data:data})));
  data.buffer.push("\n                    ");
  hashContexts = {'placeholder': depth0,'valueBinding': depth0};
  hashTypes = {'placeholder': "STRING",'valueBinding': "STRING"};
  data.buffer.push(escapeExpression(helpers.view.call(depth0, "Ember.TextField", {hash:{
    'placeholder': ("City"),
    'valueBinding': ("city")
  },contexts:[depth0],types:["ID"],hashContexts:hashContexts,hashTypes:hashTypes,data:data})));
  data.buffer.push("\n                    ");
  hashContexts = {'viewName': depth0,'prompt': depth0,'contentBinding': depth0,'optionLabelPath': depth0,'optionValuePath': depth0,'selectionBinding': depth0,'required': depth0};
  hashTypes = {'viewName': "STRING",'prompt': "STRING",'contentBinding': "STRING",'optionLabelPath': "STRING",'optionValuePath': "STRING",'selectionBinding': "STRING",'required': "STRING"};
  data.buffer.push(escapeExpression(helpers.view.call(depth0, "Sitterfied.Select2", {hash:{
    'viewName': ("fieldValueSelect2"),
    'prompt': ("Select State"),
    'contentBinding': ("Sitterfied.States"),
    'optionLabelPath': ("content"),
    'optionValuePath': ("content"),
    'selectionBinding': ("state"),
    'required': ("")
  },contexts:[depth0],types:["ID"],hashContexts:hashContexts,hashTypes:hashTypes,data:data})));
  data.buffer.push("\n\n                  </p>\n				  <a class=\"button button_small\" ");
  hashTypes = {};
  hashContexts = {};
  data.buffer.push(escapeExpression(helpers.action.call(depth0, "saveSettings", {hash:{},contexts:[depth0],types:["STRING"],hashContexts:hashContexts,hashTypes:hashTypes,data:data})));
  data.buffer.push("><span class=\"icon_ok2\">&nbsp;</span>Save</a>\n				</li>\n			  </ul>\n			</li>\n			<li>\n			  <ul>\n				<li><span class=\"icon_iphone2\">&nbsp;</span>Cell Phone Number</li>\n				<li>\n				  <p>\n                    ");
  hashContexts = {'placeholder': depth0,'valueBinding': depth0};
  hashTypes = {'placeholder': "STRING",'valueBinding': "STRING"};
  data.buffer.push(escapeExpression(helpers.view.call(depth0, "Ember.TextField", {hash:{
    'placeholder': ("(123) 456-7890"),
    'valueBinding': ("cell")
  },contexts:[depth0],types:["ID"],hashContexts:hashContexts,hashTypes:hashTypes,data:data})));
  data.buffer.push("\n                  </p>\n				  <a class=\"button button_small\" ");
  hashTypes = {};
  hashContexts = {};
  data.buffer.push(escapeExpression(helpers.action.call(depth0, "saveSettings", {hash:{},contexts:[depth0],types:["STRING"],hashContexts:hashContexts,hashTypes:hashTypes,data:data})));
  data.buffer.push("><span class=\"icon_ok2\">&nbsp;</span>Save</a>\n				</li>\n			  </ul>\n			</li>\n			<li>\n			  <ul>\n				<li><span class=\"icon_email3\">&nbsp;</span>Email Address</li>\n				<li>\n				  <p>");
  hashContexts = {'placeholder': depth0,'valueBinding': depth0};
  hashTypes = {'placeholder': "STRING",'valueBinding': "STRING"};
  data.buffer.push(escapeExpression(helpers.view.call(depth0, "Ember.TextField", {hash:{
    'placeholder': ("Email"),
    'valueBinding': ("email")
  },contexts:[depth0],types:["ID"],hashContexts:hashContexts,hashTypes:hashTypes,data:data})));
  data.buffer.push("</p>\n				  <a class=\"button button_small\" ");
  hashTypes = {};
  hashContexts = {};
  data.buffer.push(escapeExpression(helpers.action.call(depth0, "saveSettings", {hash:{},contexts:[depth0],types:["STRING"],hashContexts:hashContexts,hashTypes:hashTypes,data:data})));
  data.buffer.push("><span class=\"icon_ok2\">&nbsp;</span>Save</a>\n				</li>\n			  </ul>\n			</li>\n			<li>\n			  <ul>\n				<li><span class=\"icon_age2\">&nbsp;</span>Age</li>\n				<li>\n				  <p><span class=\"short\">DATE OF BIRTH</span>");
  hashContexts = {'valueBinding': depth0};
  hashTypes = {'valueBinding': "STRING"};
  data.buffer.push(escapeExpression(helpers.view.call(depth0, "Ember.DatePicker", {hash:{
    'valueBinding': ("dob")
  },contexts:[depth0],types:["ID"],hashContexts:hashContexts,hashTypes:hashTypes,data:data})));
  data.buffer.push(" </p>\n				  <a class=\"button button_small\" href=\"#\"><span class=\"icon_ok2\">&nbsp;</span>Save</a>\n				</li>\n			  </ul>\n			</li>\n			<li>\n			  <ul>\n				<li><span class=\"icon_smoker2\">&nbsp;</span>Smoker</li>\n				<li>\n				  <p>\n                    ");
  hashContexts = {'id': depth0,'selectionBinding': depth0,'value': depth0,'name': depth0};
  hashTypes = {'id': "STRING",'selectionBinding': "STRING",'value': "STRING",'name': "STRING"};
  data.buffer.push(escapeExpression(helpers.view.call(depth0, "Ember.RadioButton", {hash:{
    'id': ("yes"),
    'selectionBinding': ("smoker"),
    'value': ("true"),
    'name': ("smoker")
  },contexts:[depth0],types:["ID"],hashContexts:hashContexts,hashTypes:hashTypes,data:data})));
  data.buffer.push("\n                    <label for=\"yes\">YES</label>\n                    ");
  hashContexts = {'id': depth0,'selectionBinding': depth0,'value': depth0,'name': depth0};
  hashTypes = {'id': "STRING",'selectionBinding': "STRING",'value': "STRING",'name': "STRING"};
  data.buffer.push(escapeExpression(helpers.view.call(depth0, "Ember.RadioButton", {hash:{
    'id': ("no"),
    'selectionBinding': ("smoker"),
    'value': ("false"),
    'name': ("smoker")
  },contexts:[depth0],types:["ID"],hashContexts:hashContexts,hashTypes:hashTypes,data:data})));
  data.buffer.push("\n                    <label for=\"no\">NO</label>\n                  </p>\n				  <a class=\"button button_small\" ");
  hashTypes = {};
  hashContexts = {};
  data.buffer.push(escapeExpression(helpers.action.call(depth0, "saveSettings", {hash:{},contexts:[depth0],types:["STRING"],hashContexts:hashContexts,hashTypes:hashTypes,data:data})));
  data.buffer.push("><span class=\"icon_ok2\">&nbsp;</span>Save</a>\n				</li>\n			  </ul>\n			</li>\n			<li>\n			  <ul>\n				<li><span class=\"icon_sick2\">&nbsp;</span>Sick Kids</li>\n				<li>\n				  <p>\n                    <span>willing to care for sick kids?</span>\n                    ");
  hashContexts = {'id': depth0,'selectionBinding': depth0,'value': depth0,'name': depth0};
  hashTypes = {'id': "STRING",'selectionBinding': "STRING",'value': "STRING",'name': "STRING"};
  data.buffer.push(escapeExpression(helpers.view.call(depth0, "Ember.RadioButton", {hash:{
    'id': ("yes2"),
    'selectionBinding': ("sick"),
    'value': ("true"),
    'name': ("sick")
  },contexts:[depth0],types:["ID"],hashContexts:hashContexts,hashTypes:hashTypes,data:data})));
  data.buffer.push("\n                    <label for=\"yes2\">YES</label>\n                    ");
  hashContexts = {'id': depth0,'selectionBinding': depth0,'value': depth0,'name': depth0};
  hashTypes = {'id': "STRING",'selectionBinding': "STRING",'value': "STRING",'name': "STRING"};
  data.buffer.push(escapeExpression(helpers.view.call(depth0, "Ember.RadioButton", {hash:{
    'id': ("no2"),
    'selectionBinding': ("sick"),
    'value': ("false"),
    'name': ("sick")
  },contexts:[depth0],types:["ID"],hashContexts:hashContexts,hashTypes:hashTypes,data:data})));
  data.buffer.push("\n                    <label for=\"no2\">NO</label>\n                  </p>\n				  <a class=\"button button_small\" ");
  hashTypes = {};
  hashContexts = {};
  data.buffer.push(escapeExpression(helpers.action.call(depth0, "saveSettings", {hash:{},contexts:[depth0],types:["STRING"],hashContexts:hashContexts,hashTypes:hashTypes,data:data})));
  data.buffer.push("><span class=\"icon_ok2\">&nbsp;</span>Save</a>\n				</li>\n			  </ul>\n			</li>\n			<li>\n			  <ul>\n				<li><span class=\"icon_transportation2\">&nbsp;</span>Transportation</li>\n				<li>\n                  <p><span>distance willing to travel:</span>");
  hashContexts = {'id': depth0,'placeholder': depth0,'valueBinding': depth0,'class': depth0};
  hashTypes = {'id': "STRING",'placeholder': "STRING",'valueBinding': "STRING",'class': "STRING"};
  data.buffer.push(escapeExpression(helpers.view.call(depth0, "Ember.TextField", {hash:{
    'id': ("distance"),
    'placeholder': ("Distance"),
    'valueBinding': ("travel_distance"),
    'class': ("small")
  },contexts:[depth0],types:["ID"],hashContexts:hashContexts,hashTypes:hashTypes,data:data})));
  data.buffer.push("<label for=\"distance\">Miles</label></p>\n				  <p><span>have a current driver’s license?</span>");
  hashContexts = {'id': depth0,'checkedBinding': depth0};
  hashTypes = {'id': "STRING",'checkedBinding': "STRING"};
  data.buffer.push(escapeExpression(helpers.view.call(depth0, "Ember.Checkbox", {hash:{
    'id': ("no3"),
    'checkedBinding': ("has_drivers_licence")
  },contexts:[depth0],types:["ID"],hashContexts:hashContexts,hashTypes:hashTypes,data:data})));
  data.buffer.push("<label for=\"no3\"></label></p>\n				  <a class=\"button button_small\" ");
  hashTypes = {};
  hashContexts = {};
  data.buffer.push(escapeExpression(helpers.action.call(depth0, "saveSettings", {hash:{},contexts:[depth0],types:["STRING"],hashContexts:hashContexts,hashTypes:hashTypes,data:data})));
  data.buffer.push("><span class=\"icon_ok2\">&nbsp;</span>Save</a>\n				</li>\n			  </ul>\n			</li>\n			<li>\n			  <ul>\n				<li><span class=\"icon_experience2\">&nbsp;</span>General Experience</li>\n				<li>\n				  <p><span>TOTAL years of experience:</span>");
  hashContexts = {'placeholder': depth0,'valueBinding': depth0};
  hashTypes = {'placeholder': "STRING",'valueBinding': "STRING"};
  data.buffer.push(escapeExpression(helpers.view.call(depth0, "Ember.TextField", {hash:{
    'placeholder': ("0"),
    'valueBinding': ("total_exp")
  },contexts:[depth0],types:["ID"],hashContexts:hashContexts,hashTypes:hashTypes,data:data})));
  data.buffer.push("</p>\n				  <p><span>Experience with infants:</span>");
  hashContexts = {'placeholder': depth0,'valueBinding': depth0};
  hashTypes = {'placeholder': "STRING",'valueBinding': "STRING"};
  data.buffer.push(escapeExpression(helpers.view.call(depth0, "Ember.TextField", {hash:{
    'placeholder': ("0"),
    'valueBinding': ("infant_exp")
  },contexts:[depth0],types:["ID"],hashContexts:hashContexts,hashTypes:hashTypes,data:data})));
  data.buffer.push("</p>\n				  <p><span>Experience with toddlers:</span>");
  hashContexts = {'placeholder': depth0,'valueBinding': depth0};
  hashTypes = {'placeholder': "STRING",'valueBinding': "STRING"};
  data.buffer.push(escapeExpression(helpers.view.call(depth0, "Ember.TextField", {hash:{
    'placeholder': ("0"),
    'valueBinding': ("toddler_exp")
  },contexts:[depth0],types:["ID"],hashContexts:hashContexts,hashTypes:hashTypes,data:data})));
  data.buffer.push("</p>\n				  <p><span>Experience with preschoolers:</span>");
  hashContexts = {'placeholder': depth0,'valueBinding': depth0};
  hashTypes = {'placeholder': "STRING",'valueBinding': "STRING"};
  data.buffer.push(escapeExpression(helpers.view.call(depth0, "Ember.TextField", {hash:{
    'placeholder': ("0"),
    'valueBinding': ("preschool_exp")
  },contexts:[depth0],types:["ID"],hashContexts:hashContexts,hashTypes:hashTypes,data:data})));
  data.buffer.push("</p>\n				  <p><span>Experience with School age:</span>");
  hashContexts = {'placeholder': depth0,'valueBinding': depth0};
  hashTypes = {'placeholder': "STRING",'valueBinding': "STRING"};
  data.buffer.push(escapeExpression(helpers.view.call(depth0, "Ember.TextField", {hash:{
    'placeholder': ("0"),
    'valueBinding': ("school_age_exp")
  },contexts:[depth0],types:["ID"],hashContexts:hashContexts,hashTypes:hashTypes,data:data})));
  data.buffer.push("</p>\n				  <p><span>Experience with Pre Teens:</span>");
  hashContexts = {'placeholder': depth0,'valueBinding': depth0};
  hashTypes = {'placeholder': "STRING",'valueBinding': "STRING"};
  data.buffer.push(escapeExpression(helpers.view.call(depth0, "Ember.TextField", {hash:{
    'placeholder': ("0."),
    'valueBinding': ("pre_teen_exp")
  },contexts:[depth0],types:["ID"],hashContexts:hashContexts,hashTypes:hashTypes,data:data})));
  data.buffer.push("</p>\n				  <p><span>Experience with teenagers:</span>");
  hashContexts = {'placeholder': depth0,'valueBinding': depth0};
  hashTypes = {'placeholder': "STRING",'valueBinding': "STRING"};
  data.buffer.push(escapeExpression(helpers.view.call(depth0, "Ember.TextField", {hash:{
    'placeholder': ("0"),
    'valueBinding': ("teen_exp")
  },contexts:[depth0],types:["ID"],hashContexts:hashContexts,hashTypes:hashTypes,data:data})));
  data.buffer.push("</p>\n				  <p><span>Experience with special needs?</span>");
  hashContexts = {'id': depth0,'checkedBinding': depth0};
  hashTypes = {'id': "STRING",'checkedBinding': "STRING"};
  data.buffer.push(escapeExpression(helpers.view.call(depth0, "Ember.Checkbox", {hash:{
    'id': ("special_needs"),
    'checkedBinding': ("special_needs_exp")
  },contexts:[depth0],types:["ID"],hashContexts:hashContexts,hashTypes:hashTypes,data:data})));
  data.buffer.push("<label for=\"special_needs\"></label></p>\n				  <p><span>add another (if not listed above):</span>");
  hashContexts = {'valueBinding': depth0};
  hashTypes = {'valueBinding': "STRING"};
  data.buffer.push(escapeExpression(helpers.view.call(depth0, "Ember.TextField", {hash:{
    'valueBinding': ("extra_exp")
  },contexts:[depth0],types:["ID"],hashContexts:hashContexts,hashTypes:hashTypes,data:data})));
  data.buffer.push("\n                  ");
  options = {hash:{},inverse:self.noop,fn:self.program(1, program1, data),contexts:[],types:[],hashContexts:hashContexts,hashTypes:hashTypes,data:data};
  if (stack1 = helpers.comment) { stack1 = stack1.call(depth0, options); }
  else { stack1 = depth0.comment; stack1 = typeof stack1 === functionType ? stack1.apply(depth0) : stack1; }
  hashTypes = {};
  hashContexts = {};
  if (!helpers.comment) { stack1 = blockHelperMissing.call(depth0, stack1, options); }
  if(stack1 || stack1 === 0) { data.buffer.push(stack1); }
  data.buffer.push("\n				</li>\n			  </ul>\n			</li>\n			<li>\n			  <ul>\n				<li><span class=\"icon_education3\">&nbsp;</span>Education Level</li>\n				<li>\n				  <p><span>Education level:</span>\n                  ");
  hashContexts = {'contentBinding': depth0,'selectionBinding': depth0};
  hashTypes = {'contentBinding': "ID",'selectionBinding': "STRING"};
  data.buffer.push(escapeExpression(helpers.view.call(depth0, "Sitterfied.Select2", {hash:{
    'contentBinding': ("Sitterfied.Educations"),
    'selectionBinding': ("highest_education")
  },contexts:[depth0],types:["ID"],hashContexts:hashContexts,hashTypes:hashTypes,data:data})));
  data.buffer.push("\n                  </p>\n				  <p><span>last school attended:</span>");
  hashContexts = {'placeholder': depth0,'valueBinding': depth0};
  hashTypes = {'placeholder': "STRING",'valueBinding': "STRING"};
  data.buffer.push(escapeExpression(helpers.view.call(depth0, "Ember.TextField", {hash:{
    'placeholder': ("School Name"),
    'valueBinding': ("last_school")
  },contexts:[depth0],types:["ID"],hashContexts:hashContexts,hashTypes:hashTypes,data:data})));
  data.buffer.push("</p>\n				  ");
  options = {hash:{},inverse:self.noop,fn:self.program(3, program3, data),contexts:[],types:[],hashContexts:hashContexts,hashTypes:hashTypes,data:data};
  if (stack1 = helpers.comment) { stack1 = stack1.call(depth0, options); }
  else { stack1 = depth0.comment; stack1 = typeof stack1 === functionType ? stack1.apply(depth0) : stack1; }
  hashTypes = {};
  hashContexts = {};
  if (!helpers.comment) { stack1 = blockHelperMissing.call(depth0, stack1, options); }
  if(stack1 || stack1 === 0) { data.buffer.push(stack1); }
  data.buffer.push("\n				    <p>\n\n                      <span>Still in school?</span>\n                      ");
  hashContexts = {'id': depth0,'selectionBinding': depth0,'value': depth0,'name': depth0};
  hashTypes = {'id': "STRING",'selectionBinding': "STRING",'value': "STRING",'name': "STRING"};
  data.buffer.push(escapeExpression(helpers.view.call(depth0, "Ember.RadioButton", {hash:{
    'id': ("yes3"),
    'selectionBinding': ("current_student"),
    'value': ("true"),
    'name': ("student")
  },contexts:[depth0],types:["ID"],hashContexts:hashContexts,hashTypes:hashTypes,data:data})));
  data.buffer.push("\n                      <label for=\"yes3\">YES</label>\n                      ");
  hashContexts = {'id': depth0,'selectionBinding': depth0,'value': depth0,'name': depth0};
  hashTypes = {'id': "STRING",'selectionBinding': "STRING",'value': "STRING",'name': "STRING"};
  data.buffer.push(escapeExpression(helpers.view.call(depth0, "Ember.RadioButton", {hash:{
    'id': ("no5"),
    'selectionBinding': ("current_student"),
    'value': ("false"),
    'name': ("student")
  },contexts:[depth0],types:["ID"],hashContexts:hashContexts,hashTypes:hashTypes,data:data})));
  data.buffer.push("\n                      <label for=\"no5\">NO</label>\n                    </p>\n				  <p><span>Major (if yes):</span>");
  hashContexts = {'placeholder': depth0,'valueBinding': depth0};
  hashTypes = {'placeholder': "STRING",'valueBinding': "STRING"};
  data.buffer.push(escapeExpression(helpers.view.call(depth0, "Ember.TextField", {hash:{
    'placeholder': ("major"),
    'valueBinding': ("major")
  },contexts:[depth0],types:["ID"],hashContexts:hashContexts,hashTypes:hashTypes,data:data})));
  data.buffer.push("</p>\n				  <p><span>occupation (if no):</span>");
  hashContexts = {'placeholder': depth0,'valueBinding': depth0};
  hashTypes = {'placeholder': "STRING",'valueBinding': "STRING"};
  data.buffer.push(escapeExpression(helpers.view.call(depth0, "Ember.TextField", {hash:{
    'placeholder': ("occupation"),
    'valueBinding': ("occupation")
  },contexts:[depth0],types:["ID"],hashContexts:hashContexts,hashTypes:hashTypes,data:data})));
  data.buffer.push("</p>\n				  <a class=\"button button_small\" ");
  hashTypes = {};
  hashContexts = {};
  data.buffer.push(escapeExpression(helpers.action.call(depth0, "saveSettings", {hash:{},contexts:[depth0],types:["STRING"],hashContexts:hashContexts,hashTypes:hashTypes,data:data})));
  data.buffer.push("><span class=\"icon_ok2\">&nbsp;</span>Save</a>\n				</li>\n			  </ul>\n			</li>\n			<li>\n			  <ul>\n				<li><span class=\"icon_certification3\">&nbsp;</span>Certification or Training</li>\n				<li>\n				  <p>\n                    <span>&nbsp;</span>\n                    ");
  hashContexts = {'contentBinding': depth0,'optionLabelPath': depth0,'optionValuePath': depth0,'selectionBinding': depth0,'multiple': depth0};
  hashTypes = {'contentBinding': "ID",'optionLabelPath': "STRING",'optionValuePath': "STRING",'selectionBinding': "STRING",'multiple': "STRING"};
  data.buffer.push(escapeExpression(helpers.view.call(depth0, "Sitterfied.Select2", {hash:{
    'contentBinding': ("Sitterfied.certificationsController"),
    'optionLabelPath': ("content.certification"),
    'optionValuePath': ("content.id"),
    'selectionBinding': ("certifications"),
    'multiple': ("multiple")
  },contexts:[depth0],types:["ID"],hashContexts:hashContexts,hashTypes:hashTypes,data:data})));
  data.buffer.push("\n                  </p>\n				  <p>\n                    <span>add another (if not listed above):</span>\n                    ");
  hashContexts = {'valueBinding': depth0};
  hashTypes = {'valueBinding': "STRING"};
  data.buffer.push(escapeExpression(helpers.view.call(depth0, "Ember.TextField", {hash:{
    'valueBinding': ("Sitterfied.certificationsController.newCert")
  },contexts:[depth0],types:["ID"],hashContexts:hashContexts,hashTypes:hashTypes,data:data})));
  data.buffer.push("\n                    <a class=\"button button_smaller button_edit certbutton\" ");
  hashTypes = {};
  hashContexts = {};
  data.buffer.push(escapeExpression(helpers.action.call(depth0, "saveCertification", {hash:{},contexts:[depth0],types:["STRING"],hashContexts:hashContexts,hashTypes:hashTypes,data:data})));
  data.buffer.push(">\n                      <span class=\"icon_plus\">&nbsp;</span>ADD\n                    </a>\n                  </p>\n				  <a class=\"button button_small\" href=\"#\"><span class=\"icon_ok2\">&nbsp;</span>Save</a>\n				</li>\n			  </ul>\n			</li>\n			<li>\n			  <ul>\n				<li><span class=\"icon_rates2\">&nbsp;</span>Standard Rates</li>\n				<li>\n				  <p><span>Minimum for 1 child:</span>");
  hashContexts = {'valueBinding': depth0};
  hashTypes = {'valueBinding': "STRING"};
  data.buffer.push(escapeExpression(helpers.view.call(depth0, "Ember.TextField", {hash:{
    'valueBinding': ("one_child_min_rate")
  },contexts:[depth0],types:["ID"],hashContexts:hashContexts,hashTypes:hashTypes,data:data})));
  data.buffer.push("</p>\n				  <p><span>Maximum for 1 child:</span>");
  hashContexts = {'valueBinding': depth0};
  hashTypes = {'valueBinding': "STRING"};
  data.buffer.push(escapeExpression(helpers.view.call(depth0, "Ember.TextField", {hash:{
    'valueBinding': ("one_child_max_rate")
  },contexts:[depth0],types:["ID"],hashContexts:hashContexts,hashTypes:hashTypes,data:data})));
  data.buffer.push("</p>\n				  <p><span>Minimum for 2 children:</span>");
  hashContexts = {'valueBinding': depth0};
  hashTypes = {'valueBinding': "STRING"};
  data.buffer.push(escapeExpression(helpers.view.call(depth0, "Ember.TextField", {hash:{
    'valueBinding': ("two_child_min_rate")
  },contexts:[depth0],types:["ID"],hashContexts:hashContexts,hashTypes:hashTypes,data:data})));
  data.buffer.push("</p>\n				  <p><span>Maximum for 2 children:</span>");
  hashContexts = {'valueBinding': depth0};
  hashTypes = {'valueBinding': "STRING"};
  data.buffer.push(escapeExpression(helpers.view.call(depth0, "Ember.TextField", {hash:{
    'valueBinding': ("two_child_max_rate")
  },contexts:[depth0],types:["ID"],hashContexts:hashContexts,hashTypes:hashTypes,data:data})));
  data.buffer.push("</p>\n				  <p><span>Minimum for 3 or more children</span>");
  hashContexts = {'valueBinding': depth0};
  hashTypes = {'valueBinding': "STRING"};
  data.buffer.push(escapeExpression(helpers.view.call(depth0, "Ember.TextField", {hash:{
    'valueBinding': ("three_child_min_rate")
  },contexts:[depth0],types:["ID"],hashContexts:hashContexts,hashTypes:hashTypes,data:data})));
  data.buffer.push("</p>\n				  <p><span>Maximum for 3 or more children</span>");
  hashContexts = {'valueBinding': depth0};
  hashTypes = {'valueBinding': "STRING"};
  data.buffer.push(escapeExpression(helpers.view.call(depth0, "Ember.TextField", {hash:{
    'valueBinding': ("three_child_max_rate")
  },contexts:[depth0],types:["ID"],hashContexts:hashContexts,hashTypes:hashTypes,data:data})));
  data.buffer.push("</p>\n				  <a class=\"button button_small\" ");
  hashTypes = {};
  hashContexts = {};
  data.buffer.push(escapeExpression(helpers.action.call(depth0, "saveSettings", {hash:{},contexts:[depth0],types:["STRING"],hashContexts:hashContexts,hashTypes:hashTypes,data:data})));
  data.buffer.push("><span class=\"icon_ok2\">&nbsp;</span>Save</a>\n				</li>\n			  </ul>\n			</li>\n			<li>\n			  <ul>\n				<li>\n                  <span class=\"icon_lng2\">&nbsp; </span>Languages\n                </li>\n				<li>\n				  <p>\n                    <span>I speak:</span>\n                   </p>\n                      ");
  hashContexts = {'contentBinding': depth0,'optionLabelPath': depth0,'optionValuePath': depth0,'selectionBinding': depth0,'multiple': depth0};
  hashTypes = {'contentBinding': "ID",'optionLabelPath': "STRING",'optionValuePath': "STRING",'selectionBinding': "STRING",'multiple': "STRING"};
  data.buffer.push(escapeExpression(helpers.view.call(depth0, "Sitterfied.Select2", {hash:{
    'contentBinding': ("Sitterfied.languagesController.content"),
    'optionLabelPath': ("content.language"),
    'optionValuePath': ("content.id"),
    'selectionBinding': ("languages"),
    'multiple': ("multiple")
  },contexts:[depth0],types:["ID"],hashContexts:hashContexts,hashTypes:hashTypes,data:data})));
  data.buffer.push("\n                    </p>\n				  <p><span>add another (if not listed above):</span>");
  hashContexts = {'valueBinding': depth0};
  hashTypes = {'valueBinding': "STRING"};
  data.buffer.push(escapeExpression(helpers.view.call(depth0, "Ember.TextField", {hash:{
    'valueBinding': ("Sitterfied.languagesController.newLanguage")
  },contexts:[depth0],types:["ID"],hashContexts:hashContexts,hashTypes:hashTypes,data:data})));
  data.buffer.push("<a class=\"button button_smaller button_edit\" ");
  hashTypes = {};
  hashContexts = {};
  data.buffer.push(escapeExpression(helpers.action.call(depth0, "saveLanguage", {hash:{},contexts:[depth0],types:["STRING"],hashContexts:hashContexts,hashTypes:hashTypes,data:data})));
  data.buffer.push("><span class=\"icon_plus\">&nbsp;</span>ADD</a></p>\n				</lpi>\n			  </ul>\n			</li>\n			<li>\n			  <ul>\n				<li><span class=\"icon_other2\">&nbsp;</span>Other Services</li>\n				<li>\n				    <p>\n                      <span>&nbsp;</span>\n                      ");
  hashContexts = {'contentBinding': depth0,'optionLabelPath': depth0,'optionValuePath': depth0,'selectionBinding': depth0,'multiple': depth0};
  hashTypes = {'contentBinding': "ID",'optionLabelPath': "STRING",'optionValuePath': "STRING",'selectionBinding': "STRING",'multiple': "STRING"};
  data.buffer.push(escapeExpression(helpers.view.call(depth0, "Sitterfied.Select2", {hash:{
    'contentBinding': ("Sitterfied.otherServicesController.content"),
    'optionLabelPath': ("content.service"),
    'optionValuePath': ("content.id"),
    'selectionBinding': ("other_services"),
    'multiple': ("multiple")
  },contexts:[depth0],types:["ID"],hashContexts:hashContexts,hashTypes:hashTypes,data:data})));
  data.buffer.push("`\n                    </p>\n				  <p><span>add another (if not listed above):</span>");
  hashContexts = {'valueBinding': depth0};
  hashTypes = {'valueBinding': "STRING"};
  data.buffer.push(escapeExpression(helpers.view.call(depth0, "Ember.TextField", {hash:{
    'valueBinding': ("Sitterfied.otherServicesController.newService")
  },contexts:[depth0],types:["ID"],hashContexts:hashContexts,hashTypes:hashTypes,data:data})));
  data.buffer.push("<a class=\"button button_smaller button_edit\" ");
  hashTypes = {};
  hashContexts = {};
  data.buffer.push(escapeExpression(helpers.action.call(depth0, "saveService", {hash:{},contexts:[depth0],types:["STRING"],hashContexts:hashContexts,hashTypes:hashTypes,data:data})));
  data.buffer.push("><span class=\"icon_plus\">&nbsp;</span>ADD</a></p>\n				  <a class=\"button button_small\" ");
  hashTypes = {};
  hashContexts = {};
  data.buffer.push(escapeExpression(helpers.action.call(depth0, "saveSettings", {hash:{},contexts:[depth0],types:["STRING"],hashContexts:hashContexts,hashTypes:hashTypes,data:data})));
  data.buffer.push("><span class=\"icon_ok2\">&nbsp;</span>Save</a>\n				</li>\n			  </ul>\n			</li>\n			<li>\n			  <ul>\n				<li><span class=\"icon_preferences2\">&nbsp;</span>Job Preferences</li>\n				<li class=\"long_headers\">\n				  <p>\n                    <span>Will you babysit in a home of smokers?</span>\n                    ");
  hashContexts = {'id': depth0,'selectionBinding': depth0,'value': depth0,'name': depth0};
  hashTypes = {'id': "STRING",'selectionBinding': "STRING",'value': "STRING",'name': "STRING"};
  data.buffer.push(escapeExpression(helpers.view.call(depth0, "Ember.RadioButton", {hash:{
    'id': ("yes4"),
    'selectionBinding': ("smokers_ok"),
    'value': ("true"),
    'name': ("pref")
  },contexts:[depth0],types:["ID"],hashContexts:hashContexts,hashTypes:hashTypes,data:data})));
  data.buffer.push("\n                    <label for=\"yes4\">YES</label>\n                    ");
  hashContexts = {'id': depth0,'selectionBinding': depth0,'value': depth0,'name': depth0};
  hashTypes = {'id': "STRING",'selectionBinding': "STRING",'value': "STRING",'name': "STRING"};
  data.buffer.push(escapeExpression(helpers.view.call(depth0, "Ember.RadioButton", {hash:{
    'id': ("no6"),
    'selectionBinding': ("smokers_ok"),
    'value': ("false"),
    'name': ("pref")
  },contexts:[depth0],types:["ID"],hashContexts:hashContexts,hashTypes:hashTypes,data:data})));
  data.buffer.push("\n                    <label for=\"no6\">NO</label>\n                  </p>\n				  <p>\n                    <span>Will you babysit in a home with dogs?                    </span>\n                    ");
  hashContexts = {'id': depth0,'selectionBinding': depth0,'value': depth0,'name': depth0};
  hashTypes = {'id': "STRING",'selectionBinding': "STRING",'value': "STRING",'name': "STRING"};
  data.buffer.push(escapeExpression(helpers.view.call(depth0, "Ember.RadioButton", {hash:{
    'id': ("yes5"),
    'selectionBinding': ("dogs_ok"),
    'value': ("true"),
    'name': ("pref2")
  },contexts:[depth0],types:["ID"],hashContexts:hashContexts,hashTypes:hashTypes,data:data})));
  data.buffer.push("\n                    <label for=\"yes5\">YES</label>\n                    ");
  hashContexts = {'id': depth0,'selectionBinding': depth0,'value': depth0,'name': depth0};
  hashTypes = {'id': "STRING",'selectionBinding': "STRING",'value': "STRING",'name': "STRING"};
  data.buffer.push(escapeExpression(helpers.view.call(depth0, "Ember.RadioButton", {hash:{
    'id': ("no7"),
    'selectionBinding': ("dogs_ok"),
    'value': ("false"),
    'name': ("pref2")
  },contexts:[depth0],types:["ID"],hashContexts:hashContexts,hashTypes:hashTypes,data:data})));
  data.buffer.push("\n                    <label for=\"no7\">NO</label>\n                  </p>\n				  <p>\n                    <span>Will you babysit in a home with cats?\n                    </span>\n                    ");
  hashContexts = {'id': depth0,'selectionBinding': depth0,'value': depth0,'name': depth0};
  hashTypes = {'id': "STRING",'selectionBinding': "STRING",'value': "STRING",'name': "STRING"};
  data.buffer.push(escapeExpression(helpers.view.call(depth0, "Ember.RadioButton", {hash:{
    'id': ("yes6"),
    'selectionBinding': ("cats_ok"),
    'value': ("true"),
    'name': ("pref3")
  },contexts:[depth0],types:["ID"],hashContexts:hashContexts,hashTypes:hashTypes,data:data})));
  data.buffer.push("\n                    <label for=\"yes6\">YES</label>\n                    ");
  hashContexts = {'id': depth0,'selectionBinding': depth0,'value': depth0,'name': depth0};
  hashTypes = {'id': "STRING",'selectionBinding': "STRING",'value': "STRING",'name': "STRING"};
  data.buffer.push(escapeExpression(helpers.view.call(depth0, "Ember.RadioButton", {hash:{
    'id': ("no8"),
    'selectionBinding': ("cats_ok"),
    'value': ("false"),
    'name': ("pref3")
  },contexts:[depth0],types:["ID"],hashContexts:hashContexts,hashTypes:hashTypes,data:data})));
  data.buffer.push("\n                    <label for=\"no8\">NO</label>\n                  </p>\n				  <p>\n                    <span>Will you babysit in a home that has other animals?</span>\n                    ");
  hashContexts = {'id': depth0,'selectionBinding': depth0,'value': depth0,'name': depth0};
  hashTypes = {'id': "STRING",'selectionBinding': "STRING",'value': "STRING",'name': "STRING"};
  data.buffer.push(escapeExpression(helpers.view.call(depth0, "Ember.RadioButton", {hash:{
    'id': ("yes7"),
    'selectionBinding': ("other_animals_ok"),
    'value': ("true"),
    'name': ("pref4")
  },contexts:[depth0],types:["ID"],hashContexts:hashContexts,hashTypes:hashTypes,data:data})));
  data.buffer.push("\n                    <label for=\"yes7\">YES</label>\n                    ");
  hashContexts = {'id': depth0,'selectionBinding': depth0,'value': depth0,'name': depth0};
  hashTypes = {'id': "STRING",'selectionBinding': "STRING",'value': "STRING",'name': "STRING"};
  data.buffer.push(escapeExpression(helpers.view.call(depth0, "Ember.RadioButton", {hash:{
    'id': ("no9"),
    'selectionBinding': ("other_animals_ok"),
    'value': ("false"),
    'name': ("pref4")
  },contexts:[depth0],types:["ID"],hashContexts:hashContexts,hashTypes:hashTypes,data:data})));
  data.buffer.push("\n                    <label for=\"no9\">NO</label>\n                  </p>\n				  <a class=\"button button_small\" ");
  hashTypes = {};
  hashContexts = {};
  data.buffer.push(escapeExpression(helpers.action.call(depth0, "saveSettings", {hash:{},contexts:[depth0],types:["STRING"],hashContexts:hashContexts,hashTypes:hashTypes,data:data})));
  data.buffer.push("><span class=\"icon_ok2\">&nbsp;</span>Save</a>\n				</li>\n			  </ul>\n			</li>\n		  </ul>\n		</form>\n	  </div>\n	  <!-- /profile_block -->\n");
  return buffer;
  
});
Ember.TEMPLATES["sitterEdit/top"] = Ember.Handlebars.template(function anonymous(Handlebars,depth0,helpers,partials,data) {
this.compilerInfo = [3,'>= 1.0.0-rc.4'];
helpers = helpers || Ember.Handlebars.helpers; data = data || {};
  var buffer = '', stack1, stack2, hashContexts, hashTypes, options, escapeExpression=this.escapeExpression, self=this, helperMissing=helpers.helperMissing;

function program1(depth0,data) {
  
  
  data.buffer.push("<span class=\"icon_eye\">&nbsp;</span>VIEW PROFILE");
  }

function program3(depth0,data) {
  
  
  data.buffer.push("Accept more booking requests");
  }

  data.buffer.push("<div class=\"top_info clear\">\n  <div class=\"member_since\">Feb 2013</div>\n  <div class=\"photo\">\n	<div class=\"photo_edit_wrap\">\n	  <img ");
  hashContexts = {'src': depth0};
  hashTypes = {'src': "ID"};
  data.buffer.push(escapeExpression(helpers.bindAttr.call(depth0, {hash:{
    'src': ("avatarUrl")
  },contexts:[],types:[],hashContexts:hashContexts,hashTypes:hashTypes,data:data})));
  data.buffer.push(" alt=\"\" />\n	  <p ");
  hashTypes = {};
  hashContexts = {};
  data.buffer.push(escapeExpression(helpers.action.call(depth0, "openPhotoPopup", {hash:{},contexts:[depth0],types:["STRING"],hashContexts:hashContexts,hashTypes:hashTypes,data:data})));
  data.buffer.push("><span class=\"icon_pen\">&nbsp;</span><a ");
  hashTypes = {};
  hashContexts = {};
  data.buffer.push(escapeExpression(helpers.action.call(depth0, "openPhotoPopup", {hash:{},contexts:[depth0],types:["STRING"],hashContexts:hashContexts,hashTypes:hashTypes,data:data})));
  data.buffer.push(">Edit Photo</a></p>\n	</div>\n  </div>\n  <div class=\"ranking_info\">\n	<p>");
  hashTypes = {};
  hashContexts = {};
  data.buffer.push(escapeExpression(helpers._triageMustache.call(depth0, "full_name", {hash:{},contexts:[depth0],types:["ID"],hashContexts:hashContexts,hashTypes:hashTypes,data:data})));
  data.buffer.push("</p>\n	<p>Ranking: <span>14th</span> of 137</p>\n	");
  hashContexts = {'class': depth0};
  hashTypes = {'class': "STRING"};
  options = {hash:{
    'class': ("db_button")
  },inverse:self.noop,fn:self.program(1, program1, data),contexts:[depth0,depth0],types:["ID","ID"],hashContexts:hashContexts,hashTypes:hashTypes,data:data};
  stack2 = ((stack1 = helpers.linkTo),stack1 ? stack1.call(depth0, "sitter", "", options) : helperMissing.call(depth0, "linkTo", "sitter", "", options));
  if(stack2 || stack2 === 0) { data.buffer.push(stack2); }
  data.buffer.push("\n	<fieldset>\n	  <legend>Here are some simple ways to improve your ranking:</legend>\n	  <ul class=\"clear\">\n		<li><a href=\"#\">Add more connections</a></li>\n		<li>");
  hashTypes = {};
  hashContexts = {};
  options = {hash:{},inverse:self.noop,fn:self.program(3, program3, data),contexts:[depth0],types:["ID"],hashContexts:hashContexts,hashTypes:hashTypes,data:data};
  stack2 = ((stack1 = helpers.linkTo),stack1 ? stack1.call(depth0, "sitterEdit.bookings", options) : helperMissing.call(depth0, "linkTo", "sitterEdit.bookings", options));
  if(stack2 || stack2 === 0) { data.buffer.push(stack2); }
  data.buffer.push("</li>\n		<li><a href=\"#\">Get more recommendations</a></li>\n	  </ul>\n	</fieldset>\n  </div>\n</div>\n<!-- /top info -->\n<!-- profile_completion -->\n<div class=\"profile_completion clear\" id=\"fixed_tabs\">\n  <p>Your profile is <span>ACTIVE</span> but incomplete</p>\n  <div><span>&nbsp;</span></div>\n  <p>Fill in the gaps below so parents can see how great you are!</p>\n</div>\n<!-- /profile_completion -->");
  return buffer;
  
});
Ember.TEMPLATES["sitterEdit/bookings"] = Ember.Handlebars.template(function anonymous(Handlebars,depth0,helpers,partials,data) {
this.compilerInfo = [3,'>= 1.0.0-rc.4'];
helpers = helpers || Ember.Handlebars.helpers; data = data || {};
  


  data.buffer.push("p	  <!-- bookings_block -->\n	  <div class=\"mob_tab_trigger\">Bookings</div>\n	  <div class=\"tab_content bookings_block\" id=\"tab-3\">\n		<ul class=\"subtab_select\">\n		  <li><a href=\"#tab-1-1\"><span>4</span>Pending Requests</a></li>\n		  <li><a href=\"#tab-1-2\"><span>3</span>Upcoming Jobs</a></li>\n		  <li><a href=\"#tab-1-3\"><span>7</span>Completed Jobs</a></li>\n		  <li><a href=\"#tab-1-4\"><span>12</span>Missed Requests</a></li>\n		  <li><a href=\"#tab-1-5\"><span>2</span>Expired Requests</a></li>\n		  <li><a href=\"#tab-1-6\"><span>3</span>Declined Jobs</a></li>\n		  <li><a href=\"#tab-1-7\"><span>2</span>Canceled Jobs</a></li>\n		</ul>\n\n		<div class=\"mob_tab_trigger active\"><span>4</span>Pending Requests</div>\n		<!-- pending_requests_block -->\n		<div class=\"subtab_content pending_requests_block\" id=\"tab-1-1\">\n		  <ul class=\"booking_list\">\n			<li>\n			  <header>\n				Request Sent: Friday 21 July 2012 at 4:40pm\n				<span>Job</span>\n			  </header>\n			  <div class=\"img\">\n				<a href=\"#\"><img src=\"/static/images/demo/img16.jpg\" alt=\"\" /></a>\n				<p><span><a href=\"#\">Jane E</a></span></p>\n				<div>\n				  <a href=\"#\">8 mutual friends</a>\n				  <ul>\n					<li>Friends you have in common</li>\n					<li><a href=\"#\"><img src=\"/static/images/demo/img3.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n					<li><a href=\"#\"><img src=\"/static/images/demo/img4.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n					<li><a href=\"#\"><img src=\"/static/images/demo/img5.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n					<li><a href=\"#\"><img src=\"/static/images/demo/img6.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n					<li><a href=\"#\"><img src=\"/static/images/demo/img7.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n					<li><a href=\"#\"><img src=\"/static/images/demo/img8.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n					<li><a href=\"#\"><img src=\"/static/images/demo/img9.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n					<li><a href=\"#\"><img src=\"/static/images/demo/img10.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n				  </ul>\n				</div>\n			  </div>\n			  <div class=\"desc clear\">\n				<ul>\n				  <li><span class=\"icon_date\">&nbsp;</span>Wednesday, August 1 &nbsp; <span>4:00 pm — 6:00 pm</span></li>\n				  <li><span class=\"icon_friends5\">&nbsp;</span>2 Kids</li>\n				  <li><span class=\"icon_pin3\">&nbsp;</span>New York, NY</li>\n				  <li>\n					<p><a href=\"#\">Need more info?<br />Email Jane.</a></p>\n					<span class=\"icon_email2\">&nbsp;</span><a href=\"mailto:jeyre@gmail.com\">jeyre@gmail.com</a>\n				  </li>\n				</ul>\n				<div class=\"price\"><span><strong>$</strong><input type=\"text\" value=\"25\" />/hr</span><a class=\"edit_button\" href=\"#\">edit</a></div>\n				<div class=\"btn_wrap\"><a class=\"button button_smaller\" href=\"#\"><span class=\"icon_ok2\">&nbsp;</span>ACCEPT</a><a class=\"button button_smaller button_cancel\" href=\"#\"><span class=\"icon_cancel\">&nbsp;</span>DECLINE</a></div>\n				<div class=\"note_wrap\"><a href=\"#\"><span class=\"show\">Show</span><span class=\"hide\">Hide</span> Note</a></div>\n			  </div>\n			  <div class=\"note_desc clear\">\n				<p>Nunc eu ullamcorper orci. Quisque eget odio ac lectus vestibulum faucibus eget in metus. In pellentesque faucibus vestibulum. Quisque eget odio ac lectus vestibulum faucibus eget in metus. </p>\n			  </div>\n			  <footer>\n				Request Sent: Friday 21 July 2012 at 4:40pm\n			  </footer>\n			</li>\n			<li>\n			  <header>\n				Request Sent: Friday 21 July 2012 at 4:40pm\n				<span>Job</span>\n			  </header>\n			  <div class=\"img\">\n				<a href=\"#\"><img src=\"/static/images/demo/img16.jpg\" alt=\"\" /></a>\n				<p><span><a href=\"#\">Jane E</a></span></p>\n				<div>\n				  <a href=\"#\">8 mutual friends</a>\n				  <ul>\n					<li>Friends you have in common</li>\n					<li><a href=\"#\"><img src=\"/static/images/demo/img3.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n					<li><a href=\"#\"><img src=\"/static/images/demo/img4.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n					<li><a href=\"#\"><img src=\"/static/images/demo/img5.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n					<li><a href=\"#\"><img src=\"/static/images/demo/img6.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n					<li><a href=\"#\"><img src=\"/static/images/demo/img7.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n					<li><a href=\"#\"><img src=\"/static/images/demo/img8.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n					<li><a href=\"#\"><img src=\"/static/images/demo/img9.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n					<li><a href=\"#\"><img src=\"/static/images/demo/img10.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n				  </ul>\n				</div>\n			  </div>\n			  <div class=\"desc clear\">\n				<ul>\n				  <li><span class=\"icon_date\">&nbsp;</span>Wednesday, August 1 &nbsp; <span>4:00 pm — 6:00 pm</span></li>\n				  <li><span class=\"icon_friends5\">&nbsp;</span>2 Kids</li>\n				  <li><span class=\"icon_pin3\">&nbsp;</span>New York, NY</li>\n				  <li>\n					<p><a href=\"#\">Need more info?<br />Email Jane.</a></p>\n					<span class=\"icon_email2\">&nbsp;</span><a href=\"mailto:jeyre@gmail.com\">jeyre@gmail.com</a>\n				  </li>\n				</ul>\n				<div class=\"price\"><span><strong>$</strong><input type=\"text\" value=\"25\" />/hr</span><a class=\"edit_button\" href=\"#\">edit</a></div>\n				<div class=\"btn_wrap\"><a class=\"button button_smaller\" href=\"#\"><span class=\"icon_ok2\">&nbsp;</span>ACCEPT</a><a class=\"button button_smaller button_cancel\" href=\"#\"><span class=\"icon_cancel\">&nbsp;</span>DECLINE</a></div>\n				<div class=\"note_wrap\"><a href=\"#\"><span class=\"show\">Show</span><span class=\"hide\">Hide</span> Note</a></div>\n			  </div>\n			  <div class=\"note_desc clear\">\n				<p>Nunc eu ullamcorper orci. Quisque eget odio ac lectus vestibulum faucibus eget in metus. In pellentesque faucibus vestibulum. Quisque eget odio ac lectus vestibulum faucibus eget in metus. </p>\n			  </div>\n			  <footer>\n				Request Sent: Friday 21 July 2012 at 4:40pm\n			  </footer>\n			</li>\n			<li>\n			  <header>\n				Request Sent: Friday 21 July 2012 at 4:40pm\n				<span>Interview</span>\n			  </header>\n			  <div class=\"img\">\n				<a href=\"#\"><img src=\"/static/images/demo/img16.jpg\" alt=\"\" /></a>\n				<p><span><a href=\"#\">Jane E</a></span></p>\n				<div>\n				  <a href=\"#\">8 mutual friends</a>\n				  <ul>\n					<li>Friends you have in common</li>\n					<li><a href=\"#\"><img src=\"/static/images/demo/img3.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n					<li><a href=\"#\"><img src=\"/static/images/demo/img4.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n					<li><a href=\"#\"><img src=\"/static/images/demo/img5.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n					<li><a href=\"#\"><img src=\"/static/images/demo/img6.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n					<li><a href=\"#\"><img src=\"/static/images/demo/img7.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n					<li><a href=\"#\"><img src=\"/static/images/demo/img8.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n					<li><a href=\"#\"><img src=\"/static/images/demo/img9.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n					<li><a href=\"#\"><img src=\"/static/images/demo/img10.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n				  </ul>\n				</div>\n			  </div>\n			  <div class=\"desc clear\">\n				<ul>\n				  <li><span class=\"icon_date\">&nbsp;</span>Wednesday, August 1 &nbsp; <span>4:00 pm — 6:00 pm</span></li>\n				  <li><span class=\"icon_friends5\">&nbsp;</span>2 Kids</li>\n				  <li><span class=\"icon_pin3\">&nbsp;</span>New York, NY</li>\n				  <li>\n					<p><a href=\"#\">Need more info?<br />Email Jane.</a></p>\n					<span class=\"icon_email2\">&nbsp;</span><a href=\"mailto:jeyre@gmail.com\">jeyre@gmail.com</a>\n				  </li>\n				</ul>\n				<div class=\"additional_info\">Meet Up</div>\n				<div class=\"btn_wrap\"><a class=\"button button_smaller\" href=\"#\"><span class=\"icon_ok2\">&nbsp;</span>ACCEPT</a><a class=\"button button_smaller button_cancel\" href=\"#\"><span class=\"icon_cancel\">&nbsp;</span>DECLINE</a></div>\n				<div class=\"note_wrap\"><a href=\"#\"><span class=\"show\">Show</span><span class=\"hide\">Hide</span> Note</a></div>\n			  </div>\n			  <div class=\"note_desc clear\">\n				<p>Nunc eu ullamcorper orci. Quisque eget odio ac lectus vestibulum faucibus eget in metus. In pellentesque faucibus vestibulum. Quisque eget odio ac lectus vestibulum faucibus eget in metus. </p>\n			  </div>\n			  <footer>\n				Request Sent: Friday 21 July 2012 at 4:40pm\n			  </footer>\n			</li>\n			<li>\n			  <header>\n				Request Sent: Friday 21 July 2012 at 4:40pm\n				<span>Interview</span>\n			  </header>\n			  <div class=\"img\">\n				<a href=\"#\"><img src=\"/static/images/demo/img16.jpg\" alt=\"\" /></a>\n				<p><span><a href=\"#\">Jane E</a></span></p>\n				<div>\n				  <a href=\"#\">8 mutual friends</a>\n				  <ul>\n					<li>Friends you have in common</li>\n					<li><a href=\"#\"><img src=\"/static/images/demo/img3.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n					<li><a href=\"#\"><img src=\"/static/images/demo/img4.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n					<li><a href=\"#\"><img src=\"/static/images/demo/img5.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n					<li><a href=\"#\"><img src=\"/static/images/demo/img6.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n					<li><a href=\"#\"><img src=\"/static/images/demo/img7.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n					<li><a href=\"#\"><img src=\"/static/images/demo/img8.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n					<li><a href=\"#\"><img src=\"/static/images/demo/img9.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n					<li><a href=\"#\"><img src=\"/static/images/demo/img10.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n				  </ul>\n				</div>\n			  </div>\n			  <div class=\"desc clear\">\n				<ul>\n				  <li><span class=\"icon_date\">&nbsp;</span>Wednesday, August 1 &nbsp; <span>4:00 pm — 6:00 pm</span></li>\n				  <li><span class=\"icon_friends5\">&nbsp;</span>2 Kids</li>\n				  <li><span class=\"icon_pin3\">&nbsp;</span>New York, NY</li>\n				  <li>\n					<p><a href=\"#\">Need more info?<br />Email Jane.</a></p>\n					<span class=\"icon_email2\">&nbsp;</span><a href=\"mailto:jeyre@gmail.com\">jeyre@gmail.com</a>\n				  </li>\n				</ul>\n				<div class=\"additional_info\">By Phone</div>\n				<div class=\"btn_wrap\"><a class=\"button button_smaller\" href=\"#\"><span class=\"icon_ok2\">&nbsp;</span>ACCEPT</a><a class=\"button button_smaller button_cancel\" href=\"#\"><span class=\"icon_cancel\">&nbsp;</span>DECLINE</a></div>\n				<div class=\"note_wrap\"><a href=\"#\"><span class=\"show\">Show</span><span class=\"hide\">Hide</span> Note</a></div>\n			  </div>\n			  <div class=\"note_desc clear\">\n				<p>Nunc eu ullamcorper orci. Quisque eget odio ac lectus vestibulum faucibus eget in metus. In pellentesque faucibus vestibulum. Quisque eget odio ac lectus vestibulum faucibus eget in metus. </p>\n			  </div>\n			  <footer>\n				Request Sent: Friday 21 July 2012 at 4:40pm\n			  </footer>\n			</li>\n		  </ul>\n		</div>\n		<!-- /pending_requests_block -->\n\n		<div class=\"mob_tab_trigger\"><span>3</span>Upcoming Jobs</div>\n		<!-- upcoming_jobs_block -->\n		<div class=\"subtab_content upcoming_jobs_block\" id=\"tab-1-2\">\n		  <ul class=\"booking_list\">\n			<li>\n			  <header>\n				Request Sent: Friday 21 July 2012 at 4:40pm\n				<span>Job</span>\n			  </header>\n			  <div class=\"img\">\n				<a href=\"#\"><img src=\"/static/images/demo/img16.jpg\" alt=\"\" /></a>\n				<p><span><a href=\"#\">Jane Eyre</a></span></p>\n				<div>\n				  <a href=\"#\">8 mutual friends</a>\n				  <ul>\n					<li>Friends you have in common</li>\n					<li><a href=\"#\"><img src=\"/static/images/demo/img3.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n					<li><a href=\"#\"><img src=\"/static/images/demo/img4.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n					<li><a href=\"#\"><img src=\"/static/images/demo/img5.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n					<li><a href=\"#\"><img src=\"/static/images/demo/img6.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n					<li><a href=\"#\"><img src=\"/static/images/demo/img7.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n					<li><a href=\"#\"><img src=\"/static/images/demo/img8.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n					<li><a href=\"#\"><img src=\"/static/images/demo/img9.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n					<li><a href=\"#\"><img src=\"/static/images/demo/img10.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n				  </ul>\n				</div>\n			  </div>\n			  <div class=\"desc clear\">\n				<ul>\n				  <li><span class=\"icon_date\">&nbsp;</span>Wednesday, August 1 &nbsp; <span>4:00 pm — 6:00 pm</span> <a href=\"#\" class=\"rlink\">Save to my calendar</a></li>\n				  <li><span class=\"icon_phone\">&nbsp;</span>(125) 898-6891</li>\n				  <li><span class=\"icon_email2\">&nbsp;</span><a href=\"mailto:jeyre@gmail.com\">jeyre@gmail.com</a> <a href=\"#\" class=\"rlink\">Add to my contacts</a></li>\n				  <li><span class=\"icon_pin3\">&nbsp;</span>33 Nassau Ave Suite #2 New York, NY <a href=\"#\" class=\"rlink\">Map this</a></li>\n				</ul>\n				<div class=\"children\"><span class=\"icon_friends5\">&nbsp;</span>2 Kids</div>\n				<div class=\"price\"><span><strong>$25</strong> /hr</span></div>\n				<div class=\"btn_wrap\"><a class=\"button button_smaller button_cancel\" href=\"#\"><span class=\"icon_cancel\">&nbsp;</span>CANCEL</a></div>\n				<div class=\"note_wrap\"><a href=\"#\"><span class=\"show\">Show</span><span class=\"hide\">Hide</span> Notes</a></div>\n			  </div>\n			  <div class=\"note_desc clear\">\n				<p>Nunc eu ullamcorper orci. Quisque eget odio ac lectus vestibulum faucibus eget in metus. In pellentesque faucibus vestibulum. Quisque eget odio ac lectus vestibulum faucibus eget in metus. </p>\n			  </div>\n			  <footer>\n				Request Sent: Friday 21 July 2012 at 4:40pm\n			  </footer>\n			</li>\n			<li>\n			  <header>\n				Request Sent: Friday 21 July 2012 at 4:40pm\n				<span>Interview</span>\n			  </header>\n			  <div class=\"img\">\n				<a href=\"#\"><img src=\"/static/images/demo/img16.jpg\" alt=\"\" /></a>\n				<p><span><a href=\"#\">Jane Eyre</a></span></p>\n				<div>\n				  <a href=\"#\">8 mutual friends</a>\n				  <ul>\n					<li>Friends you have in common</li>\n					<li><a href=\"#\"><img src=\"/static/images/demo/img3.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n					<li><a href=\"#\"><img src=\"/static/images/demo/img4.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n					<li><a href=\"#\"><img src=\"/static/images/demo/img5.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n					<li><a href=\"#\"><img src=\"/static/images/demo/img6.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n					<li><a href=\"#\"><img src=\"/static/images/demo/img7.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n					<li><a href=\"#\"><img src=\"/static/images/demo/img8.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n					<li><a href=\"#\"><img src=\"/static/images/demo/img9.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n					<li><a href=\"#\"><img src=\"/static/images/demo/img10.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n				  </ul>\n				</div>\n			  </div>\n			  <div class=\"desc clear\">\n				<ul>\n				  <li><span class=\"icon_date\">&nbsp;</span>Wednesday, August 1 &nbsp; <span>4:00 pm — 6:00 pm</span> <a href=\"#\" class=\"rlink\">Save to my calendar</a></li>\n				  <li><span class=\"icon_phone\">&nbsp;</span>(125) 898-6891</li>\n				  <li><span class=\"icon_email2\">&nbsp;</span><a href=\"mailto:jeyre@gmail.com\">jeyre@gmail.com</a> <a href=\"#\" class=\"rlink\">Add to my contacts</a></li>\n				  <li><span class=\"icon_pin3\">&nbsp;</span>33 Nassau Ave Suite #2 New York, NY <a href=\"#\" class=\"rlink\">Map this</a></li>\n				</ul>\n				<div class=\"children\"><span class=\"icon_friends5\">&nbsp;</span>2 Kids</div>\n				<div class=\"additional_info\">Meet Up</div>\n				<div class=\"btn_wrap\"><a class=\"button button_smaller button_cancel\" href=\"#\"><span class=\"icon_cancel\">&nbsp;</span>CANCEL</a></div>\n				<div class=\"note_wrap\"><a href=\"#\"><span class=\"show\">Show</span><span class=\"hide\">Hide</span> Notes</a></div>\n			  </div>\n			  <div class=\"note_desc clear\">\n				<p>Nunc eu ullamcorper orci. Quisque eget odio ac lectus vestibulum faucibus eget in metus. In pellentesque faucibus vestibulum. Quisque eget odio ac lectus vestibulum faucibus eget in metus. </p>\n			  </div>\n			  <footer>\n				Request Sent: Friday 21 July 2012 at 4:40pm\n			  </footer>\n			</li>\n		  </ul>\n		</div>\n		<!-- /upcoming_jobs_block -->\n\n		<div class=\"mob_tab_trigger\"><span>7</span>Completed Jobs</div>\n		<!-- completed_jobs_block -->\n		<div class=\"subtab_content completed_jobs_block\" id=\"tab-1-3\">\n		  Completed Jobs\n		</div>\n		<!-- /completed_jobs_block -->\n\n		<div class=\"mob_tab_trigger\"><span>12</span>Missed Requests</div>\n		<!-- missed_requests_block -->\n		<div class=\"subtab_content missed_requests_block\" id=\"tab-1-4\">\n		  Missed Requests\n		</div>\n		<!-- /missed_requests_block -->\n\n		<div class=\"mob_tab_trigger\"><span>2</span>Expired Requests</div>\n		<!-- expired_requests_block -->\n		<div class=\"subtab_content expired_requests_block\" id=\"tab-1-5\">\n		  Expired Requests\n		</div>\n		<!-- /expired_requests_block -->\n\n		<div class=\"mob_tab_trigger\"><span>3</span>Declined Jobs</div>\n		<!-- declined_jobs_block -->\n		<div class=\"subtab_content declined_jobs_block\" id=\"tab-1-6\">\n		  Declined Jobs\n		</div>\n		<!-- /declined_jobs_block -->\n\n		<div class=\"mob_tab_trigger\"><span>2</span>Canceled Jobs</div>\n		<!-- canceled_jobs_block -->\n		<div class=\"subtab_content canceled_jobs_block\" id=\"tab-1-7\">\n		  Canceled Jobs\n		</div>\n		<!-- /canceled_jobs_block -->\n	  </div>\n	  <!-- /bookings_block -->\n");
  
});
Ember.TEMPLATES["sitterEdit"] = Ember.Handlebars.template(function anonymous(Handlebars,depth0,helpers,partials,data) {
this.compilerInfo = [3,'>= 1.0.0-rc.4'];
helpers = helpers || Ember.Handlebars.helpers; data = data || {};
  var buffer = '', stack1, stack2, hashTypes, hashContexts, options, self=this, helperMissing=helpers.helperMissing, escapeExpression=this.escapeExpression;

function program1(depth0,data) {
  
  
  data.buffer.push("Profile");
  }

function program3(depth0,data) {
  
  
  data.buffer.push("Schedule");
  }

function program5(depth0,data) {
  
  
  data.buffer.push("Bookings");
  }

function program7(depth0,data) {
  
  
  data.buffer.push("Network");
  }

function program9(depth0,data) {
  
  
  data.buffer.push("Reviews");
  }

  data.buffer.push("<!-- container -->\n<div class=\"container clear\">\n  <div class=\"wraper\">\n\n	<!-- tabs_wrap -->\n	<div class=\"tabs_wrap\">\n	  <ul class=\"tab_select\">\n		<li>");
  hashTypes = {};
  hashContexts = {};
  options = {hash:{},inverse:self.noop,fn:self.program(1, program1, data),contexts:[depth0],types:["ID"],hashContexts:hashContexts,hashTypes:hashTypes,data:data};
  stack2 = ((stack1 = helpers.linkTo),stack1 ? stack1.call(depth0, "sitterEdit.profile", options) : helperMissing.call(depth0, "linkTo", "sitterEdit.profile", options));
  if(stack2 || stack2 === 0) { data.buffer.push(stack2); }
  data.buffer.push("</li>\n		<li>");
  hashTypes = {};
  hashContexts = {};
  options = {hash:{},inverse:self.noop,fn:self.program(3, program3, data),contexts:[depth0],types:["ID"],hashContexts:hashContexts,hashTypes:hashTypes,data:data};
  stack2 = ((stack1 = helpers.linkTo),stack1 ? stack1.call(depth0, "sitterEdit.schedlue", options) : helperMissing.call(depth0, "linkTo", "sitterEdit.schedlue", options));
  if(stack2 || stack2 === 0) { data.buffer.push(stack2); }
  data.buffer.push("</li>\n		<li>");
  hashTypes = {};
  hashContexts = {};
  options = {hash:{},inverse:self.noop,fn:self.program(5, program5, data),contexts:[depth0],types:["ID"],hashContexts:hashContexts,hashTypes:hashTypes,data:data};
  stack2 = ((stack1 = helpers.linkTo),stack1 ? stack1.call(depth0, "sitterEdit.bookings", options) : helperMissing.call(depth0, "linkTo", "sitterEdit.bookings", options));
  if(stack2 || stack2 === 0) { data.buffer.push(stack2); }
  data.buffer.push("</li>\n		<li>");
  hashTypes = {};
  hashContexts = {};
  options = {hash:{},inverse:self.noop,fn:self.program(7, program7, data),contexts:[depth0],types:["ID"],hashContexts:hashContexts,hashTypes:hashTypes,data:data};
  stack2 = ((stack1 = helpers.linkTo),stack1 ? stack1.call(depth0, "sitterEdit.network", options) : helperMissing.call(depth0, "linkTo", "sitterEdit.network", options));
  if(stack2 || stack2 === 0) { data.buffer.push(stack2); }
  data.buffer.push("</li>\n		<li>");
  hashTypes = {};
  hashContexts = {};
  options = {hash:{},inverse:self.noop,fn:self.program(9, program9, data),contexts:[depth0],types:["ID"],hashContexts:hashContexts,hashTypes:hashTypes,data:data};
  stack2 = ((stack1 = helpers.linkTo),stack1 ? stack1.call(depth0, "sitterEdit.reviews", options) : helperMissing.call(depth0, "linkTo", "sitterEdit.reviews", options));
  if(stack2 || stack2 === 0) { data.buffer.push(stack2); }
  data.buffer.push("</li>\n	  </ul>\n\n\n      ");
  hashTypes = {};
  hashContexts = {};
  data.buffer.push(escapeExpression(helpers._triageMustache.call(depth0, "outlet", {hash:{},contexts:[depth0],types:["ID"],hashContexts:hashContexts,hashTypes:hashTypes,data:data})));
  data.buffer.push("\n\n	</div>\n	<!-- /tabs_wrap -->\n\n  </div>\n</div>\n<!-- /container -->");
  return buffer;
  
});
Ember.TEMPLATES["sitterEdit/reviews"] = Ember.Handlebars.template(function anonymous(Handlebars,depth0,helpers,partials,data) {
this.compilerInfo = [3,'>= 1.0.0-rc.4'];
helpers = helpers || Ember.Handlebars.helpers; data = data || {};
  var buffer = '', stack1, hashTypes, hashContexts, helperMissing=helpers.helperMissing, escapeExpression=this.escapeExpression, self=this;

function program1(depth0,data) {
  
  var buffer = '', stack1, hashTypes, hashContexts, options;
  data.buffer.push("\n            ");
  hashTypes = {};
  hashContexts = {};
  options = {hash:{},contexts:[depth0],types:["STRING"],hashContexts:hashContexts,hashTypes:hashTypes,data:data};
  data.buffer.push(escapeExpression(((stack1 = helpers.partial),stack1 ? stack1.call(depth0, "review", options) : helperMissing.call(depth0, "partial", "review", options))));
  data.buffer.push("\n          ");
  return buffer;
  }

  data.buffer.push("	  <!-- reviews_block -->\n	  <div class=\"mob_tab_trigger\">Reviews</div>\n	  <div class=\"tab_content reviews_block\" id=\"tab-5\">\n		<div class=\"reco clear\"><a ");
  hashTypes = {};
  hashContexts = {};
  data.buffer.push(escapeExpression(helpers.action.call(depth0, "openReccomendPopup", {hash:{},contexts:[depth0],types:["STRING"],hashContexts:hashContexts,hashTypes:hashTypes,data:data})));
  data.buffer.push("><span class=\"icon_team2\">&nbsp;</span>REQUEST RECOMMENDATION</a></div>\n		<ul class=\"clear\">\n          ");
  hashTypes = {};
  hashContexts = {};
  stack1 = helpers.each.call(depth0, "reviews", {hash:{},inverse:self.noop,fn:self.program(1, program1, data),contexts:[depth0],types:["ID"],hashContexts:hashContexts,hashTypes:hashTypes,data:data});
  if(stack1 || stack1 === 0) { data.buffer.push(stack1); }
  data.buffer.push("\n		</ul>\n	  </div>\n	  <!-- /reviews_block -->\n");
  return buffer;
  
});
Ember.TEMPLATES["settings/top"] = Ember.Handlebars.template(function anonymous(Handlebars,depth0,helpers,partials,data) {
this.compilerInfo = [3,'>= 1.0.0-rc.4'];
helpers = helpers || Ember.Handlebars.helpers; data = data || {};
  


  data.buffer.push("<div class=\"top_title clear\">\n  <span class=\"icon_settings\">&nbsp;</span>My Account Settings\n</div>");
  
});
Ember.TEMPLATES["settings"] = Ember.Handlebars.template(function anonymous(Handlebars,depth0,helpers,partials,data) {
this.compilerInfo = [3,'>= 1.0.0-rc.4'];
helpers = helpers || Ember.Handlebars.helpers; data = data || {};
  var buffer = '', stack1, hashContexts, hashTypes, escapeExpression=this.escapeExpression, self=this, helperMissing=helpers.helperMissing;

function program1(depth0,data) {
  
  
  data.buffer.push("\n			    <a class=\"button button_smaller button_edit\" href=\"#\"><span class=\"icon_settings2\">&nbsp;</span>PAYMENT OPTIONS</a>\n                ");
  }

function program3(depth0,data) {
  
  
  data.buffer.push("\n                <span class=\"ur\">You are <strong>Sitterfied</strong></span>\n                ");
  }

function program5(depth0,data) {
  
  var buffer = '', stack1, stack2, hashTypes, hashContexts, options;
  data.buffer.push("\n		<ul class=\"clear\">\n		  <li>Mobile Phone</li>\n		  <li>\n			<p class=\"mobile_info\"><span>(123) 456-7890</span>You can edit the phone number on your account from your ");
  hashTypes = {};
  hashContexts = {};
  options = {hash:{},inverse:self.noop,fn:self.program(6, program6, data),contexts:[depth0],types:["ID"],hashContexts:hashContexts,hashTypes:hashTypes,data:data};
  stack2 = ((stack1 = helpers.linkTo),stack1 ? stack1.call(depth0, "profile", options) : helperMissing.call(depth0, "linkTo", "profile", options));
  if(stack2 || stack2 === 0) { data.buffer.push(stack2); }
  data.buffer.push("</p>\n		  </li>\n		  <li>Notify me when</li>\n		  <li>\n              ");
  hashTypes = {};
  hashContexts = {};
  stack2 = helpers['if'].call(depth0, "Sitterfied.isParent", {hash:{},inverse:self.program(10, program10, data),fn:self.program(8, program8, data),contexts:[depth0],types:["ID"],hashContexts:hashContexts,hashTypes:hashTypes,data:data});
  if(stack2 || stack2 === 0) { data.buffer.push(stack2); }
  data.buffer.push("\n		  </li>\n		  <li>Remind me when</li>\n		  <li>\n			<p>");
  hashContexts = {'id': depth0,'checkedBinding': depth0};
  hashTypes = {'id': "STRING",'checkedBinding': "STRING"};
  data.buffer.push(escapeExpression(helpers.view.call(depth0, "Ember.Checkbox", {hash:{
    'id': ("mn_check4"),
    'checkedBinding': ("mobile_upcoming_booking_remind")
  },contexts:[depth0],types:["ID"],hashContexts:hashContexts,hashTypes:hashTypes,data:data})));
  data.buffer.push("<label for=\"mn_check4\">I have an upcoming booking</label></p>\n		  </li>\n		  <li><a class=\"button button_small\" ");
  hashTypes = {};
  hashContexts = {};
  data.buffer.push(escapeExpression(helpers.action.call(depth0, "saveSettings", {hash:{},contexts:[depth0],types:["STRING"],hashContexts:hashContexts,hashTypes:hashTypes,data:data})));
  data.buffer.push("><span class=\"icon_ok2\">&nbsp;</span>Save</a></li>\n		</ul>\n		<h4><span class=\"icon_eset\">&nbsp;</span>Email Settings</h4>\n        <p>We will never spam. Enabling these emails ensures the best possible experience on Sitterfied but feel free to disable at any time.</p>\n		<ul class=\"clear\">\n		  <li>Notify me when</li>\n		  <li>\n            ");
  hashTypes = {};
  hashContexts = {};
  stack2 = helpers['if'].call(depth0, "Sitterfied.isParent", {hash:{},inverse:self.program(14, program14, data),fn:self.program(12, program12, data),contexts:[depth0],types:["ID"],hashContexts:hashContexts,hashTypes:hashTypes,data:data});
  if(stack2 || stack2 === 0) { data.buffer.push(stack2); }
  data.buffer.push("\n		  </li>\n		  <li>Remind me when</li>\n		  <li>\n			<p>");
  hashContexts = {'id': depth0,'checkedBinding': depth0};
  hashTypes = {'id': "STRING",'checkedBinding': "STRING"};
  data.buffer.push(escapeExpression(helpers.view.call(depth0, "Ember.Checkbox", {hash:{
    'id': ("es_check4"),
    'checkedBinding': ("email_upcoming_booking_remind")
  },contexts:[depth0],types:["ID"],hashContexts:hashContexts,hashTypes:hashTypes,data:data})));
  data.buffer.push("<label for=\"es_check4\">I have an upcoming booking</label></p>\n		  </li>\n		  <li>EMAIL me when</li>\n		  <li>\n			<p>");
  hashContexts = {'id': depth0,'checkedBinding': depth0};
  hashTypes = {'id': "STRING",'checkedBinding': "STRING"};
  data.buffer.push(escapeExpression(helpers.view.call(depth0, "Ember.Checkbox", {hash:{
    'id': ("es_check5"),
    'checkedBinding': ("email_news")
  },contexts:[depth0],types:["ID"],hashContexts:hashContexts,hashTypes:hashTypes,data:data})));
  data.buffer.push("<label for=\"es_check5\">Sitterfied has fun company news, as well as periodic emails</label></p>\n			<p>");
  hashContexts = {'id': depth0,'checkedBinding': depth0};
  hashTypes = {'id': "STRING",'checkedBinding': "STRING"};
  data.buffer.push(escapeExpression(helpers.view.call(depth0, "Ember.Checkbox", {hash:{
    'id': ("es_check6"),
    'checkedBinding': ("email_blog")
  },contexts:[depth0],types:["ID"],hashContexts:hashContexts,hashTypes:hashTypes,data:data})));
  data.buffer.push("<label for=\"es_check6\">There’s a new blog post</label></p>\n		  </li>\n		  <li><a class=\"button button_small\" ");
  hashTypes = {};
  hashContexts = {};
  data.buffer.push(escapeExpression(helpers.action.call(depth0, "saveSettings", {hash:{},contexts:[depth0],types:["STRING"],hashContexts:hashContexts,hashTypes:hashTypes,data:data})));
  data.buffer.push("><span class=\"icon_ok2\">&nbsp;</span>Save</a></li>\n\n		</ul>\n        ");
  return buffer;
  }
function program6(depth0,data) {
  
  
  data.buffer.push("profile page");
  }

function program8(depth0,data) {
  
  var buffer = '', hashContexts, hashTypes;
  data.buffer.push("\n			    <p>");
  hashContexts = {'id': depth0,'checkedBinding': depth0};
  hashTypes = {'id': "STRING",'checkedBinding': "STRING"};
  data.buffer.push(escapeExpression(helpers.view.call(depth0, "Ember.Checkbox", {hash:{
    'id': ("mn_check"),
    'checkedBinding': ("mobile_booking_accepted_denied")
  },contexts:[depth0],types:["ID"],hashContexts:hashContexts,hashTypes:hashTypes,data:data})));
  data.buffer.push("<label for=\"mn_check\">My outstanding booking request is accepted or declined</label></p>\n			    <p>");
  hashContexts = {'id': depth0,'checkedBinding': depth0};
  hashTypes = {'id': "STRING",'checkedBinding': "STRING"};
  data.buffer.push(escapeExpression(helpers.view.call(depth0, "Ember.Checkbox", {hash:{
    'id': ("mn_check2"),
    'checkedBinding': ("mobile_friend_joined")
  },contexts:[depth0],types:["ID"],hashContexts:hashContexts,hashTypes:hashTypes,data:data})));
  data.buffer.push("<label for=\"mn_check2\">A Facebook or Gmail friend has joined Sitterfied</label></p>\n			    <p>");
  hashContexts = {'id': depth0,'checkedBinding': depth0};
  hashTypes = {'id': "STRING",'checkedBinding': "STRING"};
  data.buffer.push(escapeExpression(helpers.view.call(depth0, "Ember.Checkbox", {hash:{
    'id': ("mn_check3"),
    'checkedBinding': ("mobile_groups_added_network")
  },contexts:[depth0],types:["ID"],hashContexts:hashContexts,hashTypes:hashTypes,data:data})));
  data.buffer.push("<label for=\"mn_check3\">Someone has added one of my groups to their network</label></p>\n                ");
  return buffer;
  }

function program10(depth0,data) {
  
  var buffer = '', hashContexts, hashTypes;
  data.buffer.push("\n                <p>");
  hashContexts = {'id': depth0,'checkedBinding': depth0};
  hashTypes = {'id': "STRING",'checkedBinding': "STRING"};
  data.buffer.push(escapeExpression(helpers.view.call(depth0, "Ember.Checkbox", {hash:{
    'id': ("mn_check"),
    'checkedBinding': ("mobile_booking_request")
  },contexts:[depth0],types:["ID"],hashContexts:hashContexts,hashTypes:hashTypes,data:data})));
  data.buffer.push("<label for=\"mn_check\">I receive a booking request</label></p>\n			    <p>");
  hashContexts = {'id': depth0,'checkedBinding': depth0};
  hashTypes = {'id': "STRING",'checkedBinding': "STRING"};
  data.buffer.push(escapeExpression(helpers.view.call(depth0, "Ember.Checkbox", {hash:{
    'id': ("mn_check5"),
    'checkedBinding': ("mobile_new_reivew")
  },contexts:[depth0],types:["ID"],hashContexts:hashContexts,hashTypes:hashTypes,data:data})));
  data.buffer.push("<label for=\"mn_check5\">A new review has been added</label></p>\n			    <p>");
  hashContexts = {'id': depth0,'checkedBinding': depth0};
  hashTypes = {'id': "STRING",'checkedBinding': "STRING"};
  data.buffer.push(escapeExpression(helpers.view.call(depth0, "Ember.Checkbox", {hash:{
    'id': ("mn_check2"),
    'checkedBinding': ("mobile_friend_joined")
  },contexts:[depth0],types:["ID"],hashContexts:hashContexts,hashTypes:hashTypes,data:data})));
  data.buffer.push("<label for=\"mn_check2\">A Facebook or Gmail friend has joined Sitterfied</label></p>\n			    <p>");
  hashContexts = {'id': depth0,'checkedBinding': depth0};
  hashTypes = {'id': "STRING",'checkedBinding': "STRING"};
  data.buffer.push(escapeExpression(helpers.view.call(depth0, "Ember.Checkbox", {hash:{
    'id': ("mn_check3"),
    'checkedBinding': ("mobile_groups_added_network")
  },contexts:[depth0],types:["ID"],hashContexts:hashContexts,hashTypes:hashTypes,data:data})));
  data.buffer.push("<label for=\"mn_check3\">Someone has added one of my groups to their network</label></p>\n                ");
  return buffer;
  }

function program12(depth0,data) {
  
  var buffer = '', hashContexts, hashTypes;
  data.buffer.push("\n			  <p>");
  hashContexts = {'id': depth0,'checkedBinding': depth0};
  hashTypes = {'id': "STRING",'checkedBinding': "STRING"};
  data.buffer.push(escapeExpression(helpers.view.call(depth0, "Ember.Checkbox", {hash:{
    'id': ("es_check"),
    'checkedBinding': ("email_booking_accepted_denied")
  },contexts:[depth0],types:["ID"],hashContexts:hashContexts,hashTypes:hashTypes,data:data})));
  data.buffer.push("<label for=\"es_check\">My outstanding booking request is accepted or declined</label></p>\n			  <p>");
  hashContexts = {'id': depth0,'checkedBinding': depth0};
  hashTypes = {'id': "STRING",'checkedBinding': "STRING"};
  data.buffer.push(escapeExpression(helpers.view.call(depth0, "Ember.Checkbox", {hash:{
    'id': ("es_check2"),
    'checkedBinding': ("email_friend_joined")
  },contexts:[depth0],types:["ID"],hashContexts:hashContexts,hashTypes:hashTypes,data:data})));
  data.buffer.push("<label for=\"es_check2\">A Facebook or Gmail friend has joined Sitterfied</label></p>\n			  <p>");
  hashContexts = {'id': depth0,'checkedBinding': depth0};
  hashTypes = {'id': "STRING",'checkedBinding': "STRING"};
  data.buffer.push(escapeExpression(helpers.view.call(depth0, "Ember.Checkbox", {hash:{
    'id': ("es_check3"),
    'checkedBinding': ("email_groups_added_network")
  },contexts:[depth0],types:["ID"],hashContexts:hashContexts,hashTypes:hashTypes,data:data})));
  data.buffer.push("<label for=\"es_check3\">Someone has added one of my groups to their network</label></p>\n              ");
  return buffer;
  }

function program14(depth0,data) {
  
  var buffer = '', hashContexts, hashTypes;
  data.buffer.push("\n              <p>");
  hashContexts = {'id': depth0,'checkedBinding': depth0};
  hashTypes = {'id': "STRING",'checkedBinding': "STRING"};
  data.buffer.push(escapeExpression(helpers.view.call(depth0, "Ember.Checkbox", {hash:{
    'id': ("es_check"),
    'checkedBinding': ("email_booking_request")
  },contexts:[depth0],types:["ID"],hashContexts:hashContexts,hashTypes:hashTypes,data:data})));
  data.buffer.push("<label for=\"es_check\">I receive a booking request</label></p>\n			  <p>");
  hashContexts = {'id': depth0,'checkedBinding': depth0};
  hashTypes = {'id': "STRING",'checkedBinding': "STRING"};
  data.buffer.push(escapeExpression(helpers.view.call(depth0, "Ember.Checkbox", {hash:{
    'id': ("es_check7"),
    'checkedBinding': ("email_new_review")
  },contexts:[depth0],types:["ID"],hashContexts:hashContexts,hashTypes:hashTypes,data:data})));
  data.buffer.push("<label for=\"es_check7\">A new review has been added</label></p>\n			  <p>");
  hashContexts = {'id': depth0,'checkedBinding': depth0};
  hashTypes = {'id': "STRING",'checkedBinding': "STRING"};
  data.buffer.push(escapeExpression(helpers.view.call(depth0, "Ember.Checkbox", {hash:{
    'id': ("es_check2"),
    'checkedBinding': ("email_friend_joined")
  },contexts:[depth0],types:["ID"],hashContexts:hashContexts,hashTypes:hashTypes,data:data})));
  data.buffer.push("<label for=\"es_check2\">A Facebook or Gmail friend has joined Sitterfied</label></p>\n			  <p>");
  hashContexts = {'id': depth0,'checkedBinding': depth0};
  hashTypes = {'id': "STRING",'checkedBinding': "STRING"};
  data.buffer.push(escapeExpression(helpers.view.call(depth0, "Ember.Checkbox", {hash:{
    'id': ("es_check3"),
    'checkedBinding': ("email_groups_added_network")
  },contexts:[depth0],types:["ID"],hashContexts:hashContexts,hashTypes:hashTypes,data:data})));
  data.buffer.push("<label for=\"es_check3\">Someone has added one of my groups to their network</label></p>\n              ");
  return buffer;
  }

  data.buffer.push("<div class=\"container clear\">\n  <div class=\"wraper settings_topmarg\">\n\n	<!-- account_settings_block -->\n	<div class=\"account_settings_block clear\">\n	  <form class=\"form_style\">\n		<div class=\"left\">\n		  <ul>\n			<li><label for=\"\">NAME</label></li>\n			<li><p>");
  hashContexts = {'valueBinding': depth0};
  hashTypes = {'valueBinding': "STRING"};
  data.buffer.push(escapeExpression(helpers.view.call(depth0, "Ember.TextField", {hash:{
    'valueBinding': ("full_name")
  },contexts:[depth0],types:["ID"],hashContexts:hashContexts,hashTypes:hashTypes,data:data})));
  data.buffer.push("</p></li>\n			<li><label for=\"\">STATUS</label></li>\n			<li>\n			  <div class=\"member_since\">Feb 2013</div>\n              ");
  hashTypes = {};
  hashContexts = {};
  stack1 = helpers['if'].call(depth0, "isParent", {hash:{},inverse:self.program(3, program3, data),fn:self.program(1, program1, data),contexts:[depth0],types:["ID"],hashContexts:hashContexts,hashTypes:hashTypes,data:data});
  if(stack1 || stack1 === 0) { data.buffer.push(stack1); }
  data.buffer.push("\n			</li>\n		  </ul>\n		</div>\n		<div class=\"right\">\n		  <ul>\n			<li><label for=\"\">PASSWORD</label></li>\n			<li><p>");
  hashContexts = {'type': depth0,'valueBinding': depth0};
  hashTypes = {'type': "STRING",'valueBinding': "STRING"};
  data.buffer.push(escapeExpression(helpers.view.call(depth0, "Ember.TextField", {hash:{
    'type': ("password"),
    'valueBinding': ("old_password")
  },contexts:[depth0],types:["ID"],hashContexts:hashContexts,hashTypes:hashTypes,data:data})));
  data.buffer.push("</p></li>\n			<li><label for=\"\">NEW PASSWORD</label></li>\n			<li><p>");
  hashContexts = {'type': depth0,'valueBinding': depth0};
  hashTypes = {'type': "STRING",'valueBinding': "STRING"};
  data.buffer.push(escapeExpression(helpers.view.call(depth0, "Ember.TextField", {hash:{
    'type': ("password"),
    'valueBinding': ("new_password1")
  },contexts:[depth0],types:["ID"],hashContexts:hashContexts,hashTypes:hashTypes,data:data})));
  data.buffer.push("</p></li>\n			<li><label for=\"\">NEW PASSWORD (CONFIRM)</label></li>\n			<li><p>");
  hashContexts = {'type': depth0,'valueBinding': depth0};
  hashTypes = {'type': "STRING",'valueBinding': "STRING"};
  data.buffer.push(escapeExpression(helpers.view.call(depth0, "Ember.TextField", {hash:{
    'type': ("password"),
    'valueBinding': ("new_password2")
  },contexts:[depth0],types:["ID"],hashContexts:hashContexts,hashTypes:hashTypes,data:data})));
  data.buffer.push("</p></li>\n			<li><a class=\"button button_small button_cancel\" ");
  hashTypes = {};
  hashContexts = {};
  data.buffer.push(escapeExpression(helpers.action.call(depth0, "resetPassword", {hash:{},contexts:[depth0],types:["STRING"],hashContexts:hashContexts,hashTypes:hashTypes,data:data})));
  data.buffer.push(">Reset</a></li>\n		  </ul>\n		</div>\n		<p><a ");
  hashTypes = {};
  hashContexts = {};
  data.buffer.push(escapeExpression(helpers.action.call(depth0, "deleteAccount", {hash:{},contexts:[depth0],types:["STRING"],hashContexts:hashContexts,hashTypes:hashTypes,data:data})));
  data.buffer.push(">DELETE MY ACCOUNT</a> Having problems? <strong><a href=\"mailto:hello@sitterfied.com\">talk to us</a></strong>. Maybe we can work this out.</p>\n		<h4><span class=\"icon_mobile\">&nbsp;</span>Mobile Notifications / Text Messages</h4>\n        ");
  hashTypes = {};
  hashContexts = {};
  stack1 = helpers['with'].call(depth0, "settings", {hash:{},inverse:self.noop,fn:self.program(5, program5, data),contexts:[depth0],types:["ID"],hashContexts:hashContexts,hashTypes:hashTypes,data:data});
  if(stack1 || stack1 === 0) { data.buffer.push(stack1); }
  data.buffer.push("\n	  </form>\n	</div>\n	<!-- /account_settings_block -->\n\n  </div>\n</div>\n");
  return buffer;
  
});
Ember.TEMPLATES["_review"] = Ember.Handlebars.template(function anonymous(Handlebars,depth0,helpers,partials,data) {
this.compilerInfo = [3,'>= 1.0.0-rc.4'];
helpers = helpers || Ember.Handlebars.helpers; data = data || {};
  var buffer = '', stack1, stack2, hashTypes, hashContexts, options, escapeExpression=this.escapeExpression, self=this, helperMissing=helpers.helperMissing;

function program1(depth0,data) {
  
  var hashTypes, hashContexts;
  hashTypes = {};
  hashContexts = {};
  data.buffer.push(escapeExpression(helpers._triageMustache.call(depth0, "parent.full_name", {hash:{},contexts:[depth0],types:["ID"],hashContexts:hashContexts,hashTypes:hashTypes,data:data})));
  }

function program3(depth0,data) {
  
  
  data.buffer.push("<div class=\"reco_btn\"><span class=\"icon_ok\">&nbsp;</span>Recommends</div>");
  }

  data.buffer.push("<li>\n  <a href=\"#\"><img src=\"/static/images/demo/img11.jpg\" alt=\"\" /></a>\n  <div class=\"desc\">\n	<p>");
  hashTypes = {};
  hashContexts = {};
  options = {hash:{},inverse:self.noop,fn:self.program(1, program1, data),contexts:[depth0,depth0],types:["ID","ID"],hashContexts:hashContexts,hashTypes:hashTypes,data:data};
  stack2 = ((stack1 = helpers.linkTo),stack1 ? stack1.call(depth0, "parent", "parent", options) : helperMissing.call(depth0, "linkTo", "parent", "parent", options));
  if(stack2 || stack2 === 0) { data.buffer.push(stack2); }
  data.buffer.push("</p>\n	");
  hashTypes = {};
  hashContexts = {};
  stack2 = helpers['if'].call(depth0, "recommended", {hash:{},inverse:self.noop,fn:self.program(3, program3, data),contexts:[depth0],types:["ID"],hashContexts:hashContexts,hashTypes:hashTypes,data:data});
  if(stack2 || stack2 === 0) { data.buffer.push(stack2); }
  data.buffer.push("\n	<p>");
  hashTypes = {};
  hashContexts = {};
  data.buffer.push(escapeExpression(helpers._triageMustache.call(depth0, "review", {hash:{},contexts:[depth0],types:["ID"],hashContexts:hashContexts,hashTypes:hashTypes,data:data})));
  data.buffer.push("</p>\n  </div>\n</li>\n");
  return buffer;
  
});
Ember.TEMPLATES["_booking"] = Ember.Handlebars.template(function anonymous(Handlebars,depth0,helpers,partials,data) {
this.compilerInfo = [3,'>= 1.0.0-rc.4'];
helpers = helpers || Ember.Handlebars.helpers; data = data || {};
  var buffer = '', stack1, hashTypes, hashContexts, options, escapeExpression=this.escapeExpression, self=this, helperMissing=helpers.helperMissing, functionType="function", blockHelperMissing=helpers.blockHelperMissing;

function program1(depth0,data) {
  
  
  data.buffer.push("avatar ");
  }

function program3(depth0,data) {
  
  var buffer = '', stack1, stack2, hashTypes, hashContexts, options;
  data.buffer.push("\n          ");
  hashTypes = {};
  hashContexts = {};
  data.buffer.push(escapeExpression(helpers.each.call(depth0, "booking.parent.friends_in_common", {hash:{},contexts:[depth0],types:["ID"],hashContexts:hashContexts,hashTypes:hashTypes,data:data})));
  data.buffer.push("\n          <li>");
  hashTypes = {};
  hashContexts = {};
  options = {hash:{},inverse:self.noop,fn:self.program(4, program4, data),contexts:[depth0,depth0],types:["ID","ID"],hashContexts:hashContexts,hashTypes:hashTypes,data:data};
  stack2 = ((stack1 = helpers.linkTo),stack1 ? stack1.call(depth0, "parent", "", options) : helperMissing.call(depth0, "linkTo", "parent", "", options));
  if(stack2 || stack2 === 0) { data.buffer.push(stack2); }
  data.buffer.push("</li>\n          ");
  return buffer;
  }
function program4(depth0,data) {
  
  var buffer = '', hashTypes, hashContexts;
  data.buffer.push("<img src=\"/static/images/demo/img3.jpg\" alt=\"\"></a><span> ");
  hashTypes = {};
  hashContexts = {};
  data.buffer.push(escapeExpression(helpers._triageMustache.call(depth0, "full_name", {hash:{},contexts:[depth0],types:["ID"],hashContexts:hashContexts,hashTypes:hashTypes,data:data})));
  data.buffer.push("</span>");
  return buffer;
  }

function program6(depth0,data) {
  
  var buffer = '', hashTypes, hashContexts;
  data.buffer.push("\n    <div class=\"btn_wrap\">\n      <a class=\"button button_smaller button_cancel\" ");
  hashTypes = {};
  hashContexts = {};
  data.buffer.push(escapeExpression(helpers.action.call(depth0, "cancel", {hash:{},contexts:[depth0],types:["STRING"],hashContexts:hashContexts,hashTypes:hashTypes,data:data})));
  data.buffer.push(">\n        <span class=\"icon_cancel\">&nbsp;\n        </span>CANCEL\n      </a>\n    </div>\n    ");
  return buffer;
  }

function program8(depth0,data) {
  
  var buffer = '', hashTypes, hashContexts;
  data.buffer.push("\n    <div class=\"btn_wrap\">\n      <a class=\"button button_smaller\" ");
  hashTypes = {};
  hashContexts = {};
  data.buffer.push(escapeExpression(helpers.action.call(depth0, "accept", {hash:{},contexts:[depth0],types:["STRING"],hashContexts:hashContexts,hashTypes:hashTypes,data:data})));
  data.buffer.push(">\n        <span class=\"icon_ok2\">&nbsp;\n        </span>ACCEPT\n      </a>\n      <a class=\"button button_smaller button_cancel\" ");
  hashTypes = {};
  hashContexts = {};
  data.buffer.push(escapeExpression(helpers.action.call(depth0, "decline", {hash:{},contexts:[depth0],types:["STRING"],hashContexts:hashContexts,hashTypes:hashTypes,data:data})));
  data.buffer.push(">\n        <span class=\"icon_cancel\">&nbsp;\n        </span>DECLINE\n      </a>\n    </div>\n    ");
  return buffer;
  }

function program10(depth0,data) {
  
  
  data.buffer.push("\n        <span class=\"show\">Show</span>\n        ");
  }

function program12(depth0,data) {
  
  
  data.buffer.push("\n        <span class=\"hide\">Hide</span>\n        ");
  }

  data.buffer.push("<li>\n  <header>\n    Request Sent: ");
  hashTypes = {};
  hashContexts = {};
  data.buffer.push(escapeExpression(helpers._triageMustache.call(depth0, "booking.created", {hash:{},contexts:[depth0],types:["ID"],hashContexts:hashContexts,hashTypes:hashTypes,data:data})));
  data.buffer.push("\n    <span>");
  hashTypes = {};
  hashContexts = {};
  data.buffer.push(escapeExpression(helpers._triageMustache.call(depth0, "booking.booking_type", {hash:{},contexts:[depth0],types:["ID"],hashContexts:hashContexts,hashTypes:hashTypes,data:data})));
  data.buffer.push("</span>\n  </header>\n  <div class=\"img\">\n    ");
  options = {hash:{},inverse:self.noop,fn:self.program(1, program1, data),contexts:[],types:[],hashContexts:hashContexts,hashTypes:hashTypes,data:data};
  if (stack1 = helpers.comment) { stack1 = stack1.call(depth0, options); }
  else { stack1 = depth0.comment; stack1 = typeof stack1 === functionType ? stack1.apply(depth0) : stack1; }
  hashTypes = {};
  hashContexts = {};
  if (!helpers.comment) { stack1 = blockHelperMissing.call(depth0, stack1, options); }
  if(stack1 || stack1 === 0) { data.buffer.push(stack1); }
  data.buffer.push("\n    <a href=\"#\"><img src=\"/static/images/demo/img16.jpg\" alt=\"\"></a>\n    <p><span><a href=\"#\">");
  hashTypes = {};
  hashContexts = {};
  data.buffer.push(escapeExpression(helpers._triageMustache.call(depth0, "booking.parent.full_name", {hash:{},contexts:[depth0],types:["ID"],hashContexts:hashContexts,hashTypes:hashTypes,data:data})));
  data.buffer.push("</a></span></p>\n    <div>\n      <a href=\"#\">0 mutual friends</a>\n      <ul>\n        <li>Friends you have in common</li>\n\n        ");
  options = {hash:{},inverse:self.noop,fn:self.program(3, program3, data),contexts:[],types:[],hashContexts:hashContexts,hashTypes:hashTypes,data:data};
  if (stack1 = helpers.comment) { stack1 = stack1.call(depth0, options); }
  else { stack1 = depth0.comment; stack1 = typeof stack1 === functionType ? stack1.apply(depth0) : stack1; }
  hashTypes = {};
  hashContexts = {};
  if (!helpers.comment) { stack1 = blockHelperMissing.call(depth0, stack1, options); }
  if(stack1 || stack1 === 0) { data.buffer.push(stack1); }
  data.buffer.push("\n      </ul>\n    </div>\n  </div>\n  <div class=\"desc clear\">\n    <ul>\n      <li><span class=\"icon_date\">&nbsp;</span>");
  hashTypes = {};
  hashContexts = {};
  data.buffer.push(escapeExpression(helpers._triageMustache.call(depth0, "booking.start_date_time", {hash:{},contexts:[depth0],types:["ID"],hashContexts:hashContexts,hashTypes:hashTypes,data:data})));
  data.buffer.push("&nbsp; <span>");
  hashTypes = {};
  hashContexts = {};
  data.buffer.push(escapeExpression(helpers._triageMustache.call(depth0, "booking.start_date_time", {hash:{},contexts:[depth0],types:["ID"],hashContexts:hashContexts,hashTypes:hashTypes,data:data})));
  data.buffer.push("</span></li>\n      <li><span class=\"icon_friends5\">&nbsp;</span>");
  hashTypes = {};
  hashContexts = {};
  data.buffer.push(escapeExpression(helpers._triageMustache.call(depth0, "booking.child.length", {hash:{},contexts:[depth0],types:["ID"],hashContexts:hashContexts,hashTypes:hashTypes,data:data})));
  data.buffer.push(" Kids</li>\n      <li><span class=\"icon_pin3\">&nbsp;</span>New York, NY</li>\n      <li>\n        <p><a href=\"#\">Need more info?<br>Email ");
  hashTypes = {};
  hashContexts = {};
  data.buffer.push(escapeExpression(helpers._triageMustache.call(depth0, "booking.parent.first_name", {hash:{},contexts:[depth0],types:["ID"],hashContexts:hashContexts,hashTypes:hashTypes,data:data})));
  data.buffer.push("</a></p>\n        <span class=\"icon_email2\">&nbsp;</span><a href=\"mailto:jeyre@gmail.com\">");
  hashTypes = {};
  hashContexts = {};
  data.buffer.push(escapeExpression(helpers._triageMustache.call(depth0, "booking.parent.email", {hash:{},contexts:[depth0],types:["ID"],hashContexts:hashContexts,hashTypes:hashTypes,data:data})));
  data.buffer.push("</a>\n      </li>\n    </ul>\n    <div class=\"price\">\n      <span>\n        <strong>$\n        </strong>");
  hashTypes = {};
  hashContexts = {};
  data.buffer.push(escapeExpression(helpers.view.call(depth0, "Ember.TextField", "valueBinding", "rate", {hash:{},contexts:[depth0,depth0,depth0],types:["ID","ID","ID"],hashContexts:hashContexts,hashTypes:hashTypes,data:data})));
  data.buffer.push("/hr\n      </span>\n      <a class=\"edit_button\" href=\"#\">edit\n      </a>\n    </div>\n    ");
  hashTypes = {};
  hashContexts = {};
  stack1 = helpers['if'].call(depth0, "sitter_accepted", {hash:{},inverse:self.program(8, program8, data),fn:self.program(6, program6, data),contexts:[depth0],types:["ID"],hashContexts:hashContexts,hashTypes:hashTypes,data:data});
  if(stack1 || stack1 === 0) { data.buffer.push(stack1); }
  data.buffer.push("\n    <div class=\"note_wrap\">\n      <a ");
  hashTypes = {};
  hashContexts = {};
  data.buffer.push(escapeExpression(helpers.action.call(depth0, "showNote", {hash:{},contexts:[depth0],types:["STRING"],hashContexts:hashContexts,hashTypes:hashTypes,data:data})));
  data.buffer.push(">\n        ");
  hashTypes = {};
  hashContexts = {};
  stack1 = helpers['if'].call(depth0, "isNoteShown", {hash:{},inverse:self.program(12, program12, data),fn:self.program(10, program10, data),contexts:[depth0],types:["ID"],hashContexts:hashContexts,hashTypes:hashTypes,data:data});
  if(stack1 || stack1 === 0) { data.buffer.push(stack1); }
  data.buffer.push("\n        Note\n      </a>\n    </div>\n  </div>\n  <div class=\"note_desc clear\">\n    <p>");
  hashTypes = {};
  hashContexts = {};
  data.buffer.push(escapeExpression(helpers._triageMustache.call(depth0, "booking.note", {hash:{},contexts:[depth0],types:["ID"],hashContexts:hashContexts,hashTypes:hashTypes,data:data})));
  data.buffer.push("</p>\n  </div>\n  <footer>\n    Request Sent: ");
  hashTypes = {};
  hashContexts = {};
  data.buffer.push(escapeExpression(helpers._triageMustache.call(depth0, "booking.created", {hash:{},contexts:[depth0],types:["ID"],hashContexts:hashContexts,hashTypes:hashTypes,data:data})));
  data.buffer.push("\n  </footer>\n</li>\n");
  return buffer;
  
});
Ember.TEMPLATES["parentEdit/profile"] = Ember.Handlebars.template(function anonymous(Handlebars,depth0,helpers,partials,data) {
this.compilerInfo = [3,'>= 1.0.0-rc.4'];
helpers = helpers || Ember.Handlebars.helpers; data = data || {};
  


  data.buffer.push("	  <!-- profile_block -->\n	  <div class=\"mob_tab_trigger active\">Profile</div>\n	  <div class=\"tab_content profile_block parent_profile_block\" id=\"tab-1\">\n		<form method=\"post\" action=\"#\" class=\"form_style\">\n		  <ul>\n			<li>\n			  <ul>\n				<li><span class=\"icon_friends6\">&nbsp;</span>Children</li>\n				<li>\n				  <p class=\"child_number\">CHILD 1 <a class=\"button button_smaller button_edit\" href=\"#\"><span class=\"icon_plus\">&nbsp;</span>ADD ANOTHER CHILD</a></p>\n				  <p class=\"small_selects\"><span>FIRST NAME</span> <input type=\"text\" value=\"\" /><span>DATE OF BIRTH</span> <select data-placeholder=\"MONTH\" tabindex=\"3\"><option>MONTH</option><option>MONTH</option></select> <select data-placeholder=\"DAY\" tabindex=\"4\"><option>DAY</option><option>DAY</option></select> <select data-placeholder=\"YEAR\" tabindex=\"5\"><option>YEAR</option><option>YEAR</option></select></p>\n				  <p><span>SCHOOL</span> <input type=\"text\" class=\"long\" value=\"\" /></p>\n				  <p><span>Special needs?</span> <select multiple data-placeholder=\"Choose all that apply\" tabindex=\"18\"><option>text</option><option>text</option></select> <input type=\"checkbox\" id=\"none\" /><label for=\"none\">NONE</label></p>\n				  <p><span class=\"two_row\">Not listed?<br />Add another</span> <input type=\"text\" value=\"Add special need\" /></p>\n				  <a class=\"button button_small\" href=\"#\"><span class=\"icon_ok2\">&nbsp;</span>Save</a>\n				</li>\n			  </ul>\n			</li>\n			<li>\n			  <ul>\n				<li><span class=\"icon_pin4\">&nbsp;</span>Home Address</li>\n				<li>\n				  <p><span>&nbsp;</span> <input type=\"text\" value=\"Street address\" /> <input type=\"text\" value=\"Apt/Suite\" class=\"small\" /></p>\n				  <p><span>&nbsp;</span> <input type=\"text\" value=\"07030\" class=\"small\" /> <select data-placeholder=\"Hoboken\" tabindex=\"1\"><option>Hoboken</option><option>Hoboken</option></select> <select class=\"small\" data-placeholder=\"NJ\" tabindex=\"2\"><option>NJ</option><option>NJ</option></select></p>\n				  <a class=\"button button_small\" href=\"#\"><span class=\"icon_ok2\">&nbsp;</span>Save</a>\n				</li>\n			  </ul>\n			</li>\n			<li>\n			  <ul>\n				<li><span class=\"icon_iphone2\">&nbsp;</span>Cell Phone Number</li>\n				<li>\n				  <p><span>&nbsp;</span> <input type=\"text\" value=\"(123)\" class=\"small\" /> <input type=\"text\" value=\"456-7890\" /></p>\n				  <a class=\"button button_small\" href=\"#\"><span class=\"icon_ok2\">&nbsp;</span>Save</a>\n				</li>\n			  </ul>\n			</li>\n			<li>\n			  <ul>\n				<li><span class=\"icon_email3\">&nbsp;</span>Email Address</li>\n				<li>\n				  <p><span>&nbsp;</span> <input type=\"text\" value=\"\" /></p>\n				  <a class=\"button button_small\" href=\"#\"><span class=\"icon_ok2\">&nbsp;</span>Save</a>\n				</li>\n			  </ul>\n			</li>\n			<li>\n			  <ul>\n				<li><span class=\"icon_emergency2\">&nbsp;</span>Emergency Contacts</li>\n				<li>\n				  <p><span>NAME</span> <input type=\"text\" value=\"\" /><span>PHONE</span> <input type=\"text\" value=\"\" /></p>\n				  <p><span class=\"two_row\">PEDIATRICIAN’S NAME</span> <input type=\"text\" value=\"\" /><span class=\"two_row\">PEDIATRICIAN’S PHONE</span> <input type=\"text\" value=\"\" /></p>\n				  <a class=\"button button_small\" href=\"#\"><span class=\"icon_ok2\">&nbsp;</span>Save</a>\n				</li>\n			  </ul>\n			</li>\n			<li>\n			  <ul>\n				<li><span class=\"icon_lng2\">&nbsp;</span>Languages</li>\n				<li>\n				  <p><span>I speak:</span><select multiple data-placeholder=\"English\" tabindex=\"25\"><option>English</option><option>English</option></select></p>\n				  <a class=\"button button_small\" href=\"#\"><span class=\"icon_ok2\">&nbsp;</span>Save</a>\n				</li>\n			  </ul>\n			</li>\n		  </ul>\n		</form>\n	  </div>\n	  <!-- /profile_block -->\n");
  
});
Ember.TEMPLATES["parentEdit/network"] = Ember.Handlebars.template(function anonymous(Handlebars,depth0,helpers,partials,data) {
this.compilerInfo = [3,'>= 1.0.0-rc.4'];
helpers = helpers || Ember.Handlebars.helpers; data = data || {};
  var buffer = '', stack1, hashTypes, hashContexts, escapeExpression=this.escapeExpression, self=this, helperMissing=helpers.helperMissing;

function program1(depth0,data) {
  
  var buffer = '', stack1, stack2, hashTypes, hashContexts, options;
  data.buffer.push("\n		  <li>");
  hashTypes = {};
  hashContexts = {};
  options = {hash:{},inverse:self.noop,fn:self.program(2, program2, data),contexts:[depth0,depth0],types:["ID","ID"],hashContexts:hashContexts,hashTypes:hashTypes,data:data};
  stack2 = ((stack1 = helpers.linkTo),stack1 ? stack1.call(depth0, "parent", "", options) : helperMissing.call(depth0, "linkTo", "parent", "", options));
  if(stack2 || stack2 === 0) { data.buffer.push(stack2); }
  data.buffer.push("</li>\n        ");
  return buffer;
  }
function program2(depth0,data) {
  
  var buffer = '', hashTypes, hashContexts;
  data.buffer.push("<img src=\"/static/images/demo/img15.jpg\" alt=\"\" />");
  hashTypes = {};
  hashContexts = {};
  data.buffer.push(escapeExpression(helpers._triageMustache.call(depth0, "full_name", {hash:{},contexts:[depth0],types:["ID"],hashContexts:hashContexts,hashTypes:hashTypes,data:data})));
  return buffer;
  }

  data.buffer.push("<!-- network_block -->\n<div class=\"mob_tab_trigger\">Network</div>\n<div class=\"tab_content network_block\" id=\"tab-4\">\n  <div class=\"soc_list clear\">\n	<p>Find people you know on Sitterfied</p>\n	<ul>\n	  <li>\n		<p class=\"clear\"><a ");
  hashTypes = {};
  hashContexts = {};
  data.buffer.push(escapeExpression(helpers.action.call(depth0, "facebookConnect", {hash:{},contexts:[depth0],types:["STRING"],hashContexts:hashContexts,hashTypes:hashTypes,data:data})));
  data.buffer.push("><img src=\"/static/images/icons/facebook.png\" alt=\"\" />Facebook</a><a ");
  hashTypes = {};
  hashContexts = {};
  data.buffer.push(escapeExpression(helpers.action.call(depth0, "gmailConnect", {hash:{},contexts:[depth0],types:["STRING"],hashContexts:hashContexts,hashTypes:hashTypes,data:data})));
  data.buffer.push("><img src=\"/static/images/icons/gmail.png\" alt=\"\" />Gmail</a></p>\n		<p>Connect</p>\n	  </li>\n	  <li>\n		<p>");
  hashContexts = {'placeholder': depth0,'valueBinding': depth0};
  hashTypes = {'placeholder': "STRING",'valueBinding': "STRING"};
  data.buffer.push(escapeExpression(helpers.view.call(depth0, "Ember.TextField", {hash:{
    'placeholder': ("Search a person or group"),
    'valueBinding': ("newFriendName")
  },contexts:[depth0],types:["ID"],hashContexts:hashContexts,hashTypes:hashTypes,data:data})));
  data.buffer.push("<input ");
  hashTypes = {};
  hashContexts = {};
  data.buffer.push(escapeExpression(helpers.action.call(depth0, "addFriend", {hash:{},contexts:[depth0],types:["STRING"],hashContexts:hashContexts,hashTypes:hashTypes,data:data})));
  data.buffer.push("type=\"submit\" value=\"ADD\" /></p>\n		<p>Search</p>\n	  </li>\n	  <li>\n		<p><a ");
  hashTypes = {};
  hashContexts = {};
  data.buffer.push(escapeExpression(helpers.action.call(depth0, "invite", {hash:{},contexts:[depth0],types:["STRING"],hashContexts:hashContexts,hashTypes:hashTypes,data:data})));
  data.buffer.push(">Invite Your Friends</a></p>\n		<p>Invite</p>\n	  </li>\n	</ul>\n  </div>\n  <ul class=\"soc_psg_list clear\">\n	<li>\n	  <ul>\n		<li>Parents</li>\n        ");
  hashTypes = {};
  hashContexts = {};
  stack1 = helpers.each.call(depth0, "parents_in_network", {hash:{},inverse:self.noop,fn:self.program(1, program1, data),contexts:[depth0],types:["ID"],hashContexts:hashContexts,hashTypes:hashTypes,data:data});
  if(stack1 || stack1 === 0) { data.buffer.push(stack1); }
  data.buffer.push("\n	  </ul>\n	</li>\n	<li>\n	  <ul>\n		<li>Sitters</li>\n		<li><a href=\"#\"><img src=\"/static/images/demo/img15.jpg\" alt=\"\" /></a><a href=\"#\">Lakeisha Powanda</a></li>\n		<li><a href=\"#\"><img src=\"/static/images/demo/img15.jpg\" alt=\"\" /></a><a href=\"#\">Connie Takach</a></li>\n		<li><a href=\"#\"><img src=\"/static/images/demo/img15.jpg\" alt=\"\" /></a><a href=\"#\">Jane Eyre</a></li>\n	  </ul>\n	</li>\n	<li>\n	  <ul>\n		<li>Groups</li>\n		<li><a href=\"#\">Hoboken Catholic Church</a> <a href=\"#\" class=\"delete\">&nbsp;</a></li>\n		<li><a href=\"#\">St Francis Prep School</a> <a href=\"#\" class=\"delete\">&nbsp;</a></li>\n		<li><a href=\"#\">Hoboken Mommies</a> <a href=\"#\" class=\"delete\">&nbsp;</a></li>\n	  </ul>\n	</li>\n  </ul>\n</div>\n<!-- /network_block -->\n");
  return buffer;
  
});
Ember.TEMPLATES["parentEdit/index"] = Ember.Handlebars.template(function anonymous(Handlebars,depth0,helpers,partials,data) {
this.compilerInfo = [3,'>= 1.0.0-rc.4'];
helpers = helpers || Ember.Handlebars.helpers; data = data || {};
  


  data.buffer.push("edit index");
  
});
Ember.TEMPLATES["parentEdit/top"] = Ember.Handlebars.template(function anonymous(Handlebars,depth0,helpers,partials,data) {
this.compilerInfo = [3,'>= 1.0.0-rc.4'];
helpers = helpers || Ember.Handlebars.helpers; data = data || {};
  var buffer = '', stack1, stack2, hashContexts, hashTypes, options, self=this, helperMissing=helpers.helperMissing, escapeExpression=this.escapeExpression;

function program1(depth0,data) {
  
  
  data.buffer.push("Back to search results");
  }

  hashContexts = {'class': depth0};
  hashTypes = {'class': "STRING"};
  options = {hash:{
    'class': ("back")
  },inverse:self.noop,fn:self.program(1, program1, data),contexts:[depth0],types:["ID"],hashContexts:hashContexts,hashTypes:hashTypes,data:data};
  stack2 = ((stack1 = helpers.linkTo),stack1 ? stack1.call(depth0, "search", options) : helperMissing.call(depth0, "linkTo", "search", options));
  if(stack2 || stack2 === 0) { data.buffer.push(stack2); }
  data.buffer.push("\n<!-- top info -->\n<div class=\"top_info clear\">\n  <div class=\"member_since guest\"></div>\n  <div class=\"photo\">\n	<div class=\"photo_edit_wrap\">\n	  <img src=\"/static/images/demo/img2.jpg\" alt=\"\" />\n	  <p><span class=\"icon_pen\">&nbsp;</span><a href=\"#edit_photo_popup\">Edit Photo</a></p>\n	</div>\n  </div>\n  <div class=\"guest_top_info\">\n	<p>");
  hashTypes = {};
  hashContexts = {};
  data.buffer.push(escapeExpression(helpers._triageMustache.call(depth0, "full_name", {hash:{},contexts:[depth0],types:["ID"],hashContexts:hashContexts,hashTypes:hashTypes,data:data})));
  data.buffer.push("</p>\n	<p>Hi ");
  hashTypes = {};
  hashContexts = {};
  data.buffer.push(escapeExpression(helpers._triageMustache.call(depth0, "first_name", {hash:{},contexts:[depth0],types:["ID"],hashContexts:hashContexts,hashTypes:hashTypes,data:data})));
  data.buffer.push(", you have <strong>");
  hashTypes = {};
  hashContexts = {};
  data.buffer.push(escapeExpression(helpers._triageMustache.call(depth0, "parents_in_network.length", {hash:{},contexts:[depth0],types:["ID"],hashContexts:hashContexts,hashTypes:hashTypes,data:data})));
  data.buffer.push("</strong> friends and and belong to <strong>");
  hashTypes = {};
  hashContexts = {};
  data.buffer.push(escapeExpression(helpers._triageMustache.call(depth0, "sitter_groups.length", {hash:{},contexts:[depth0],types:["ID"],hashContexts:hashContexts,hashTypes:hashTypes,data:data})));
  data.buffer.push("</strong> groups on Sitterfied</p>\n	<ul class=\"clear\">\n	  <li><p><a href=\"#\" class=\"facebook\">&nbsp;</a><a href=\"#\" class=\"gmail\">&nbsp;</a></p><a href=\"#\">Connect</a></li>\n	  <li><p><a href=\"#\" class=\"search\">&nbsp;</a></p><a href=\"#\">Search for Friends</a></li>\n	  <li><p><a href=\"#\" class=\"letter\">&nbsp;</a></p><a href=\"#\">Invite Friends</a></li>\n	</ul>\n	<p class=\"hide\"><a href=\"#\">Hide</a></p>\n	<p class=\"show\"><a href=\"#\">Show</a></p>\n  </div>\n</div>\n<!-- /top info -->\n<!-- quick_info_list -->\n<div class=\"quick_info_list clear\" id=\"fixed_tabs\">\n  <ul>\n	<li><strong>&nbsp;</strong>Facebook connected</li>\n	<li><strong>");
  hashTypes = {};
  hashContexts = {};
  data.buffer.push(escapeExpression(helpers._triageMustache.call(depth0, "sitters_in_network.length", {hash:{},contexts:[depth0],types:["ID"],hashContexts:hashContexts,hashTypes:hashTypes,data:data})));
  data.buffer.push("</strong> sitters on your team</li>\n	<li><strong>");
  hashTypes = {};
  hashContexts = {};
  data.buffer.push(escapeExpression(helpers._triageMustache.call(depth0, "bookings.length", {hash:{},contexts:[depth0],types:["ID"],hashContexts:hashContexts,hashTypes:hashTypes,data:data})));
  data.buffer.push("</strong> bookings</li>\n	<li><strong>");
  hashTypes = {};
  hashContexts = {};
  data.buffer.push(escapeExpression(helpers._triageMustache.call(depth0, "weeks_since_last_booking", {hash:{},contexts:[depth0],types:["ID"],hashContexts:hashContexts,hashTypes:hashTypes,data:data})));
  data.buffer.push("</strong> weeks &amp; <strong>");
  hashTypes = {};
  hashContexts = {};
  data.buffer.push(escapeExpression(helpers._triageMustache.call(depth0, "days_since_last_booking", {hash:{},contexts:[depth0],types:["ID"],hashContexts:hashContexts,hashTypes:hashTypes,data:data})));
  data.buffer.push("</strong> days since your last booking</li>\n  </ul>\n</div>");
  return buffer;
  
});
Ember.TEMPLATES["parentEdit"] = Ember.Handlebars.template(function anonymous(Handlebars,depth0,helpers,partials,data) {
this.compilerInfo = [3,'>= 1.0.0-rc.4'];
helpers = helpers || Ember.Handlebars.helpers; data = data || {};
  var buffer = '', stack1, stack2, hashTypes, hashContexts, options, self=this, helperMissing=helpers.helperMissing, escapeExpression=this.escapeExpression;

function program1(depth0,data) {
  
  
  data.buffer.push("Profile");
  }

function program3(depth0,data) {
  
  
  data.buffer.push("Bookings");
  }

function program5(depth0,data) {
  
  
  data.buffer.push("Sitter Team");
  }

function program7(depth0,data) {
  
  
  data.buffer.push("Network");
  }

function program9(depth0,data) {
  
  
  data.buffer.push("Reviews");
  }

  data.buffer.push("<div class=\"container clear\">\n  <div class=\"wraper\">\n\n	<div class=\"tabs_wrap\">\n	  <ul class=\"tab_select\">\n		<li>");
  hashTypes = {};
  hashContexts = {};
  options = {hash:{},inverse:self.noop,fn:self.program(1, program1, data),contexts:[depth0],types:["ID"],hashContexts:hashContexts,hashTypes:hashTypes,data:data};
  stack2 = ((stack1 = helpers.linkTo),stack1 ? stack1.call(depth0, "parentEdit.profile", options) : helperMissing.call(depth0, "linkTo", "parentEdit.profile", options));
  if(stack2 || stack2 === 0) { data.buffer.push(stack2); }
  data.buffer.push("</li>\n		<li>");
  hashTypes = {};
  hashContexts = {};
  options = {hash:{},inverse:self.noop,fn:self.program(3, program3, data),contexts:[depth0],types:["ID"],hashContexts:hashContexts,hashTypes:hashTypes,data:data};
  stack2 = ((stack1 = helpers.linkTo),stack1 ? stack1.call(depth0, "parentEdit.bookings", options) : helperMissing.call(depth0, "linkTo", "parentEdit.bookings", options));
  if(stack2 || stack2 === 0) { data.buffer.push(stack2); }
  data.buffer.push("</li>\n		<li>");
  hashTypes = {};
  hashContexts = {};
  options = {hash:{},inverse:self.noop,fn:self.program(5, program5, data),contexts:[depth0],types:["ID"],hashContexts:hashContexts,hashTypes:hashTypes,data:data};
  stack2 = ((stack1 = helpers.linkTo),stack1 ? stack1.call(depth0, "parentEdit.sitterTeam", options) : helperMissing.call(depth0, "linkTo", "parentEdit.sitterTeam", options));
  if(stack2 || stack2 === 0) { data.buffer.push(stack2); }
  data.buffer.push("</li>\n		<li>");
  hashTypes = {};
  hashContexts = {};
  options = {hash:{},inverse:self.noop,fn:self.program(7, program7, data),contexts:[depth0],types:["ID"],hashContexts:hashContexts,hashTypes:hashTypes,data:data};
  stack2 = ((stack1 = helpers.linkTo),stack1 ? stack1.call(depth0, "parentEdit.network", options) : helperMissing.call(depth0, "linkTo", "parentEdit.network", options));
  if(stack2 || stack2 === 0) { data.buffer.push(stack2); }
  data.buffer.push("</li>\n		<li>");
  hashTypes = {};
  hashContexts = {};
  options = {hash:{},inverse:self.noop,fn:self.program(9, program9, data),contexts:[depth0],types:["ID"],hashContexts:hashContexts,hashTypes:hashTypes,data:data};
  stack2 = ((stack1 = helpers.linkTo),stack1 ? stack1.call(depth0, "parentEdit.reviews", options) : helperMissing.call(depth0, "linkTo", "parentEdit.reviews", options));
  if(stack2 || stack2 === 0) { data.buffer.push(stack2); }
  data.buffer.push("</li>\n	  </ul>\n\n      ");
  hashTypes = {};
  hashContexts = {};
  data.buffer.push(escapeExpression(helpers._triageMustache.call(depth0, "outlet", {hash:{},contexts:[depth0],types:["ID"],hashContexts:hashContexts,hashTypes:hashTypes,data:data})));
  data.buffer.push("\n\n	</div>\n  </div>\n</div>");
  return buffer;
  
});
Ember.TEMPLATES["parentEdit/bookings"] = Ember.Handlebars.template(function anonymous(Handlebars,depth0,helpers,partials,data) {
this.compilerInfo = [3,'>= 1.0.0-rc.4'];
helpers = helpers || Ember.Handlebars.helpers; data = data || {};
  


  data.buffer.push("	  <!-- bookings_block -->\n	  <div class=\"mob_tab_trigger\">Bookings</div>\n	  <div class=\"tab_content bookings_block parent_bookings_block\" id=\"tab-2\">\n		<ul class=\"subtab_select\">\n		  <li><a href=\"#tab-1-1\"><span>4</span>Pending Requests</a></li>\n		  <li><a href=\"#tab-1-2\"><span>3</span>Upcoming Jobs</a></li>\n		  <li><a href=\"#tab-1-3\"><span>7</span>Completed Jobs</a></li>\n		  <li><a href=\"#tab-1-5\"><span>2</span>Expired Requests</a></li>\n		  <li><a href=\"#tab-1-6\"><span>3</span>Declined Requests</a></li>\n		  <li><a href=\"#tab-1-7\"><span>2</span>Canceled Jobs</a></li>\n		</ul>\n\n		<div class=\"mob_tab_trigger active\"><span>4</span>Pending Requests</div>\n		<!-- pending_requests_block -->\n		<div class=\"subtab_content pending_requests_block\" id=\"tab-1-1\">\n		  <ul class=\"booking_list\">\n			<li>\n			  <header>\n				Request Sent: Friday 21 July 2012 at 4:40pm\n				<span>Job</span>\n			  </header>\n			  <div class=\"img\">\n				<a href=\"#\"><img src=\"/static/images/demo/img16.jpg\" alt=\"\" /></a>\n				<p><span><a href=\"#\">Jane E</a></span></p>\n				<div>\n				  <a href=\"#\">8 mutual friends</a>\n				  <ul>\n					<li>Friends you have in common</li>\n					<li><a href=\"#\"><img src=\"/static/images/demo/img3.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n					<li><a href=\"#\"><img src=\"/static/images/demo/img4.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n					<li><a href=\"#\"><img src=\"/static/images/demo/img5.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n					<li><a href=\"#\"><img src=\"/static/images/demo/img6.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n					<li><a href=\"#\"><img src=\"/static/images/demo/img7.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n					<li><a href=\"#\"><img src=\"/static/images/demo/img8.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n					<li><a href=\"#\"><img src=\"/static/images/demo/img9.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n					<li><a href=\"#\"><img src=\"/static/images/demo/img10.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n				  </ul>\n				</div>\n			  </div>\n			  <div class=\"desc clear\">\n				<ul>\n				  <li><span class=\"icon_date\">&nbsp;</span>Wednesday, August 1 &nbsp; <span>4:00 pm — 6:00 pm</span></li>\n				  <li><span class=\"icon_friends5\">&nbsp;</span>2 Kids</li>\n				  <li><span class=\"icon_pin3\">&nbsp;</span>New York, NY</li>\n				  <li>\n					<p><a href=\"#\">Need more info?<br />Email Jane.</a></p>\n					<span class=\"icon_email2\">&nbsp;</span><a href=\"mailto:jeyre@gmail.com\">jeyre@gmail.com</a>\n				  </li>\n				</ul>\n				<div class=\"price_lng\"><span><strong>$12 -15</strong> /hr</span></div>\n				<div class=\"btn_wrap\"><a class=\"button button_smaller button_cancel\" href=\"#\"><span class=\"icon_cancel\">&nbsp;</span>CANCEL</a></div>\n				<div class=\"note_wrap\"><a href=\"#\"><span class=\"show\">Show</span><span class=\"hide\">Hide</span> Note</a></div>\n			  </div>\n			  <div class=\"note_desc clear\">\n				<p>Nunc eu ullamcorper orci. Quisque eget odio ac lectus vestibulum faucibus eget in metus. In pellentesque faucibus vestibulum. Quisque eget odio ac lectus vestibulum faucibus eget in metus. </p>\n			  </div>\n			  <footer>\n				Request Sent: Friday 21 July 2012 at 4:40pm\n			  </footer>\n			</li>\n			<li>\n			  <header>\n				Request Sent: Friday 21 July 2012 at 4:40pm\n				<span>Job</span>\n			  </header>\n			  <div class=\"img\">\n				<a href=\"#\"><img src=\"/static/images/demo/img16.jpg\" alt=\"\" /></a>\n				<p><span><a href=\"#\">Jane E</a></span></p>\n				<div>\n				  <a href=\"#\">8 mutual friends</a>\n				  <ul>\n					<li>Friends you have in common</li>\n					<li><a href=\"#\"><img src=\"/static/images/demo/img3.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n					<li><a href=\"#\"><img src=\"/static/images/demo/img4.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n					<li><a href=\"#\"><img src=\"/static/images/demo/img5.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n					<li><a href=\"#\"><img src=\"/static/images/demo/img6.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n					<li><a href=\"#\"><img src=\"/static/images/demo/img7.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n					<li><a href=\"#\"><img src=\"/static/images/demo/img8.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n					<li><a href=\"#\"><img src=\"/static/images/demo/img9.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n					<li><a href=\"#\"><img src=\"/static/images/demo/img10.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n				  </ul>\n				</div>\n			  </div>\n			  <div class=\"desc clear\">\n				<ul>\n				  <li><span class=\"icon_date\">&nbsp;</span>Wednesday, August 1 &nbsp; <span>4:00 pm — 6:00 pm</span></li>\n				  <li><span class=\"icon_friends5\">&nbsp;</span>2 Kids</li>\n				  <li><span class=\"icon_pin3\">&nbsp;</span>New York, NY</li>\n				  <li>\n					<p><a href=\"#\">Need more info?<br />Email Jane.</a></p>\n					<span class=\"icon_email2\">&nbsp;</span><a href=\"mailto:jeyre@gmail.com\">jeyre@gmail.com</a>\n				  </li>\n				</ul>\n				<div class=\"price_lng\"><span><strong>$12 -15</strong> /hr</span></div>\n				<div class=\"btn_wrap\"><a class=\"button button_smaller button_cancel\" href=\"#\"><span class=\"icon_cancel\">&nbsp;</span>CANCEL</a></div>\n				<div class=\"note_wrap\"><a href=\"#\"><span class=\"show\">Show</span><span class=\"hide\">Hide</span> Note</a></div>\n			  </div>\n			  <div class=\"note_desc clear\">\n				<p>Nunc eu ullamcorper orci. Quisque eget odio ac lectus vestibulum faucibus eget in metus. In pellentesque faucibus vestibulum. Quisque eget odio ac lectus vestibulum faucibus eget in metus. </p>\n			  </div>\n			  <footer>\n				Request Sent: Friday 21 July 2012 at 4:40pm\n			  </footer>\n			</li>\n			<li>\n			  <header>\n				Request Sent: Friday 21 July 2012 at 4:40pm\n				<span>Interview</span>\n			  </header>\n			  <div class=\"img\">\n				<a href=\"#\"><img src=\"/static/images/demo/img16.jpg\" alt=\"\" /></a>\n				<p><span><a href=\"#\">Jane E</a></span></p>\n				<div>\n				  <a href=\"#\">8 mutual friends</a>\n				  <ul>\n					<li>Friends you have in common</li>\n					<li><a href=\"#\"><img src=\"/static/images/demo/img3.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n					<li><a href=\"#\"><img src=\"/static/images/demo/img4.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n					<li><a href=\"#\"><img src=\"/static/images/demo/img5.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n					<li><a href=\"#\"><img src=\"/static/images/demo/img6.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n					<li><a href=\"#\"><img src=\"/static/images/demo/img7.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n					<li><a href=\"#\"><img src=\"/static/images/demo/img8.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n					<li><a href=\"#\"><img src=\"/static/images/demo/img9.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n					<li><a href=\"#\"><img src=\"/static/images/demo/img10.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n				  </ul>\n				</div>\n			  </div>\n			  <div class=\"desc clear\">\n				<ul>\n				  <li><span class=\"icon_date\">&nbsp;</span>Wednesday, August 1 &nbsp; <span>4:00 pm — 6:00 pm</span></li>\n				  <li><span class=\"icon_friends5\">&nbsp;</span>2 Kids</li>\n				  <li><span class=\"icon_pin3\">&nbsp;</span>New York, NY</li>\n				  <li>\n					<p><a href=\"#\">Need more info?<br />Email Jane.</a></p>\n					<span class=\"icon_email2\">&nbsp;</span><a href=\"mailto:jeyre@gmail.com\">jeyre@gmail.com</a>\n				  </li>\n				</ul>\n				<div class=\"additional_info\">Meet Up</div>\n				<div class=\"btn_wrap\"><a class=\"button button_smaller button_cancel\" href=\"#\"><span class=\"icon_cancel\">&nbsp;</span>CANCEL</a></div>\n				<div class=\"note_wrap\"><a href=\"#\"><span class=\"show\">Show</span><span class=\"hide\">Hide</span> Note</a></div>\n			  </div>\n			  <div class=\"note_desc clear\">\n				<p>Nunc eu ullamcorper orci. Quisque eget odio ac lectus vestibulum faucibus eget in metus. In pellentesque faucibus vestibulum. Quisque eget odio ac lectus vestibulum faucibus eget in metus. </p>\n			  </div>\n			  <footer>\n				Request Sent: Friday 21 July 2012 at 4:40pm\n			  </footer>\n			</li>\n			<li>\n			  <header>\n				Request Sent: Friday 21 July 2012 at 4:40pm\n				<span>Interview</span>\n			  </header>\n			  <div class=\"img\">\n				<a href=\"#\"><img src=\"/static/images/demo/img16.jpg\" alt=\"\" /></a>\n				<p><span><a href=\"#\">Jane E</a></span></p>\n				<div>\n				  <a href=\"#\">8 mutual friends</a>\n				  <ul>\n					<li>Friends you have in common</li>\n					<li><a href=\"#\"><img src=\"/static/images/demo/img3.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n					<li><a href=\"#\"><img src=\"/static/images/demo/img4.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n					<li><a href=\"#\"><img src=\"/static/images/demo/img5.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n					<li><a href=\"#\"><img src=\"/static/images/demo/img6.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n					<li><a href=\"#\"><img src=\"/static/images/demo/img7.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n					<li><a href=\"#\"><img src=\"/static/images/demo/img8.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n					<li><a href=\"#\"><img src=\"/static/images/demo/img9.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n					<li><a href=\"#\"><img src=\"/static/images/demo/img10.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n				  </ul>\n				</div>\n			  </div>\n			  <div class=\"desc clear\">\n				<ul>\n				  <li><span class=\"icon_date\">&nbsp;</span>Wednesday, August 1 &nbsp; <span>4:00 pm — 6:00 pm</span></li>\n				  <li><span class=\"icon_friends5\">&nbsp;</span>2 Kids</li>\n				  <li><span class=\"icon_pin3\">&nbsp;</span>New York, NY</li>\n				  <li>\n					<p><a href=\"#\">Need more info?<br />Email Jane.</a></p>\n					<span class=\"icon_email2\">&nbsp;</span><a href=\"mailto:jeyre@gmail.com\">jeyre@gmail.com</a>\n				  </li>\n				</ul>\n				<div class=\"additional_info\">By Phone</div>\n				<div class=\"btn_wrap\"><a class=\"button button_smaller button_cancel\" href=\"#\"><span class=\"icon_cancel\">&nbsp;</span>CANCEL</a></div>\n				<div class=\"note_wrap\"><a href=\"#\"><span class=\"show\">Show</span><span class=\"hide\">Hide</span> Note</a></div>\n			  </div>\n			  <div class=\"note_desc clear\">\n				<p>Nunc eu ullamcorper orci. Quisque eget odio ac lectus vestibulum faucibus eget in metus. In pellentesque faucibus vestibulum. Quisque eget odio ac lectus vestibulum faucibus eget in metus. </p>\n			  </div>\n			  <footer>\n				Request Sent: Friday 21 July 2012 at 4:40pm\n			  </footer>\n			</li>\n		  </ul>\n		</div>\n		<!-- /pending_requests_block -->\n\n		<div class=\"mob_tab_trigger\"><span>3</span>Upcoming Jobs</div>\n		<!-- upcoming_jobs_block -->\n		<div class=\"subtab_content upcoming_jobs_block\" id=\"tab-1-2\">\n		  <ul class=\"booking_list\">\n			<li>\n			  <header>\n				Request Sent: Friday 21 July 2012 at 4:40pm\n				<span>Job</span>\n			  </header>\n			  <div class=\"img\">\n				<a href=\"#\"><img src=\"/static/images/demo/img16.jpg\" alt=\"\" /></a>\n				<p><span><a href=\"#\">Jane Eyre</a></span></p>\n				<div>\n				  <a href=\"#\">8 mutual friends</a>\n				  <ul>\n					<li>Friends you have in common</li>\n					<li><a href=\"#\"><img src=\"/static/images/demo/img3.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n					<li><a href=\"#\"><img src=\"/static/images/demo/img4.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n					<li><a href=\"#\"><img src=\"/static/images/demo/img5.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n					<li><a href=\"#\"><img src=\"/static/images/demo/img6.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n					<li><a href=\"#\"><img src=\"/static/images/demo/img7.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n					<li><a href=\"#\"><img src=\"/static/images/demo/img8.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n					<li><a href=\"#\"><img src=\"/static/images/demo/img9.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n					<li><a href=\"#\"><img src=\"/static/images/demo/img10.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n				  </ul>\n				</div>\n			  </div>\n			  <div class=\"desc clear\">\n				<ul>\n				  <li><span class=\"icon_date\">&nbsp;</span>Wednesday, August 1 &nbsp; <span>4:00 pm — 6:00 pm</span> <a href=\"#\" class=\"rlink\">Save to my calendar</a></li>\n				  <li><span class=\"icon_phone\">&nbsp;</span>(125) 898-6891</li>\n				  <li><span class=\"icon_email2\">&nbsp;</span><a href=\"mailto:jeyre@gmail.com\">jeyre@gmail.com</a> <a href=\"#\" class=\"rlink\">Add to my contacts</a></li>\n				  <li><span class=\"icon_pin3\">&nbsp;</span>33 Nassau Ave Suite #2 New York, NY <a href=\"#\" class=\"rlink\">Map this</a></li>\n				</ul>\n				<div class=\"children\"><span class=\"icon_friends5\">&nbsp;</span>2 Kids</div>\n				<div class=\"price\"><span><strong>$25</strong> /hr</span></div>\n				<div class=\"btn_wrap\"><a class=\"button button_smaller button_cancel\" href=\"#\"><span class=\"icon_cancel\">&nbsp;</span>CANCEL</a></div>\n				<div class=\"note_wrap\"><a href=\"#\"><span class=\"show\">Show</span><span class=\"hide\">Hide</span> Notes</a></div>\n			  </div>\n			  <div class=\"note_desc clear\">\n				<p>Nunc eu ullamcorper orci. Quisque eget odio ac lectus vestibulum faucibus eget in metus. In pellentesque faucibus vestibulum. Quisque eget odio ac lectus vestibulum faucibus eget in metus. </p>\n			  </div>\n			  <footer>\n				Request Sent: Friday 21 July 2012 at 4:40pm\n			  </footer>\n			</li>\n			<li>\n			  <header>\n				Request Sent: Friday 21 July 2012 at 4:40pm\n				<span>Interview</span>\n			  </header>\n			  <div class=\"img\">\n				<a href=\"#\"><img src=\"/static/images/demo/img16.jpg\" alt=\"\" /></a>\n				<p><span><a href=\"#\">Jane Eyre</a></span></p>\n				<div>\n				  <a href=\"#\">8 mutual friends</a>\n				  <ul>\n					<li>Friends you have in common</li>\n					<li><a href=\"#\"><img src=\"/static/images/demo/img3.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n					<li><a href=\"#\"><img src=\"/static/images/demo/img4.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n					<li><a href=\"#\"><img src=\"/static/images/demo/img5.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n					<li><a href=\"#\"><img src=\"/static/images/demo/img6.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n					<li><a href=\"#\"><img src=\"/static/images/demo/img7.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n					<li><a href=\"#\"><img src=\"/static/images/demo/img8.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n					<li><a href=\"#\"><img src=\"/static/images/demo/img9.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n					<li><a href=\"#\"><img src=\"/static/images/demo/img10.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n				  </ul>\n				</div>\n			  </div>\n			  <div class=\"desc clear\">\n				<ul>\n				  <li><span class=\"icon_date\">&nbsp;</span>Wednesday, August 1 &nbsp; <span>4:00 pm — 6:00 pm</span> <a href=\"#\" class=\"rlink\">Save to my calendar</a></li>\n				  <li><span class=\"icon_phone\">&nbsp;</span>(125) 898-6891</li>\n				  <li><span class=\"icon_email2\">&nbsp;</span><a href=\"mailto:jeyre@gmail.com\">jeyre@gmail.com</a> <a href=\"#\" class=\"rlink\">Add to my contacts</a></li>\n				  <li><span class=\"icon_pin3\">&nbsp;</span>33 Nassau Ave Suite #2 New York, NY <a href=\"#\" class=\"rlink\">Map this</a></li>\n				</ul>\n				<div class=\"children\"><span class=\"icon_friends5\">&nbsp;</span>2 Kids</div>\n				<div class=\"additional_info\">Meet Up</div>\n				<div class=\"btn_wrap\"><a class=\"button button_smaller button_cancel\" href=\"#\"><span class=\"icon_cancel\">&nbsp;</span>CANCEL</a></div>\n				<div class=\"note_wrap\"><a href=\"#\"><span class=\"show\">Show</span><span class=\"hide\">Hide</span> Notes</a></div>\n			  </div>\n			  <div class=\"note_desc clear\">\n				<p>Nunc eu ullamcorper orci. Quisque eget odio ac lectus vestibulum faucibus eget in metus. In pellentesque faucibus vestibulum. Quisque eget odio ac lectus vestibulum faucibus eget in metus. </p>\n			  </div>\n			  <footer>\n				Request Sent: Friday 21 July 2012 at 4:40pm\n			  </footer>\n			</li>\n		  </ul>\n		</div>\n		<!-- /upcoming_jobs_block -->\n\n		<div class=\"mob_tab_trigger\"><span>7</span>Completed Jobs</div>\n		<!-- completed_jobs_block -->\n		<div class=\"subtab_content completed_jobs_block\" id=\"tab-1-3\">\n		  Completed Jobs\n		</div>\n		<!-- /completed_jobs_block -->\n\n		<div class=\"mob_tab_trigger\"><span>2</span>Expired Requests</div>\n		<!-- expired_requests_block -->\n		<div class=\"subtab_content expired_requests_block\" id=\"tab-1-5\">\n		  Expired Requests\n		</div>\n		<!-- /expired_requests_block -->\n\n		<div class=\"mob_tab_trigger\"><span>3</span>Declined Requests</div>\n		<!-- declined_jobs_block -->\n		<div class=\"subtab_content declined_jobs_block\" id=\"tab-1-6\">\n		  Declined Requests\n		</div>\n		<!-- /declined_jobs_block -->\n\n		<div class=\"mob_tab_trigger\"><span>2</span>Canceled Jobs</div>\n		<!-- canceled_jobs_block -->\n		<div class=\"subtab_content canceled_jobs_block\" id=\"tab-1-7\">\n		  Canceled Jobs\n		</div>\n		<!-- /canceled_jobs_block -->\n	  </div>\n	  <!-- /bookings_block -->\n");
  
});
Ember.TEMPLATES["parentEdit/reviews"] = Ember.Handlebars.template(function anonymous(Handlebars,depth0,helpers,partials,data) {
this.compilerInfo = [3,'>= 1.0.0-rc.4'];
helpers = helpers || Ember.Handlebars.helpers; data = data || {};
  


  data.buffer.push("	  <!-- reviews_block -->\n	  <div class=\"mob_tab_trigger\">Reviews</div>\n	  <div class=\"tab_content reviews_block\" id=\"tab-5\">\n		<ul class=\"clear\">\n		  <li>\n			<a href=\"#\"><img src=\"/static/images/demo/img11.jpg\" alt=\"\" /></a>\n			<div class=\"desc\">\n			  <p><a href=\"#\">Marcie Silk</a></p>\n			  <div class=\"reco_btn\"><span class=\"icon_ok\">&nbsp;</span>Recommends</div>\n			  <p>Sed auctor neque eu tellus rhoncus ut eleifend nibh porttitor. Ut in nulla enim. Phasellus molestie magna non est bibendum non venenatis nisl tempor. Suspendisse dictum feugiat nisl ut dapibus. Mauris iaculis porttitor posuere. Praesent id metus massa, ut blandit odio. Proin quis tortor orci. Etiam at risus et justo dignissim congue. Donec congue lacinia dui, a porttitor lectus condimentum laoreet. Nunc eu ullamcorper orci. Quisque eget odio ac lectus vestibulum faucibus eget in metus. In pellentesque faucibus vestibulum. </p>\n			  <p>Nulla at nulla justo, eget luctus tortor. Nulla facilisi. Duis aliquet egestas purus in blandit. Curabitur vulputate, ligula lacinia scelerisque tempor, lacus lacus ornare ante, ac egestas est urna sit amet.</p>\n			</div>\n		  </li>\n		  <li>\n			<a href=\"#\"><img src=\"/static/images/demo/img12.jpg\" alt=\"\" /></a>\n			<div class=\"desc\">\n			  <p><a href=\"#\">Otis Devin</a></p>\n			  <p>Sed auctor neque eu tellus rhoncus ut eleifend nibh porttitor. Ut in nulla enim. Phasellus molestie magna non est bibendum non venenatis nisl tempor. Suspendisse dictum feugiat nisl ut dapibus. Mauris iaculis porttitor posuere. Praesent id metus massa, ut blandit odio. Proin quis tortor orci. Etiam at risus et justo dignissim congue. Donec congue lacinia dui, a porttitor lectus condimentum laoreet. </p>\n			</div>\n		  </li>\n		</ul>\n	  </div>\n	  <!-- /reviews_block -->\n");
  
});
Ember.TEMPLATES["parentEdit/sitterTeam"] = Ember.Handlebars.template(function anonymous(Handlebars,depth0,helpers,partials,data) {
this.compilerInfo = [3,'>= 1.0.0-rc.4'];
helpers = helpers || Ember.Handlebars.helpers; data = data || {};
  


  data.buffer.push("	  <!-- sitter_team -->\n	  <div class=\"mob_tab_trigger\">Sitter Team</div>\n	  <div class=\"tab_content my_sitter_team my_sitter_team_tab_bg\" id=\"tab-3\">\n		<div class=\"send_request\"><a href=\"#\">Send a job request to the team</a></div>\n		<ul class=\"clear\">\n		  <li>\n			<div class=\"tit\">\n			  <span><strong>$15</strong> /hr</span>\n			  <a href=\"#\">Samantha Chadwick</a>\n			</div>\n			<div class=\"img\">\n			  <a href=\"#\"><img src=\"/static/images/demo/img13.jpg\" alt=\"\" /></a>\n			</div>\n			<ul>\n			  <li><span class=\"icon_plus_box\">&nbsp;</span>Last hired: <span>April 23, 2013</span></li>\n			  <li><span class=\"icon_reload\">&nbsp;</span>4 jobs <span class=\"friends_span\"><span class=\"icon_friends4\">&nbsp;</span><a href=\"#\">24 sitter friends</a></span></li>\n			</ul>\n			<div class=\"btns clear\">\n			  <a class=\"button\" href=\"#\">BOOK</a>\n			  <p><a href=\"#\">REMOVE FROM SITTER TEAM</a></p>\n			</div>\n		  </li>\n		  <li>\n			<div class=\"tit\">\n			  <span><strong>$15</strong> /hr</span>\n			  <a href=\"#\">Samantha Chadwick</a>\n			</div>\n			<div class=\"img\">\n			  <a href=\"#\"><img src=\"/static/images/demo/img13.jpg\" alt=\"\" /></a>\n			</div>\n			<ul>\n			  <li><span class=\"icon_plus_box\">&nbsp;</span>Last hired: <span>April 23, 2013</span></li>\n			  <li><span class=\"icon_reload\">&nbsp;</span>4 jobs <span class=\"friends_span\"><span class=\"icon_friends4\">&nbsp;</span><a href=\"#\">24 sitter friends</a></span></li>\n			</ul>\n			<div class=\"btns clear\">\n			  <a class=\"button\" href=\"#\">BOOK</a>\n			  <p><a href=\"#\">REMOVE FROM SITTER TEAM</a></p>\n			</div>\n		  </li>\n		  <li>\n			<div class=\"tit\">\n			  <span><strong>$15</strong> /hr</span>\n			  <a href=\"#\">Samantha Chadwick</a>\n			</div>\n			<div class=\"img\">\n			  <a href=\"#\"><img src=\"/static/images/demo/img13.jpg\" alt=\"\" /></a>\n			</div>\n			<ul>\n			  <li><span class=\"icon_plus_box\">&nbsp;</span>Last hired: <span>April 23, 2013</span></li>\n			  <li><span class=\"icon_reload\">&nbsp;</span>4 jobs <span class=\"friends_span\"><span class=\"icon_friends4\">&nbsp;</span><a href=\"#\">24 sitter friends</a></span></li>\n			</ul>\n			<div class=\"btns clear\">\n			  <a class=\"button\" href=\"#\">BOOK</a>\n			  <p><a href=\"#\">REMOVE FROM SITTER TEAM</a></p>\n			</div>\n		  </li>\n		  <li>\n			<div class=\"tit\">\n			  <span><strong>$15</strong> /hr</span>\n			  <a href=\"#\">Samantha Chadwick</a>\n			</div>\n			<div class=\"img\">\n			  <a href=\"#\"><img src=\"/static/images/demo/img13.jpg\" alt=\"\" /></a>\n			</div>\n			<ul>\n			  <li><span class=\"icon_plus_box\">&nbsp;</span>Last hired: <span>April 23, 2013</span></li>\n			  <li><span class=\"icon_reload\">&nbsp;</span>4 jobs <span class=\"friends_span\"><span class=\"icon_friends4\">&nbsp;</span><a href=\"#\">24 sitter friends</a></span></li>\n			</ul>\n			<div class=\"btns clear\">\n			  <a class=\"button\" href=\"#\">BOOK</a>\n			  <p><a href=\"#\">REMOVE FROM SITTER TEAM</a></p>\n			</div>\n		  </li>\n		</ul>\n	  </div>\n	  <!-- /sitter_team -->\n");
  
});
Ember.TEMPLATES["sitter"] = Ember.Handlebars.template(function anonymous(Handlebars,depth0,helpers,partials,data) {
this.compilerInfo = [3,'>= 1.0.0-rc.4'];
helpers = helpers || Ember.Handlebars.helpers; data = data || {};
  


  data.buffer.push("<div class=\"container clear\">\n  <div class=\"wraper\">\n\n	<!-- stat_bar -->\n	<div class=\"stat_bar clear\" id=\"fixed_tabs\">\n	  <p><span class=\"icon_check2\">&nbsp;</span>Background Cleared</p>\n	  <ul>\n		<li><span class=\"icon_pin6\">&nbsp;</span>New York, NY</li>\n		<li><span class=\"icon_dollar2\">&nbsp;</span>from $15 /hr</li>\n		<li><span class=\"icon_review2\">&nbsp;</span>11 reviews</li>\n		<li><span class=\"icon_friends8\">&nbsp;</span>24 sitter friends</li>\n	  </ul>\n	</div>\n	<!-- /stat_bar -->\n\n	<!-- tabs_wrap -->\n	<div class=\"tabs_wrap\">\n	  <ul class=\"tab_select\">\n		<li><a href=\"#tab-1\">About</a></li>\n		<li><a href=\"#tab-2\">Reviews</a></li>\n		<li><a href=\"#tab-3\">Sitter Friends</a></li>\n	  </ul>\n\n	  <!-- about_block -->\n	  <div class=\"tab_content about_block\" id=\"tab-1\">\n		<ul class=\"subtab_select\">\n		  <li><a href=\"#tab-1-1\">Snapshot</a></li>\n		  <li><a href=\"#tab-1-2\">Details</a></li>\n		</ul>\n		<!-- snapshot_block -->\n		<div class=\"subtab_content snapshot_block\" id=\"tab-1-1\">\n		  <p>Need to know</p>\n		  <ul class=\"clear\">\n			<li><span class=\"icon_certification\">&nbsp;</span><strong>Studying</strong> at <strong>Hoboken Nursing School</strong></li>\n			<li><span class=\"icon_education\">&nbsp;</span>Graduated <strong>college</strong></li>\n			<li><span class=\"icon_pin2\">&nbsp;</span>Located in <strong>New York, NY</strong></li>\n			<li><span class=\"icon_certification2\">&nbsp;</span><strong>CPR</strong> and <strong>First Aid</strong> certified</li>\n			<li><span class=\"icon_age\">&nbsp;</span><strong>25</strong> years old</li>\n			<li><span class=\"icon_other\">&nbsp;</span>Will do <strong>light housekeeping</strong></li>\n			<li><span class=\"icon_transportation\">&nbsp;</span>Has <strong>current driver’s license</strong></li>\n			<li><span class=\"icon_rates\">&nbsp;</span><strong>$15/hr - $20/hr</strong> standard rates</li>\n			<li><span class=\"icon_experience\">&nbsp;</span><strong>6 years</strong> of experience with kids</li>\n		  </ul>\n		</div>\n		<!-- /snapshot_block -->\n		<!-- about_details_block -->\n		<div class=\"mob_tab_trigger active\">About</div>\n		<div class=\"subtab_content about_details_block\" id=\"tab-1-2\">\n		  <ul>\n			<li>\n			  <ul>\n				<li><span class=\"icon_pin4\">&nbsp;</span>Location</li>\n				<li>\n				  <p><span>Lives in</span>New York, NY</p>\n				  <p><span>Will work within</span>10-11</p>\n				</li>\n			  </ul>\n			</li>\n			<li>\n			  <ul>\n				<li><span class=\"icon_age2\">&nbsp;</span>Age</li>\n				<li>\n				  <p>25</p>\n				</li>\n			  </ul>\n			</li>\n			<li>\n			  <ul>\n				<li><span class=\"icon_smoker2\">&nbsp;</span>Smoker</li>\n				<li>\n				  <p><img src=\"/static/images/icons/no.png\" alt=\"\" /> <strong>No</strong></p>\n				</li>\n			  </ul>\n			</li>\n			<li>\n			  <ul>\n				<li><span class=\"icon_transportation2\">&nbsp;</span>Transportation</li>\n				<li>\n				  <p>I am willing to transport children to and from events, activities, school, or appointments.</p>\n				</li>\n			  </ul>\n			</li>\n			<li>\n			  <ul>\n				<li><span class=\"icon_experience2\">&nbsp;</span>General Experience</li>\n				<li>\n				  <p><span>Total years of experience</span>4 Years</p>\n				  <p><span>Experience with Infants</span>1-2 years</p>\n				  <p><span>Experience with Toddlers</span>1-2 years</p>\n				  <p><span>Experience with Preschoolers</span>1-2 years</p>\n				  <p><span>Experience with School Age</span>1-2 years</p>\n				  <p><span>Experience with Pre Teens</span>No Experience</p>\n				  <p><span>Experience with Teenagers</span>No Experience</p>\n				</li>\n			  </ul>\n			</li>\n			<li>\n			  <ul>\n				<li><span class=\"icon_education3\">&nbsp;</span>Education</li>\n				<li>\n				  <p><span>Education Level</span>Advanced Degree</p>\n				  <p><span>Last School Attended</span>Bank Street College of Education</p>\n				  <p><span>Currently</span>Attending school</p>\n				</li>\n			  </ul>\n			</li>\n			<li>\n			  <ul>\n				<li><span class=\"icon_certification3\">&nbsp;</span>Certifications</li>\n				<li>\n				  <p>Current Infant/Child CPR Certification, Teacher License</p>\n				</li>\n			  </ul>\n			</li>\n			<li>\n			  <ul>\n				<li><span class=\"icon_availability2\">&nbsp;</span>General Availability</li>\n				<li>\n				  <p>Regular, part-time, Occasional sitting</p>\n				</li>\n			  </ul>\n			</li>\n			<li>\n			  <ul>\n				<li><span class=\"icon_other2\">&nbsp;</span>Other Services</li>\n				<li>\n				  <p>Homework Assistance/Tutoring, Grocery Shopping</p>\n				</li>\n			  </ul>\n			</li>\n			<li>\n			  <ul>\n				<li><span class=\"icon_rates2\">&nbsp;</span>Standard Rates</li>\n				<li>\n				  <p><span>Standard rates for one child</span>Min Rate: <strong>$20</strong> /hr &nbsp;  Max Rate: <strong>$25</strong> /hr </p>\n				  <p><span>Standard rates for two children</span>Min Rate: <strong>$20</strong> /hr &nbsp;  Max Rate: <strong>$25</strong> /hr </p>\n				</li>\n			  </ul>\n			</li>\n			<li>\n			  <ul>\n				<li><span class=\"icon_preferences2\">&nbsp;</span>Job Preferences</li>\n				<li>\n				  <p><span>Will you babysit in the home of smokers</span><img src=\"/static/images/icons/yes.png\" alt=\"\" /> <strong>Yes</strong></p>\n				  <p><span>Will you babysit in a home with dogs</span><img src=\"/static/images/icons/no.png\" alt=\"\" /> <strong>No</strong></p>\n				  <p><span>Will you babysit in a home with cats</span><img src=\"/static/images/icons/yes.png\" alt=\"\" /> <strong>Yes</strong></p>\n				  <p><span>Will you babysit in a home that has other animals</span><img src=\"/static/images/icons/no.png\" alt=\"\" /> <strong>No</strong></p>\n				</li>\n			  </ul>\n			</li>\n		  </ul>\n		</div>\n		<!-- /about_details_block -->\n	  </div>\n	  <!-- /about_block -->\n\n	  <!-- reviews_block -->\n	  <div class=\"mob_tab_trigger\">Reviews</div>\n	  <div class=\"tab_content reviews_block\" id=\"tab-2\">\n		<div class=\"reco clear\"><a href=\"#recommend_popup\"><span class=\"icon_team2\">&nbsp;</span>RECOMMEND ELLEN</a></div>\n		<ul class=\"clear\">\n		  <li>\n			<a href=\"#\"><img src=\"/static/images/demo/img11.jpg\" alt=\"\" /></a>\n			<div class=\"desc\">\n			  <p><a href=\"#\">Marcie Silk</a></p>\n			  <div class=\"reco_btn\"><span class=\"icon_ok\">&nbsp;</span>Recommends</div>\n			  <p>Sed auctor neque eu tellus rhoncus ut eleifend nibh porttitor. Ut in nulla enim. Phasellus molestie magna non est bibendum non venenatis nisl tempor. Suspendisse dictum feugiat nisl ut dapibus. Mauris iaculis porttitor posuere. Praesent id metus massa, ut blandit odio. Proin quis tortor orci. Etiam at risus et justo dignissim congue. Donec congue lacinia dui, a porttitor lectus condimentum laoreet. Nunc eu ullamcorper orci. Quisque eget odio ac lectus vestibulum faucibus eget in metus. In pellentesque faucibus vestibulum. </p>\n			  <p>Nulla at nulla justo, eget luctus tortor. Nulla facilisi. Duis aliquet egestas purus in blandit. Curabitur vulputate, ligula lacinia scelerisque tempor, lacus lacus ornare ante, ac egestas est urna sit amet.</p>\n			</div>\n		  </li>\n		  <li>\n			<a href=\"#\"><img src=\"/static/images/demo/img12.jpg\" alt=\"\" /></a>\n			<div class=\"desc\">\n			  <p><a href=\"#\">Otis Devin</a></p>\n			  <p>Sed auctor neque eu tellus rhoncus ut eleifend nibh porttitor. Ut in nulla enim. Phasellus molestie magna non est bibendum non venenatis nisl tempor. Suspendisse dictum feugiat nisl ut dapibus. Mauris iaculis porttitor posuere. Praesent id metus massa, ut blandit odio. Proin quis tortor orci. Etiam at risus et justo dignissim congue. Donec congue lacinia dui, a porttitor lectus condimentum laoreet. </p>\n			</div>\n		  </li>\n		</ul>\n	  </div>\n	  <!-- /reviews_block -->\n\n	  <!-- friends_block -->\n	  <div class=\"mob_tab_trigger\">Sitter Friends</div>\n	  <div class=\"tab_content friends_block\" id=\"tab-3\">\n		<ul class=\"clear\">\n		  <li>\n			<div class=\"bookmark\"></div>\n			<div class=\"tit\">\n			  <span><strong>$15</strong> /hr</span>\n			  <a href=\"#\">Ellen Vukelich</a>\n			</div>\n			<div class=\"img\">\n			  <div class=\"heart\"></div>\n			  <a href=\"#\"><img src=\"/static/images/demo/img13.jpg\" alt=\"\" /></a>\n			  <span>Background Cleared</span>\n			</div>\n			<ul>\n			  <li><span class=\"icon_friends3\">&nbsp;</span>5 mutual friends\n			  <ul>\n				<li>Friends you have in common</li>\n				<li><a href=\"#\"><img src=\"/static/images/demo/img3.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n				<li><a href=\"#\"><img src=\"/static/images/demo/img4.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n				<li><a href=\"#\"><img src=\"/static/images/demo/img5.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n				<li><a href=\"#\"><img src=\"/static/images/demo/img6.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n				<li><a href=\"#\"><img src=\"/static/images/demo/img7.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n				<li><a href=\"#\"><img src=\"/static/images/demo/img8.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n				<li><a href=\"#\"><img src=\"/static/images/demo/img9.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n				<li><a href=\"#\"><img src=\"/static/images/demo/img10.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n			  </ul>\n			  </li>\n			  <li><span class=\"icon_recommend2\">&nbsp;</span>4 recommends\n			  <ul>\n				<li>Recommendations</li>\n				<li><a href=\"#\"><img src=\"/static/images/demo/img3.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n				<li><a href=\"#\"><img src=\"/static/images/demo/img4.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n				<li><a href=\"#\"><img src=\"/static/images/demo/img5.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n				<li><a href=\"#\"><img src=\"/static/images/demo/img6.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n				<li><a href=\"#\"><img src=\"/static/images/demo/img7.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n				<li><a href=\"#\"><img src=\"/static/images/demo/img8.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n				<li><a href=\"#\"><img src=\"/static/images/demo/img9.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n				<li><a href=\"#\"><img src=\"/static/images/demo/img10.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n			  </ul>\n			  </li>\n			  <li><span class=\"icon_team3\">&nbsp;</span>9 sitter teams\n			  <ul>\n				<li>Added to sitter teams and repeatedly hired</li>\n				<li><a href=\"#\"><img src=\"/static/images/demo/img3.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n				<li><a href=\"#\"><img src=\"/static/images/demo/img4.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n				<li><a href=\"#\"><img src=\"/static/images/demo/img5.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n				<li><a href=\"#\"><img src=\"/static/images/demo/img6.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n				<li><a href=\"#\"><img src=\"/static/images/demo/img7.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n				<li><a href=\"#\"><img src=\"/static/images/demo/img8.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n				<li><a href=\"#\"><img src=\"/static/images/demo/img9.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n				<li><a href=\"#\"><img src=\"/static/images/demo/img10.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n			  </ul>\n			  </li>\n			  <li><span class=\"icon_reviews\">&nbsp;</span>11 reviews\n			  <ul>\n				<li class=\"rev clear\">\n				  <a href=\"#\"><img src=\"/static/images/demo/img3.jpg\" alt=\"\" /></a>\n				  <div>\n					<p>Ellen has been a sitter for my children fore more than a year and I couldn’t be happier! She arrives on time and my kids light up when they see her!</p>\n					<p><a href=\"#\">Read more reviews </a></p>\n				  </div>\n				</li>\n			  </ul>\n			  </li>\n			</ul>\n			<div class=\"btns clear\">\n			  <a class=\"button\" href=\"#\">BOOK</a><a class=\"button button2\" href=\"#\">INTERVIEW</a>\n			  <p><a href=\"#\">ADD TO SITTER TEAM</a></p>\n			  <p><a href=\"#\">BOOKMARK</a></p>\n			</div>\n		  </li>\n		  <li>\n			<div class=\"bookmark\"></div>\n			<div class=\"tit\">\n			  <span><strong>$15</strong> /hr</span>\n			  <a href=\"#\">Ellen Vukelich</a>\n			</div>\n			<div class=\"img\">\n			  <div class=\"heart\"></div>\n			  <a href=\"#\"><img src=\"/static/images/demo/img13.jpg\" alt=\"\" /></a>\n			  <span>Background Cleared</span>\n			</div>\n			<ul>\n			  <li><span class=\"icon_friends3\">&nbsp;</span>5 mutual friends\n			  <ul>\n				<li>Friends you have in common</li>\n				<li><a href=\"#\"><img src=\"/static/images/demo/img3.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n				<li><a href=\"#\"><img src=\"/static/images/demo/img4.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n				<li><a href=\"#\"><img src=\"/static/images/demo/img5.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n				<li><a href=\"#\"><img src=\"/static/images/demo/img6.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n				<li><a href=\"#\"><img src=\"/static/images/demo/img7.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n				<li><a href=\"#\"><img src=\"/static/images/demo/img8.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n				<li><a href=\"#\"><img src=\"/static/images/demo/img9.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n				<li><a href=\"#\"><img src=\"/static/images/demo/img10.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n			  </ul>\n			  </li>\n			  <li><span class=\"icon_recommend2\">&nbsp;</span>4 recommends\n			  <ul>\n				<li>Recommendations</li>\n				<li><a href=\"#\"><img src=\"/static/images/demo/img3.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n				<li><a href=\"#\"><img src=\"/static/images/demo/img4.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n				<li><a href=\"#\"><img src=\"/static/images/demo/img5.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n				<li><a href=\"#\"><img src=\"/static/images/demo/img6.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n				<li><a href=\"#\"><img src=\"/static/images/demo/img7.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n				<li><a href=\"#\"><img src=\"/static/images/demo/img8.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n				<li><a href=\"#\"><img src=\"/static/images/demo/img9.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n				<li><a href=\"#\"><img src=\"/static/images/demo/img10.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n			  </ul>\n			  </li>\n			  <li><span class=\"icon_team3\">&nbsp;</span>9 sitter teams\n			  <ul>\n				<li>Added to sitter teams and repeatedly hired</li>\n				<li><a href=\"#\"><img src=\"/static/images/demo/img3.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n				<li><a href=\"#\"><img src=\"/static/images/demo/img4.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n				<li><a href=\"#\"><img src=\"/static/images/demo/img5.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n				<li><a href=\"#\"><img src=\"/static/images/demo/img6.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n				<li><a href=\"#\"><img src=\"/static/images/demo/img7.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n				<li><a href=\"#\"><img src=\"/static/images/demo/img8.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n				<li><a href=\"#\"><img src=\"/static/images/demo/img9.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n				<li><a href=\"#\"><img src=\"/static/images/demo/img10.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n			  </ul>\n			  </li>\n			  <li><span class=\"icon_reviews\">&nbsp;</span>11 reviews\n			  <ul>\n				<li class=\"rev clear\">\n				  <a href=\"#\"><img src=\"/static/images/demo/img3.jpg\" alt=\"\" /></a>\n				  <div>\n					<p>Ellen has been a sitter for my children fore more than a year and I couldn’t be happier! She arrives on time and my kids light up when they see her!</p>\n					<p><a href=\"#\">Read more reviews </a></p>\n				  </div>\n				</li>\n			  </ul>\n			  </li>\n			</ul>\n			<div class=\"btns clear\">\n			  <a class=\"button\" href=\"#\">BOOK</a><a class=\"button button2\" href=\"#\">INTERVIEW</a>\n			  <p><a href=\"#\">ADD TO SITTER TEAM</a></p>\n			  <p><a href=\"#\">BOOKMARK</a></p>\n			</div>\n		  </li>\n		  <li>\n			<div class=\"bookmark\"></div>\n			<div class=\"tit\">\n			  <span><strong>$15</strong> /hr</span>\n			  <a href=\"#\">Ellen Vukelich</a>\n			</div>\n			<div class=\"img\">\n			  <div class=\"heart\"></div>\n			  <a href=\"#\"><img src=\"/static/images/demo/img13.jpg\" alt=\"\" /></a>\n			  <span>Background Cleared</span>\n			</div>\n			<ul>\n			  <li><span class=\"icon_friends3\">&nbsp;</span>5 mutual friends\n			  <ul>\n				<li>Friends you have in common</li>\n				<li><a href=\"#\"><img src=\"/static/images/demo/img3.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n				<li><a href=\"#\"><img src=\"/static/images/demo/img4.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n				<li><a href=\"#\"><img src=\"/static/images/demo/img5.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n				<li><a href=\"#\"><img src=\"/static/images/demo/img6.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n				<li><a href=\"#\"><img src=\"/static/images/demo/img7.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n				<li><a href=\"#\"><img src=\"/static/images/demo/img8.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n				<li><a href=\"#\"><img src=\"/static/images/demo/img9.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n				<li><a href=\"#\"><img src=\"/static/images/demo/img10.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n			  </ul>\n			  </li>\n			  <li><span class=\"icon_recommend2\">&nbsp;</span>4 recommends\n			  <ul>\n				<li>Recommendations</li>\n				<li><a href=\"#\"><img src=\"/static/images/demo/img3.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n				<li><a href=\"#\"><img src=\"/static/images/demo/img4.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n				<li><a href=\"#\"><img src=\"/static/images/demo/img5.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n				<li><a href=\"#\"><img src=\"/static/images/demo/img6.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n				<li><a href=\"#\"><img src=\"/static/images/demo/img7.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n				<li><a href=\"#\"><img src=\"/static/images/demo/img8.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n				<li><a href=\"#\"><img src=\"/static/images/demo/img9.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n				<li><a href=\"#\"><img src=\"/static/images/demo/img10.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n			  </ul>\n			  </li>\n			  <li><span class=\"icon_team3\">&nbsp;</span>9 sitter teams\n			  <ul>\n				<li>Added to sitter teams and repeatedly hired</li>\n				<li><a href=\"#\"><img src=\"/static/images/demo/img3.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n				<li><a href=\"#\"><img src=\"/static/images/demo/img4.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n				<li><a href=\"#\"><img src=\"/static/images/demo/img5.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n				<li><a href=\"#\"><img src=\"/static/images/demo/img6.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n				<li><a href=\"#\"><img src=\"/static/images/demo/img7.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n				<li><a href=\"#\"><img src=\"/static/images/demo/img8.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n				<li><a href=\"#\"><img src=\"/static/images/demo/img9.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n				<li><a href=\"#\"><img src=\"/static/images/demo/img10.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n			  </ul>\n			  </li>\n			  <li><span class=\"icon_reviews\">&nbsp;</span>11 reviews\n			  <ul>\n				<li class=\"rev clear\">\n				  <a href=\"#\"><img src=\"/static/images/demo/img3.jpg\" alt=\"\" /></a>\n				  <div>\n					<p>Ellen has been a sitter for my children fore more than a year and I couldn’t be happier! She arrives on time and my kids light up when they see her!</p>\n					<p><a href=\"#\">Read more reviews </a></p>\n				  </div>\n				</li>\n			  </ul>\n			  </li>\n			</ul>\n			<div class=\"btns clear\">\n			  <a class=\"button\" href=\"#\">BOOK</a><a class=\"button button2\" href=\"#\">INTERVIEW</a>\n			  <p><a href=\"#\">ADD TO SITTER TEAM</a></p>\n			  <p><a href=\"#\">BOOKMARK</a></p>\n			</div>\n		  </li>\n		  <li>\n			<div class=\"bookmark\"></div>\n			<div class=\"tit\">\n			  <span><strong>$15</strong> /hr</span>\n			  <a href=\"#\">Ellen Vukelich</a>\n			</div>\n			<div class=\"img\">\n			  <div class=\"heart\"></div>\n			  <a href=\"#\"><img src=\"/static/images/demo/img13.jpg\" alt=\"\" /></a>\n			  <span>Background Cleared</span>\n			</div>\n			<ul>\n			  <li><span class=\"icon_friends3\">&nbsp;</span>5 mutual friends\n			  <ul>\n				<li>Friends you have in common</li>\n				<li><a href=\"#\"><img src=\"/static/images/demo/img3.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n				<li><a href=\"#\"><img src=\"/static/images/demo/img4.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n				<li><a href=\"#\"><img src=\"/static/images/demo/img5.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n				<li><a href=\"#\"><img src=\"/static/images/demo/img6.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n				<li><a href=\"#\"><img src=\"/static/images/demo/img7.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n				<li><a href=\"#\"><img src=\"/static/images/demo/img8.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n				<li><a href=\"#\"><img src=\"/static/images/demo/img9.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n				<li><a href=\"#\"><img src=\"/static/images/demo/img10.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n			  </ul>\n			  </li>\n			  <li><span class=\"icon_recommend2\">&nbsp;</span>4 recommends\n			  <ul>\n				<li>Recommendations</li>\n				<li><a href=\"#\"><img src=\"/static/images/demo/img3.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n				<li><a href=\"#\"><img src=\"/static/images/demo/img4.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n				<li><a href=\"#\"><img src=\"/static/images/demo/img5.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n				<li><a href=\"#\"><img src=\"/static/images/demo/img6.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n				<li><a href=\"#\"><img src=\"/static/images/demo/img7.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n				<li><a href=\"#\"><img src=\"/static/images/demo/img8.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n				<li><a href=\"#\"><img src=\"/static/images/demo/img9.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n				<li><a href=\"#\"><img src=\"/static/images/demo/img10.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n			  </ul>\n			  </li>\n			  <li><span class=\"icon_team3\">&nbsp;</span>9 sitter teams\n			  <ul>\n				<li>Added to sitter teams and repeatedly hired</li>\n				<li><a href=\"#\"><img src=\"/static/images/demo/img3.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n				<li><a href=\"#\"><img src=\"/static/images/demo/img4.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n				<li><a href=\"#\"><img src=\"/static/images/demo/img5.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n				<li><a href=\"#\"><img src=\"/static/images/demo/img6.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n				<li><a href=\"#\"><img src=\"/static/images/demo/img7.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n				<li><a href=\"#\"><img src=\"/static/images/demo/img8.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n				<li><a href=\"#\"><img src=\"/static/images/demo/img9.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n				<li><a href=\"#\"><img src=\"/static/images/demo/img10.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n			  </ul>\n			  </li>\n			  <li><span class=\"icon_reviews\">&nbsp;</span>11 reviews\n			  <ul>\n				<li class=\"rev clear\">\n				  <a href=\"#\"><img src=\"/static/images/demo/img3.jpg\" alt=\"\" /></a>\n				  <div>\n					<p>Ellen has been a sitter for my children fore more than a year and I couldn’t be happier! She arrives on time and my kids light up when they see her!</p>\n					<p><a href=\"#\">Read more reviews </a></p>\n				  </div>\n				</li>\n			  </ul>\n			  </li>\n			</ul>\n			<div class=\"btns clear\">\n			  <a class=\"button\" href=\"#\">BOOK</a><a class=\"button button2\" href=\"#\">INTERVIEW</a>\n			  <p><a href=\"#\">ADD TO SITTER TEAM</a></p>\n			  <p><a href=\"#\">BOOKMARK</a></p>\n			</div>\n		  </li>\n		  <li>\n			<div class=\"bookmark\"></div>\n			<div class=\"tit\">\n			  <span><strong>$15</strong> /hr</span>\n			  <a href=\"#\">Ellen Vukelich</a>\n			</div>\n			<div class=\"img\">\n			  <div class=\"heart\"></div>\n			  <a href=\"#\"><img src=\"/static/images/demo/img13.jpg\" alt=\"\" /></a>\n			  <span>Background Cleared</span>\n			</div>\n			<ul>\n			  <li><span class=\"icon_friends3\">&nbsp;</span>5 mutual friends\n			  <ul>\n				<li>Friends you have in common</li>\n				<li><a href=\"#\"><img src=\"/static/images/demo/img3.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n				<li><a href=\"#\"><img src=\"/static/images/demo/img4.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n				<li><a href=\"#\"><img src=\"/static/images/demo/img5.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n				<li><a href=\"#\"><img src=\"/static/images/demo/img6.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n				<li><a href=\"#\"><img src=\"/static/images/demo/img7.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n				<li><a href=\"#\"><img src=\"/static/images/demo/img8.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n				<li><a href=\"#\"><img src=\"/static/images/demo/img9.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n				<li><a href=\"#\"><img src=\"/static/images/demo/img10.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n			  </ul>\n			  </li>\n			  <li><span class=\"icon_recommend2\">&nbsp;</span>4 recommends\n			  <ul>\n				<li>Recommendations</li>\n				<li><a href=\"#\"><img src=\"/static/images/demo/img3.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n				<li><a href=\"#\"><img src=\"/static/images/demo/img4.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n				<li><a href=\"#\"><img src=\"/static/images/demo/img5.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n				<li><a href=\"#\"><img src=\"/static/images/demo/img6.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n				<li><a href=\"#\"><img src=\"/static/images/demo/img7.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n				<li><a href=\"#\"><img src=\"/static/images/demo/img8.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n				<li><a href=\"#\"><img src=\"/static/images/demo/img9.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n				<li><a href=\"#\"><img src=\"/static/images/demo/img10.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n			  </ul>\n			  </li>\n			  <li><span class=\"icon_team3\">&nbsp;</span>9 sitter teams\n			  <ul>\n				<li>Added to sitter teams and repeatedly hired</li>\n				<li><a href=\"#\"><img src=\"/static/images/demo/img3.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n				<li><a href=\"#\"><img src=\"/static/images/demo/img4.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n				<li><a href=\"#\"><img src=\"/static/images/demo/img5.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n				<li><a href=\"#\"><img src=\"/static/images/demo/img6.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n				<li><a href=\"#\"><img src=\"/static/images/demo/img7.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n				<li><a href=\"#\"><img src=\"/static/images/demo/img8.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n				<li><a href=\"#\"><img src=\"/static/images/demo/img9.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n				<li><a href=\"#\"><img src=\"/static/images/demo/img10.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n			  </ul>\n			  </li>\n			  <li><span class=\"icon_reviews\">&nbsp;</span>11 reviews\n			  <ul>\n				<li class=\"rev clear\">\n				  <a href=\"#\"><img src=\"/static/images/demo/img3.jpg\" alt=\"\" /></a>\n				  <div>\n					<p>Ellen has been a sitter for my children fore more than a year and I couldn’t be happier! She arrives on time and my kids light up when they see her!</p>\n					<p><a href=\"#\">Read more reviews </a></p>\n				  </div>\n				</li>\n			  </ul>\n			  </li>\n			</ul>\n			<div class=\"btns clear\">\n			  <a class=\"button\" href=\"#\">BOOK</a><a class=\"button button2\" href=\"#\">INTERVIEW</a>\n			  <p><a href=\"#\">ADD TO SITTER TEAM</a></p>\n			  <p><a href=\"#\">BOOKMARK</a></p>\n			</div>\n		  </li>\n		</ul>\n	  </div>\n	  <!-- /friends_block -->\n\n	</div>\n	<!-- /tabs_wrap -->\n\n  </div>\n</div>");
  
});
Ember.TEMPLATES["sitter/top"] = Ember.Handlebars.template(function anonymous(Handlebars,depth0,helpers,partials,data) {
this.compilerInfo = [3,'>= 1.0.0-rc.4'];
helpers = helpers || Ember.Handlebars.helpers; data = data || {};
  var buffer = '', hashContexts, hashTypes, escapeExpression=this.escapeExpression;


  data.buffer.push("<div class=\"top_info clear\">\n  <div class=\"bookmark\"></div>\n  <div class=\"member_since\">Feb 2013</div>\n  <div class=\"photo\">\n	<div class=\"heart_wrap\">\n	  <div class=\"heart\"></div>\n	  <span>Add to my sitter team</span>\n	</div>\n	<img ");
  hashContexts = {'src': depth0};
  hashTypes = {'src': "STRING"};
  data.buffer.push(escapeExpression(helpers.bindAttr.call(depth0, {hash:{
    'src': ("avatarUrl")
  },contexts:[],types:[],hashContexts:hashContexts,hashTypes:hashTypes,data:data})));
  data.buffer.push(" alt=\"\" />\n  </div>\n  <div class=\"desc\">\n	<p><a class=\"button\" href=\"#\">BOOK</a><a class=\"button button2\" href=\"#\">INTERVIEW</a></p>\n	<p><span>Hi, I'm <strong>");
  hashTypes = {};
  hashContexts = {};
  data.buffer.push(escapeExpression(helpers._triageMustache.call(depth0, "full_name", {hash:{},contexts:[depth0],types:["ID"],hashContexts:hashContexts,hashTypes:hashTypes,data:data})));
  data.buffer.push("</strong></span></p>\n    ");
  hashTypes = {};
  hashContexts = {};
  data.buffer.push(escapeExpression(helpers._triageMustache.call(depth0, "biography", {hash:{},contexts:[depth0],types:["ID"],hashContexts:hashContexts,hashTypes:hashTypes,data:data})));
  data.buffer.push("<a href=\"#\" class=\"read_more\">Read More</a></p>\n	<div class=\"full_desc\">\n	  <p>");
  hashTypes = {};
  hashContexts = {};
  data.buffer.push(escapeExpression(helpers._triageMustache.call(depth0, "biography", {hash:{},contexts:[depth0],types:["ID"],hashContexts:hashContexts,hashTypes:hashTypes,data:data})));
  data.buffer.push("</p>\n	</div>\n  </div>\n  <div class=\"ico\">\n	<ul>\n	  <li><span class=\"icon_friends\">&nbsp;</span><span class=\"number\">5</span>mutual friends\n	  <ul>\n		<li>Friends you have in common with Ellen</li>\n		<li><a href=\"#\"><img src=\"/static/images/demo/img3.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n		<li><a href=\"#\"><img src=\"/static/images/demo/img4.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n		<li><a href=\"#\"><img src=\"/static/images/demo/img5.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n		<li><a href=\"#\"><img src=\"/static/images/demo/img6.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n		<li><a href=\"#\"><img src=\"/static/images/demo/img7.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n		<li><a href=\"#\"><img src=\"/static/images/demo/img8.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n		<li><a href=\"#\"><img src=\"/static/images/demo/img9.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n		<li><a href=\"#\"><img src=\"/static/images/demo/img10.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n	  </ul>\n	  </li>\n	  <li><span class=\"icon_recommend\">&nbsp;</span><span class=\"number\">4</span>recommends\n	  <ul>\n		<li>Friends who recommend Ellen</li>\n		<li><a href=\"#\"><img src=\"/static/images/demo/img3.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n		<li><a href=\"#\"><img src=\"/static/images/demo/img4.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n		<li><a href=\"#\"><img src=\"/static/images/demo/img5.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n		<li><a href=\"#\"><img src=\"/static/images/demo/img6.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n		<li><a href=\"#\"><img src=\"/static/images/demo/img7.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n		<li><a href=\"#\"><img src=\"/static/images/demo/img8.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n		<li><a href=\"#\"><img src=\"/static/images/demo/img9.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n		<li><a href=\"#\"><img src=\"/static/images/demo/img10.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n	  </ul>\n	  </li>\n	  <li><span class=\"icon_team\">&nbsp;</span><span class=\"number\">9</span>sitter teams\n	  <ul>\n		<li>Friends who added Ellen to their sitter team</li>\n		<li><a href=\"#\"><img src=\"/static/images/demo/img3.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n		<li><a href=\"#\"><img src=\"/static/images/demo/img4.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n		<li><a href=\"#\"><img src=\"/static/images/demo/img5.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n		<li><a href=\"#\"><img src=\"/static/images/demo/img6.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n		<li><a href=\"#\"><img src=\"/static/images/demo/img7.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n		<li><a href=\"#\"><img src=\"/static/images/demo/img8.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n		<li><a href=\"#\"><img src=\"/static/images/demo/img9.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n		<li><a href=\"#\"><img src=\"/static/images/demo/img10.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n	  </ul>\n	  </li>\n	</ul>\n  </div>\n</div>");
  return buffer;
  
});
Ember.TEMPLATES["profile/topInfo"] = Ember.Handlebars.template(function anonymous(Handlebars,depth0,helpers,partials,data) {
this.compilerInfo = [3,'>= 1.0.0-rc.4'];
helpers = helpers || Ember.Handlebars.helpers; data = data || {};
  


  data.buffer.push("		<div class=\"top_info clear\">\n			<div class=\"bookmark\"></div>\n			<div class=\"member_since\">Feb 2013</div>\n			<div class=\"photo\">\n				<div class=\"heart_wrap\">\n					<div class=\"heart\"></div>\n					<span>Add to my sitter team</span>\n				</div>\n				<img src=\"/static/images/demo/img2.jpg\" alt=\"\" />\n			</div>\n			<div class=\"desc\">\n				<p><a class=\"button\" href=\"#\">BOOK</a><a class=\"button button2\" href=\"#\">INTERVIEW</a></p>\n				<p><span>Hi, I'm <strong>Ellen Vukelich</strong></span></p>\n				<p>Nunc eu ullamcorper orci. Quisque eget odio ac lectus vestibulum faucibus eget in metus. In pellentesque faucibus vestibulum. Quisque eget odio ac lectus vestibulum faucibus eget in metus. In pellentesque faucibus vestibulum  <a href=\"#\" class=\"read_more\">Read More</a></p>\n				<div class=\"full_desc\">\n					<p>Nunc eu ullamcorper orci. Quisque eget odio ac lectus vestibulum faucibus eget in metus. In pellentesque faucibus vestibulum. Quisque eget odio ac lectus vestibulum faucibus eget in metus. In pellentesque faucibus vestibulum. Quisque eget odio ac lectus vestibulum faucibus eget in metus.</p>\n					<p>In pellentesque faucibus vestibulum. Quisque eget odio ac lectus vestibulum faucibus eget in metus. n pellentesque faucibus vestibulum. Quisque eget odio ac lectus vestibulum faucibus eget in metus.</p>\n					<p>Quisque eget odio ac lectus vestibulum faucibus eget in metus. In pellentesque faucibus vestibulum. Quisque eget odio ac lectus vestibulum faucibus eget in metus.</p>\n					<p>Nunc eu ullamcorper orci. Quisque eget odio ac lectus vestibulum faucibus eget in metus. In pellentesque faucibus vestibulum. Quisque eget odio ac lectus vestibulum faucibus eget in metus. In pellentesque faucibus vestibulum. Quisque eget odio ac lectus vestibulum faucibus eget in metus.</p>\n					<p>In pellentesque faucibus!</p>\n				</div>\n			</div>\n			<div class=\"ico\">\n				<ul>\n					<li><span class=\"icon_friends\">&nbsp;</span><span class=\"number\">5</span>mutual friends\n						<ul>\n							<li>Friends you have in common with Ellen</li>\n							<li><a href=\"#\"><img src=\"/static/images/demo/img3.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n							<li><a href=\"#\"><img src=\"/static/images/demo/img4.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n							<li><a href=\"#\"><img src=\"/static/images/demo/img5.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n							<li><a href=\"#\"><img src=\"/static/images/demo/img6.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n							<li><a href=\"#\"><img src=\"/static/images/demo/img7.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n							<li><a href=\"#\"><img src=\"/static/images/demo/img8.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n							<li><a href=\"#\"><img src=\"/static/images/demo/img9.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n							<li><a href=\"#\"><img src=\"/static/images/demo/img10.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n						</ul>\n					</li>\n					<li><span class=\"icon_recommend\">&nbsp;</span><span class=\"number\">4</span>recommends\n						<ul>\n							<li>Friends who recommend Ellen</li>\n							<li><a href=\"#\"><img src=\"/static/images/demo/img3.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n							<li><a href=\"#\"><img src=\"/static/images/demo/img4.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n							<li><a href=\"#\"><img src=\"/static/images/demo/img5.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n							<li><a href=\"#\"><img src=\"/static/images/demo/img6.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n							<li><a href=\"#\"><img src=\"/static/images/demo/img7.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n							<li><a href=\"#\"><img src=\"/static/images/demo/img8.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n							<li><a href=\"#\"><img src=\"/static/images/demo/img9.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n							<li><a href=\"#\"><img src=\"/static/images/demo/img10.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n						</ul>\n					</li>\n					<li><span class=\"icon_team\">&nbsp;</span><span class=\"number\">9</span>sitter teams\n						<ul>\n							<li>Friends who added Ellen to their sitter team</li>\n							<li><a href=\"#\"><img src=\"/static/images/demo/img3.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n							<li><a href=\"#\"><img src=\"/static/images/demo/img4.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n							<li><a href=\"#\"><img src=\"/static/images/demo/img5.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n							<li><a href=\"#\"><img src=\"/static/images/demo/img6.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n							<li><a href=\"#\"><img src=\"/static/images/demo/img7.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n							<li><a href=\"#\"><img src=\"/static/images/demo/img8.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n							<li><a href=\"#\"><img src=\"/static/images/demo/img9.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n							<li><a href=\"#\"><img src=\"/static/images/demo/img10.jpg\" alt=\"\" /></a><span>Andrea Barelli</span></li>\n						</ul>\n					</li>\n				</ul>\n			</div>\n		</div>\n");
  
});
})