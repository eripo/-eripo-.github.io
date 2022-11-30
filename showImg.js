(function($) {
    $(window).on("load", function() {
        //imgのIDやクラスを指定
        var $img = $("#zoomImg").imgViewer2(
                {
                //画像の揺れの改善
                onReady: function() {
                    this.setZoom(2);
                    this.setZoom(1);
                }
            }
        );
    });
})(jQuery);