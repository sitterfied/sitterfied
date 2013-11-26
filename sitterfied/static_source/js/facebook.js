window.fbAsyncInit = function() {
    FB.init({
        appId      : '141907389308388', // App ID
        channelUrl : '/channel.html', // Channel File
        status     : true, // check login status
        cookie     : true, // enable cookies to allow the server to access the session
        xfbml      : true,  // parse XFBML
        frictionlessRequests : true
    });

};

// Load the SDK Asynchronously

(function(d){
    var js, id = 'facebook-jssdk', ref = d.getElementsByTagName('script')[0];
    if (d.getElementById(id)) {return;}
    js = d.createElement('script'); js.id = id; js.async = true;
    js.src = "//connect.facebook.net/en_US/all.js";
    ref.parentNode.insertBefore(js, ref);
}(document));


window.FBConnect = function() {
    // First time someone gets to the page we are going to check if they are connected - if they are we then load up their picture list
    FB.getLoginStatus(function(response) {
        if (response.status === 'connected') {
            var access_token = FB.getAccessToken();
        }
        else if (response.status === 'not_authorized')
            FB.login(function(){
                FBConnect();
            }, {scope: 'email'});
    });
}
