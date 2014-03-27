if (!(typeof $ === "undefined")) {
    $(function(){
        function detectIE() {
            var ua = window.navigator.userAgent;
            var msie = ua.indexOf('MSIE ');
            var trident = ua.indexOf('Trident/');
    
            if (msie > 0) {
                // IE 10 or older => return version number
                return parseInt(ua.substring(msie + 5, ua.indexOf('.', msie)), 10);
            }
    
            if (trident > 0) {
                // IE 11 (or newer) => return version number
                var rv = ua.indexOf('rv:');
                return parseInt(ua.substring(rv + 3, ua.indexOf('.', rv)), 10);
            }
    
            // other browser
            return false;
        }
        
        if (detectIE()) {
            var modalParent = "body";
            if ($("div#application").length) {
                modalParent = "div#application"
            }
            $.fancybox({
                href: "#ie_modal",
                maxWidth: 390,
                maxHeight: 257,
                minWidth: 390,
                minHeight: 257,
                fitToView: false,
                closeBtn: false,
                helpers: {
                    overlay: {
                        closeClick: false,
                    }
                },
                parent: modalParent
            });
        }
        
    });
}