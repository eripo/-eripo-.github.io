

// ページの読み込みが完了したらコールバック関数が呼ばれる
// ※コールバック: 第2引数の無名関数(=関数名が省略された関数)
window.addEventListener('load', () => {
	flag = 0;	//flag=1のときペン、flag=0のときページめくり
	
		// var w = $('.wrapper').width();
		// var h = $('.wrapper').height();
		// $('#draw-area1').attr('width', w);
		// $('#draw-area1').attr('height', h);

		// var w2 = $('.wrapper').width();
		// var h2 = $('.wrapper').height();
		// $('#draw-area2').attr('width', w2);
		// $('#draw-area2').attr('height', h2);


		//canvasの背景を教科書画像に。(http://urusulambda.com/2018/07/29/canvas%E3%82%BF%E3%82%B0%E3%81%AE%E8%83%8C%E6%99%AF%E7%94%BB%E5%83%8F%E3%82%84%E8%83%8C%E6%99%AF%E8%89%B2%E3%82%92%E5%A4%89%E6%9B%B4%E3%81%99%E3%82%8Bfabric-js-javascript/)
		const canvas1 = document.querySelector('#draw-area1');
		const canvas2 = document.querySelector('#draw-area2');
		// contextを使ってcanvasに絵を書いていく
		const context = canvas1.getContext('2d', {alpha:false});
		const context2 = canvas2.getContext('2d', {alpha:false});

		var drawArea1 = document.getElementById("#draw-area1");
		var drawArea2 = document.getElementById("#draw-area2");
		
		console.log("あいうえお");
		
		var ctx = canvas1.getContext("2d");
		var ctx2 = canvas2.getContext("2d");

		var background = new Image();
		var background2 = new Image();
		background.src = "Textbook_page1.png";
		background2.src = "Textbook_page2.png";

		//画像をCanvasのサイズに合わせて等倍して画像をcanvasに貼り付ける.
		var canvas_width = 900;
		var canvas_height = 600;
		background.onload = function(){
			//canvas_widthを height / width倍する.
			ctx.drawImage(background,0,0,canvas_width, background.height * canvas_width / background.width);
			ctx2.drawImage(background2,0,0,canvas_width, background2.height * canvas_width / background2.width);
			// ctx.drawImage(background,0,0,w, h * w / w);
			// ctx2.drawImage(background2,0,0,w2, h2 * w2 / w2);
		}

	if(flag === 1) {	

		// 直前のマウスのcanvas上のx座標とy座標を記録する
		const lastPosition = { x: null, y: null };
	
		// マウスがドラッグされているか(クリックされたままか)判断するためのフラグ
		let isDrag = false;
	
		// 絵を書く
		function draw(x, y) {
			// マウスがドラッグされていなかったら処理を中断する。
			// ドラッグしながらしか絵を書くことが出来ない。
			if(!isDrag) {
				return;
			}
	
		// 「context.beginPath()」と「context.closePath()」を都度draw関数内で実行するよりも、
		// 線の描き始め(dragStart関数)と線の描き終わり(dragEnd)で1回ずつ読んだほうがより綺麗に線画書ける
	
		// 線の状態を定義する
		// MDN CanvasRenderingContext2D: https://developer.mozilla.org/en-US/docs/Web/API/CanvasRenderingContext2D/lineJoin
		context.lineCap = 'round'; // 丸みを帯びた線にする
		context.lineJoin = 'round'; // 丸みを帯びた線にする
		context.lineWidth = 5; // 線の太さ
		context.strokeStyle = 'black'; // 線の色
	

		// 書き始めは lastPosition.x, lastPosition.y の値はnullとなっているため、
		// クリックしたところを開始点としている。
		// この関数(draw関数内)の最後の2行で lastPosition.xとlastPosition.yに
		// 現在のx, y座標を記録することで、次にマウスを動かした時に、
		// 前回の位置から現在のマウスの位置まで線を引くようになる。
		if (lastPosition.x === null || lastPosition.y === null) {
			// ドラッグ開始時の線の開始位置
			context.moveTo(x, y);
		} else {
			// ドラッグ中の線の開始位置
			context.moveTo(lastPosition.x, lastPosition.y);
		}
		// context.moveToで設定した位置から、context.lineToで設定した位置までの線を引く。
		// - 開始時はmoveToとlineToの値が同じであるためただの点となる。
		// - ドラッグ中はlastPosition変数で前回のマウス位置を記録しているため、
		//   前回の位置から現在の位置までの線(点のつながり)となる
		context.lineTo(x, y);
	
		// context.moveTo, context.lineToの値を元に実際に線を引く
		context.stroke();
	
		// 現在のマウス位置を記録して、次回線を書くときの開始点に使う
		lastPosition.x = x;
		lastPosition.y = y;
		}
	
		// canvas上に書いた絵を全部消す
		function clear() {
			//canvasが黒い四角で塗りつぶされる
			context.clearRect(0, 0, canvas1.width, canvas1.height);
			//canvasの背景が画像になるように再設定
			background.onload();	
		}
	
		// マウスのドラッグを開始したらisDragのフラグをtrueにしてdraw関数内で
		// お絵かき処理が途中で止まらないようにする
		function dragStart(event) {
		// これから新しい線を書き始めることを宣言する
		// 一連の線を書く処理が終了したらdragEnd関数内のclosePathで終了を宣言する
		context.beginPath();
	
		isDrag = true;
		}

		// マウスのドラッグが終了したら、もしくはマウスがcanvas外に移動したら
		// isDragのフラグをfalseにしてdraw関数内でお絵かき処理が中断されるようにする
		function dragEnd(event) {
		// 線を書く処理の終了を宣言する
		context.closePath();
		isDrag = false;
	
		// 描画中に記録していた値をリセットする
		lastPosition.x = null;
		lastPosition.y = null;
		}
	
		// マウス操作やボタンクリック時のイベント処理を定義する
		function initEventHandler() {
		const clearButton = document.querySelector('#clear-button');
		clearButton.addEventListener('click', clear);
	
		canvas1.addEventListener('mousedown', dragStart);
		canvas1.addEventListener('mouseup', dragEnd);
		canvas1.addEventListener('mouseout', dragEnd);
		canvas1.addEventListener('mousemove', (event) => {
			// eventの中の値を見たい場合は以下のようにconsole.log(event)で、
			// デベロッパーツールのコンソールに出力させると良い
			// console.log(event);
	
			draw(event.layerX, event.layerY);
		});
		}

	// イベント処理を初期化する
	initEventHandler();



	} else if(flag === 0) {
		jQuery.prototype.mousedragscrollable = function () {
		let target;
		$(this).each(function (i, e) {
			$(e).mousedown(function (event) {
			event.preventDefault();
			target = $(e);
			$(e).data({
				down: true,
				move: false,
				x: event.clientX,
				y: event.clientY,
				scrollleft: $(e).scrollLeft(),
				scrolltop: $(e).scrollTop(),
			});
			return false;
			});
			$(e).click(function (event) {
			if ($(e).data("move")) {
				return false;
			}
			});
		});
		$(document)
			.mousemove(function (event) {
			if ($(target).data("down")) {
				event.preventDefault();
				let move_x = $(target).data("x") - event.clientX;
				let move_y = $(target).data("y") - event.clientY;
				if (move_x !== 0 || move_y !== 0) {
				$(target).data("move", true);
				} else {
				return;
				}
				$(target).scrollLeft($(target).data("scrollleft") + move_x);
				$(target).scrollTop($(target).data("scrolltop") + move_y);
				return false;
			}
			})
			.mouseup(function (event) {
			$(target).data("down", false);
			return false;
			});
		};
		
		$(".slide-wrap").mousedragscrollable();
		
		
		console.log("flag");

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
	}
	

});




