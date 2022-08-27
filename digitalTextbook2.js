// 主な参考↓
// https://www.koikikukan.com/archives/2012/01/17-015555.php

var penFlag = 0;
$(function() {
	// 変数の定義と初期化
    var offset = 5;
    var startX;
    var startY;
    var flag = false;
	

	console.log(penFlag);


	//canvasの背景を教科書画像に。(http://urusulambda.com/2018/07/29/canvas%E3%82%BF%E3%82%B0%E3%81%AE%E8%83%8C%E6%99%AF%E7%94%BB%E5%83%8F%E3%82%84%E8%83%8C%E6%99%AF%E8%89%B2%E3%82%92%E5%A4%89%E6%9B%B4%E3%81%99%E3%82%8Bfabric-js-javascript/)
	const canvas = document.querySelector('#draw-area1');
	const canvas2 = document.querySelector('#draw-area2');

	// 2D描画コンテキストを取得
    // var canvas = $('canvas').get(0);
    if (canvas.getContext) {
        var context = canvas.getContext('2d');
		var context2 = canvas2.getContext('2d');
    }

	// contextを使ってcanvasに絵を書いていく
	// const context = canvas.getContext('2d', {alpha:false});
	// const context2 = canvas2.getContext('2d', {alpha:false});

	var drawArea1 = document.getElementById("#draw-area1");
	var drawArea2 = document.getElementById("#draw-area2");
	
	console.log("あいうえお");
	
	// var ctx = canvas.getContext("2d");
	// var ctx2 = canvas2.getContext("2d");

	var background = new Image();
	var background2 = new Image();
	background.src = "Textbook_page1.png";
	background2.src = "Textbook_page2.png";

	//画像をCanvasのサイズに合わせて等倍して画像をcanvasに貼り付ける.
	var canvas_width = 900;
	var canvas_height = 600;
	background.onload = function(){
		//canvas_widthを height / width倍する.
		context.drawImage(background,0,0,canvas_width, background.height * canvas_width / background.width);
		context2.drawImage(background2,0,0,canvas_width, background2.height * canvas_width / background2.width);
		// ctx.drawImage(background,0,0,w, h * w / w);
		// ctx2.drawImage(background2,0,0,w2, h2 * w2 / w2);
	}


	// // 2D描画コンテキストを取得
    // var canvas = $('canvas').get(0);
    // if (canvas.getContext) {
    //     var context = canvas.getContext('2d');
	// 	var context2 = canvas.getContext('2d');
    // }


	// モード切り替え
	$('#pen-mode').click(function(e) {
		penFlag = 1;
		console.log(penFlag);
		
		console.log("かきくけこ");

		// クリック時
		// penFlagが1ならペンモードに、penFlagが0なら描かれない
		$('canvas').mousedown(function(e) {
			// console.log(penFlag);
			if(penFlag===0){
				flag = false;

			} else {
				flag = true;
				startX = e.pageX - $(this).offset().left - offset;
				startY = e.pageY - $(this).offset().top - offset;
				return false; // for chrome
			}
			
		});

		// ドラッグ操作時
		$('canvas').mousemove(function(e) {
			if (flag) {
				var endX = e.pageX - $('canvas').offset().left - offset;
				var endY = e.pageY - $('canvas').offset().top - offset;
				context.lineWidth = 2;
				context.beginPath();
				context.moveTo(startX, startY);
				context.lineTo(endX, endY);
				context.stroke();
				context.closePath();
				startX = endX;
				startY = endY;
			}
		});

		// クリックをやめたとき
		$('canvas').on('mouseup', function() {
			flag = false;
		});

		// マウスがcanvas外に出たとき
		$('canvas').on('mouseleave', function() {
			flag = false;
		});


		// ページめくりボタンが押されたとき
		$('#turn-mode').click(function(e) {
		penFlag = 0;
		// context.beginPath();
		console.log(penFlag);
		});
	});


	
	
	// if(penFlag === 1){

	// }

	// 色変えるボタンがリストになってるから、li要素が押されたとき、その背景色をペン色に設定する
    // $('li').click(function() {
    //     context.strokeStyle = $(this).css('background-color');
    // });
 
	// canvasをクリア
    $('#clear').click(function(e) {
        e.preventDefault();

		// ここのcontextのところが現在表示されてるcanvasになるようにしたい。
        context.clearRect(0, 0, $('canvas').width(), $('canvas').height());
		//canvasの背景が画像になるように再設定
		background.onload();
    });
 
	// canvasの描画を画像として保存
    $('#save').click(function() {
        var d = canvas.toDataURL('image/png');
        d = d.replace('image/png', 'image/octet-stream');
        window.open(d, 'save');
    });
});




	// イベント処理を初期化する
	// initEventHandler();

	// document.open();
    //      /*jquery*/
    //      (function(){
    //         $.fn.dragScroll = function(){
    //            let target = this;
    //            $(this).mousedown(function (event){
    //               $(this)
    //               .data('down', true)
    //               .data('x', event.clientX)
    //               .data('y', event.clientY)
    //               .data('scrollLeft', this.scrollLeft)
    //               .data('scrollTop', this.scrollTop);
    //               return false;
    //            }).css({
    //               'overflow': 'hidden', // 現在スクロールバー非表示。表示の場合'scroll'を設定して下さい
    //               'cursor': 'auto'
    //            });
    //            // ウィンドウから外れてもイベント実行
    //            $(document).mousemove(function (event){
    //               if ($(target).data('down') == true){
    //               // スクロール
    //               target.scrollLeft($(target).data('scrollLeft') + $(target).data('x') - event.clientX);
    //               target.scrollTop($(target).data('scrollTop') + $(target).data('y') - event.clientY);
    //               return false; // 文字列選択を抑止
    //               }
    //            }).mouseup(function (event){
    //               $(target).data('down', false);
    //            });
    //            return this;
    //         }
    //      })(jQuery);
    //      $(document).ready(function () {$('.slide-wrap').dragScroll();});//Your Settings ID or Class
    //      document.close();
	// 	 // イベント処理を初期化する
	// 	//initEventHandler();





