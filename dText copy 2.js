var flag = 1;

/* スライダー関係 */
// const swiper = new Swiper('.swiper', {
// 	// allowTouchMove: true,

// 	// If we need pagination
// 	pagination: {
// 		el: '.swiper-pagination',
// 	},

// 	// Navigation arrows
// 	navigation: {
// 		nextEl: '.swiper-button-next',
// 		prevEl: '.swiper-button-prev',
// 	},

// 	// // And if we need scrollbar
// 	// scrollbar: {
// 	//   el: '.swiper-scrollbar',
// 	// },
// });



document.addEventListener('DOMContentLoaded', function() {

	// /* スライダー関係 */
	// const swiper = new Swiper('.swiper', {
	// 	allowTouchMove: false,	// デフォルトがページめくりならtrue, ペンならfalse

	// 	// If we need pagination
	// 	pagination: {
	// 		el: '.swiper-pagination',
	// 	},

	// 	// Navigation arrows
	// 	navigation: {
	// 		nextEl: '.swiper-button-next',
	// 		prevEl: '.swiper-button-prev',
	// 	},

	// 	// // And if we need scrollbar
	// 	// scrollbar: {
	// 	//   el: '.swiper-scrollbar',
	// 	// },
	// });


	// /* canvas関係 */
	// const canvas = document.getElementById("myCanvas");
	// // const canvas = document.getElementsByClassName("swiper-slide");
	// const context = canvas.getContext("2d");
	// // console.log("canvas="+canvas);
	// // console.log("context="+context);


	// context.rect(0, 0, canvas.width, canvas.height);
	// context.fillStyle = "#fff";	// 白
	// context.fill();


	normal_event();	

	
})



function normal_event() {
	console.log("normal_event flag="+flag);

	if(flag === 1) {	// 書込モード flag=1
		console.log("mode= canvas");

		// swiper.allowTouchMove = false;  // falseに書き換え
		/* スライダー関係 */
		const swiper = new Swiper('.swiper', {
			allowTouchMove: false,

			// If we need pagination
			pagination: {
				el: '.swiper-pagination',
			},

			// Navigation arrows
			navigation: {
				nextEl: '.swiper-button-next',
				prevEl: '.swiper-button-prev',
			},

			// // And if we need scrollbar
			// scrollbar: {
			//   el: '.swiper-scrollbar',
			// },
		});
		console.log("swiper= "+swiper.allowTouchMove);



		/* canvas関係 */
		const canvas = document.getElementById("myCanvas");
		const canvas2 = document.getElementById("myCanvas2");
		// const canvas = document.getElementsByClassName("swiper-slide");
		const context = canvas.getContext("2d");
		const context2 = canvas.getContext("2d");
		console.log("canvas="+canvas);
		console.log("context="+context);


		context.rect(0, 0, canvas.width, canvas.height);
		context2.rect(0, 0, canvas2.width, canvas2.height);
		// context.fillStyle = "#fff";	// 白
		// context.fill();

		// 描画線の設定
		context.lineCap = 'round'; // 丸みを帯びた線にする
		context.lineJoin = 'round'; // 丸みを帯びた線にする
		context.lineWidth = 5;
		context.strokeStyle = "#black";

		context2.lineCap = 'round'; // 丸みを帯びた線にする
		context2.lineJoin = 'round'; // 丸みを帯びた線にする
		context2.lineWidth = 5;
		context2.strokeStyle = "#black";


		let mouse = {x: 0, y: 0};

		/* canvas用（1枚目用） */
		canvas.addEventListener("mousemove", function(e) {
			if(flag===1) {
				mouse.x = e.pageX - this.offsetLeft;
				mouse.y = e.pageY - this.offsetTop;
			}
			
		}, false);

		canvas.addEventListener("mousedown", function(e) {
			console.log("マウスダウン中");
			if(flag===1) {
				// swiper.allowTouchMove = false;
				console.log("ペンモードだよ！！");
				context.beginPath();
				context.moveTo(mouse.x, mouse.y);
			
				canvas.addEventListener("mousemove", onPaint, false);
			} else {
				swiper.allowTouchMove = true;
				console.log("ページめくりモードだよ！！！")
			}
		}, false);

		canvas.addEventListener("mouseup", function() {
			if(flag===1) {
				canvas.removeEventListener("mousemove", onPaint, false);
			}

			swiper.allowTouchMove = false;
		})

		const onPaint = function() {
			context.lineTo(mouse.x, mouse.y);
			context.stroke();
		}




		/* canvas2用（2枚目用） */
		canvas2.addEventListener("mousemove", function(e) {
			if(flag===1) {
				mouse.x = e.pageX - this.offsetLeft;
				mouse.y = e.pageY - this.offsetTop;
			}
			
		}, false);

		canvas2.addEventListener("mousedown", function(e) {
			console.log("マウスダウン中");
			if(flag===1) {
				// swiper.allowTouchMove = false;
				console.log("ペンモードだよ！！");
				context2.beginPath();
				context2.moveTo(mouse.x, mouse.y);
			
				canvas2.addEventListener("mousemove", onPaint2, false);
			} else {
				swiper.allowTouchMove = true;
				console.log("ページめくりモードだよ！！！")
			}
		}, false);

		canvas2.addEventListener("mouseup", function() {
			if(flag===1) {
				canvas2.removeEventListener("mousemove", onPaint2, false);
			}

			swiper.allowTouchMove = false;
		})

		const onPaint2 = function() {
			context2.lineTo(mouse.x, mouse.y);
			context2.stroke();
		}
		


		// /* スライダー関係 */
		// const swiper = new Swiper('.swiper', {
		// 	allowTouchMove: false,
	  
		// 	// If we need pagination
		// 	pagination: {
		// 		el: '.swiper-pagination',
		// 	},
		
		// 	// Navigation arrows
		// 	navigation: {
		// 		nextEl: '.swiper-button-next',
		// 		prevEl: '.swiper-button-prev',
		// 	},
		
		// 	// // And if we need scrollbar
		// 	// scrollbar: {
		// 	//   el: '.swiper-scrollbar',
		// 	// },
		// });


	} else {	// ページめくりモード flag=0
		console.log("mode= slider");
		
		// swiper.allowTouchMove = true;  // trueに書き換え
		/* スライダー関係 */
		const swiper = new Swiper('.swiper', {
			allowTouchMove: false,

			// If we need pagination
			pagination: {
				el: '.swiper-pagination',
			},

			// Navigation arrows
			navigation: {
				nextEl: '.swiper-button-next',
				prevEl: '.swiper-button-prev',
			},

			// // And if we need scrollbar
			// scrollbar: {
			//   el: '.swiper-scrollbar',
			// },
		});

		console.log("swiper= "+swiper.allowTouchMove);

	
	}
}


// normal_event();

/* モード切り替えボタンを押したとき */
function btn_pen(){
	flag = 1;
	console.log("button clicked! flag="+flag);
	normal_event();
}
function btn_page(){
	flag = 0;
	console.log("button clicked2 flag="+flag);
	normal_event();
}