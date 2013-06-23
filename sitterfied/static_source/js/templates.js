define(['ember'], function(Ember){Ember.TEMPLATES["searchResultsTop"] = Ember.Handlebars.template(function anonymous(Handlebars,depth0,helpers,partials,data) {
this.compilerInfo = [3,'>= 1.0.0-rc.4'];
helpers = helpers || Ember.Handlebars.helpers; data = data || {};
  


  data.buffer.push("<div class=\"find_form_block\">\n  <p>Where and when do you need your sitter?</p>\n  <form method=\"post\" action=\"#\">\n	<ul class=\"clear\">\n	  <li>\n		<label for=\"where\">Where</label>\n		<input id=\"where\" type=\"text\" value=\"Enter town or zipcode\" />\n	  </li>\n	  <li>\n		<label for=\"when\">When</label>\n		<input type=\"text\" id=\"datepicker\" />\n		<p><input type=\"checkbox\" id=\"check\" name=\"check\" /><label for=\"check\">Overnight / Multiday booking?</label></p>\n	  </li>\n	  <li>\n		<label for=\"from\">From</label>\n		<select id=\"from\" data-placeholder=\"\" tabindex=\"8\"><option>6:00 PM</option><option>7:00 PM</option></select>\n	  </li>\n	  <li>\n		<label for=\"to\">To</label>\n		<select id=\"to\" data-placeholder=\"\" tabindex=\"9\"><option>11:00 PM</option><option>12:00 PM</option></select>\n	  </li>\n	  <li>\n		<label>&nbsp;</label>\n		<select data-placeholder=\"\" tabindex=\"10\"><option>2 Kids</option><option>3 Kids</option></select>\n	  </li>\n	  <li><input type=\"submit\" value=\"FIND MY SITTER\" /></li>\n	</ul>\n  </form>\n  <p class=\"hide\"><a href=\"#\">Hide Search Bar</a></p>\n  <p class=\"show\"><a href=\"#\">Show Search Bar</a></p>\n</div>\n");
  
});
Ember.TEMPLATES["about"] = Ember.Handlebars.template(function anonymous(Handlebars,depth0,helpers,partials,data) {
this.compilerInfo = [3,'>= 1.0.0-rc.4'];
helpers = helpers || Ember.Handlebars.helpers; data = data || {};
  var buffer = '';


  return buffer;
  
});
Ember.TEMPLATES["noSearchResults"] = Ember.Handlebars.template(function anonymous(Handlebars,depth0,helpers,partials,data) {
this.compilerInfo = [3,'>= 1.0.0-rc.4'];
helpers = helpers || Ember.Handlebars.helpers; data = data || {};
  


  data.buffer.push("	  <!-- tabs_wrap -->\n	  <div class=\"tabs_wrap my_tabs_style tabs_no_results\">\n		<ul class=\"tab_select\">\n		  <li><a href=\"#tab-1\">sitter<br />team<span>0</span></a></li>\n		  <li><a href=\"#tab-2\">friends<br />sitters<span>0</span></a></li>\n		  <li><a href=\"#tab-3\">local<br />sitters<span>0</span></a></li>\n		</ul>\n\n		<!-- my_sitter_team -->\n		<div class=\"mob_tab_trigger my_mob_tab\">sitter<br />team<span>0</span></div>\n		<div class=\"tab_content my_sitter_team\" id=\"tab-1\">\n		  <!-- sitter team 0 -->\n		</div>\n		<!-- /my_sitter_team -->\n\n		<!-- my_friends_sitters -->\n		<div class=\"mob_tab_trigger my_mob_tab\">friends<br />sitters<span>0</span></div>\n		<div class=\"tab_content friends_block my_friends_sitters\" id=\"tab-2\">\n		  <!-- friends sitters 0 -->\n		</div>\n		<!-- /my_friends_sitters -->\n\n		<!-- my_local_sitters -->\n		<div class=\"mob_tab_trigger my_mob_tab\">local<br />sitters<span>0</span></div>\n		<div class=\"tab_content my_local_sitters\" id=\"tab-3\">\n		  <!-- local sitters 0 -->\n		</div>\n		<!-- /my_local_sitters -->\n\n	  </div>\n	  <!-- /tabs_wrap -->\n\n	  <!-- no_results -->\n	  <div class=\"no_results clear\">\n		<p>We’re not in your neighborhood just yet.</p>\n		<p>Here are a few things you can do right now.</p>\n		<ul>\n		  <li>\n			<p><a href=\"#\" class=\"button\">Invite</a></p>\n			<p>Invite your friends and discover great sitters together. We’ll even reward you and your friends with free months as they join Sitterfied</p>\n		  </li>\n		  <li>\n			<p><a href=\"#\" class=\"button\">Connect</a></p>\n			<p>Connect with your existing social networks to find great sitters through your friends</p>\n		  </li>\n		  <li>\n			<p><a href=\"#\" class=\"button\">Sign Up</a></p>\n			<p>Sign up to follow our progress and we’ll let you know when great sitters are added to your area</p>\n		  </li>\n		</ul>\n	  </div>\n	  <!-- /no_results -->\n");
  
});
Ember.TEMPLATES["index"] = Ember.Handlebars.template(function anonymous(Handlebars,depth0,helpers,partials,data) {
this.compilerInfo = [3,'>= 1.0.0-rc.4'];
helpers = helpers || Ember.Handlebars.helpers; data = data || {};
  var buffer = '', stack1, stack2, hashContexts, hashTypes, options, self=this, helperMissing=helpers.helperMissing, escapeExpression=this.escapeExpression;

function program1(depth0,data) {
  
  
  data.buffer.push("\n            <img src=\"/static/img/logo.png\" alt=\"\" />\n            ");
  }

function program3(depth0,data) {
  
  
  data.buffer.push(" Search ");
  }

  data.buffer.push("      <!-- header -->\n        <header class=\"header\">\n	      <div class=\"wraper\">\n		    ");
  hashContexts = {'class': depth0};
  hashTypes = {'class': "STRING"};
  options = {hash:{
    'class': ("logo")
  },inverse:self.noop,fn:self.program(1, program1, data),contexts:[depth0],types:["ID"],hashContexts:hashContexts,hashTypes:hashTypes,data:data};
  stack2 = ((stack1 = helpers.linkTo),stack1 ? stack1.call(depth0, "index", options) : helperMissing.call(depth0, "linkTo", "index", options));
  if(stack2 || stack2 === 0) { data.buffer.push(stack2); }
  data.buffer.push("\n		    <!-- top menu -->\n            <div class=\"menu_trigger\"></div>\n            <nav>\n              <ul>\n                <li>");
  hashTypes = {};
  hashContexts = {};
  options = {hash:{},inverse:self.noop,fn:self.program(3, program3, data),contexts:[depth0],types:["ID"],hashContexts:hashContexts,hashTypes:hashTypes,data:data};
  stack2 = ((stack1 = helpers.linkTo),stack1 ? stack1.call(depth0, "search", options) : helperMissing.call(depth0, "linkTo", "search", options));
  if(stack2 || stack2 === 0) { data.buffer.push(stack2); }
  data.buffer.push("</li>\n	            <li><a href=\"#\">Bookings</a></li>\n	            <li><a href=\"#\"><img src=\"/static/img/demo/img.jpg\" alt=\"\" /> Alex</a></li>\n              </ul>\n            </nav>\n		    <!-- /top menu -->\n		    <!-- top note -->\n		    <div class=\"top_note\">\n		    </div>\n		    <!-- /top note -->\n		    <div class=\"top_info clear\">\n              ");
  hashTypes = {};
  hashContexts = {};
  options = {hash:{},contexts:[depth0],types:["ID"],hashContexts:hashContexts,hashTypes:hashTypes,data:data};
  data.buffer.push(escapeExpression(((stack1 = helpers.outlet),stack1 ? stack1.call(depth0, "topInfo", options) : helperMissing.call(depth0, "outlet", "topInfo", options))));
  data.buffer.push("\n            </div>\n	      </div>\n        </header>\n        <!-- /header -->\n\n        <div class=\"container clear\">\n	      <div class=\"wraper\">\n            ");
  hashTypes = {};
  hashContexts = {};
  options = {hash:{},contexts:[depth0],types:["ID"],hashContexts:hashContexts,hashTypes:hashTypes,data:data};
  data.buffer.push(escapeExpression(((stack1 = helpers.outlet),stack1 ? stack1.call(depth0, "container", options) : helperMissing.call(depth0, "outlet", "container", options))));
  data.buffer.push("\n          </div>\n        </div>\n\n        <footer class=\"footer\">\n	      <div class=\"wraper\">\n		    <a href=\"#\" class=\"logo_bottom\"><img src=\"/static/img/logo_bottom.png\" alt=\"\" /></a>\n		    <!-- bottom menu -->\n            ");
  hashTypes = {};
  hashContexts = {};
  options = {hash:{},contexts:[depth0],types:["ID"],hashContexts:hashContexts,hashTypes:hashTypes,data:data};
  data.buffer.push(escapeExpression(((stack1 = helpers.outlet),stack1 ? stack1.call(depth0, "footer", options) : helperMissing.call(depth0, "outlet", "footer", options))));
  data.buffer.push("\n		    <!-- /bottom menu -->\n	      </div>\n        </footer>\n");
  return buffer;
  
});
Ember.TEMPLATES["noSearchResultsTop"] = Ember.Handlebars.template(function anonymous(Handlebars,depth0,helpers,partials,data) {
this.compilerInfo = [3,'>= 1.0.0-rc.4'];
helpers = helpers || Ember.Handlebars.helpers; data = data || {};
  


  data.buffer.push("	  <div class=\"find_form_block\">\n		<p>Where and when do you need your sitter?</p>\n		<form method=\"post\" action=\"#\">\n		  <ul class=\"clear\">\n			<li>\n			  <label for=\"where\">Where</label>\n			  <input id=\"where\" type=\"text\" value=\"Enter town or zipcode\" />\n			</li>\n			<li>\n			  <label for=\"when\">When</label>\n			  <input type=\"text\" id=\"datepicker\" />\n			  <p><input type=\"checkbox\" id=\"check\" name=\"check\" /><label for=\"check\">Overnight / Multiday booking?</label></p>\n			</li>\n			<li>\n			  <label for=\"from\">From</label>\n			  <select id=\"from\" data-placeholder=\"\" tabindex=\"8\"><option>6:00 PM</option><option>7:00 PM</option></select>\n			</li>\n			<li>\n			  <label for=\"to\">To</label>\n			  <select id=\"to\" data-placeholder=\"\" tabindex=\"9\"><option>11:00 PM</option><option>12:00 PM</option></select>\n			</li>\n			<li>\n			  <label>&nbsp;</label>\n			  <select data-placeholder=\"\" tabindex=\"10\"><option>2 Kids</option><option>3 Kids</option></select>\n			</li>\n			<li><input type=\"submit\" value=\"FIND MY SITTER\" /></li>\n		  </ul>\n		</form>\n		<p class=\"hide\"><a href=\"#\">Hide Search Bar</a></p>\n		<p class=\"show\"><a href=\"#\">Show Search Bar</a></p>\n	  </div>\n");
  
});
Ember.TEMPLATES["topNote"] = Ember.Handlebars.template(function anonymous(Handlebars,depth0,helpers,partials,data) {
this.compilerInfo = [3,'>= 1.0.0-rc.4'];
helpers = helpers || Ember.Handlebars.helpers; data = data || {};
  


  data.buffer.push("	  Hi Alex, you have 6 free months\n	  <div>\n		<p>Invite more frıends</p>\n		<span>&nbsp;</span>\n	  </div>\n");
  
});
Ember.TEMPLATES["done"] = Ember.Handlebars.template(function anonymous(Handlebars,depth0,helpers,partials,data) {
this.compilerInfo = [3,'>= 1.0.0-rc.4'];
helpers = helpers || Ember.Handlebars.helpers; data = data || {};
  var buffer = '';


  return buffer;
  
});
Ember.TEMPLATES["book"] = Ember.Handlebars.template(function anonymous(Handlebars,depth0,helpers,partials,data) {
this.compilerInfo = [3,'>= 1.0.0-rc.4'];
helpers = helpers || Ember.Handlebars.helpers; data = data || {};
  var buffer = '';


  return buffer;
  
});
Ember.TEMPLATES["parentEdit/profile"] = Ember.Handlebars.template(function anonymous(Handlebars,depth0,helpers,partials,data) {
this.compilerInfo = [3,'>= 1.0.0-rc.4'];
helpers = helpers || Ember.Handlebars.helpers; data = data || {};
  var buffer = '';


  return buffer;
  
});
Ember.TEMPLATES["parent"] = Ember.Handlebars.template(function anonymous(Handlebars,depth0,helpers,partials,data) {
this.compilerInfo = [3,'>= 1.0.0-rc.4'];
helpers = helpers || Ember.Handlebars.helpers; data = data || {};
  var buffer = '', hashTypes, hashContexts, escapeExpression=this.escapeExpression;


  data.buffer.push("username: ");
  hashTypes = {};
  hashContexts = {};
  data.buffer.push(escapeExpression(helpers._triageMustache.call(depth0, "username", {hash:{},contexts:[depth0],types:["ID"],hashContexts:hashContexts,hashTypes:hashTypes,data:data})));
  data.buffer.push("\nlast login ");
  hashTypes = {};
  hashContexts = {};
  data.buffer.push(escapeExpression(helpers._triageMustache.call(depth0, "last_login", {hash:{},contexts:[depth0],types:["ID"],hashContexts:hashContexts,hashTypes:hashTypes,data:data})));
  data.buffer.push("\nparking area: ");
  hashTypes = {};
  hashContexts = {};
  data.buffer.push(escapeExpression(helpers._triageMustache.call(depth0, "parking_area", {hash:{},contexts:[depth0],types:["ID"],hashContexts:hashContexts,hashTypes:hashTypes,data:data})));
  data.buffer.push("\nparking for sitter: ");
  hashTypes = {};
  hashContexts = {};
  data.buffer.push(escapeExpression(helpers._triageMustache.call(depth0, "parking_for_sitter", {hash:{},contexts:[depth0],types:["ID"],hashContexts:hashContexts,hashTypes:hashTypes,data:data})));
  data.buffer.push("\n");
  return buffer;
  
});
Ember.TEMPLATES["parentEdit/network"] = Ember.Handlebars.template(function anonymous(Handlebars,depth0,helpers,partials,data) {
this.compilerInfo = [3,'>= 1.0.0-rc.4'];
helpers = helpers || Ember.Handlebars.helpers; data = data || {};
  var buffer = '';


  return buffer;
  
});
Ember.TEMPLATES["parentEdit/index"] = Ember.Handlebars.template(function anonymous(Handlebars,depth0,helpers,partials,data) {
this.compilerInfo = [3,'>= 1.0.0-rc.4'];
helpers = helpers || Ember.Handlebars.helpers; data = data || {};
  


  data.buffer.push("edit index");
  
});
Ember.TEMPLATES["parentEdit/bookings"] = Ember.Handlebars.template(function anonymous(Handlebars,depth0,helpers,partials,data) {
this.compilerInfo = [3,'>= 1.0.0-rc.4'];
helpers = helpers || Ember.Handlebars.helpers; data = data || {};
  var buffer = '';


  return buffer;
  
});
Ember.TEMPLATES["parentEdit/reviews"] = Ember.Handlebars.template(function anonymous(Handlebars,depth0,helpers,partials,data) {
this.compilerInfo = [3,'>= 1.0.0-rc.4'];
helpers = helpers || Ember.Handlebars.helpers; data = data || {};
  var buffer = '';


  return buffer;
  
});
Ember.TEMPLATES["parentEdit/sitterTeam"] = Ember.Handlebars.template(function anonymous(Handlebars,depth0,helpers,partials,data) {
this.compilerInfo = [3,'>= 1.0.0-rc.4'];
helpers = helpers || Ember.Handlebars.helpers; data = data || {};
  var buffer = '';


  return buffer;
  
});
})