var flag = 0;

/* スライダー関係 */
const swiper = new Swiper('.swiper', {
	// allowTouchMove: true,

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



document.addEventListener('DOMContentLoaded', function() {
	/* canvas関係 */
	const canvas = document.getElementById("myCanvas");
	// const canvas = document.getElementsByClassName("swiper-slide");
	const context = canvas.getContext("2d");
	// console.log("canvas="+canvas);
	// console.log("context="+context);


	context.rect(0, 0, canvas.width, canvas.height);
	context.fillStyle = "#fff";	// 白
	context.fill();


	normal_event();	
})



function normal_event() {
	console.log("normal_event flag="+flag);

	if(flag === 1) {
		console.log("mode= canvas");

		swiper.allowTouchMove = 'false';  // falseに書き換え

		/* canvas関係 */
		const canvas = document.getElementById("myCanvas");
		// const canvas = document.getElementsByClassName("swiper-slide");
		const context = canvas.getContext("2d");
		// console.log("canvas="+canvas);
		// console.log("context="+context);


		context.rect(0, 0, canvas.width, canvas.height);
		// context.fillStyle = "#fff";	// 白
		// context.fill();

		// 描画線の設定
		context.lineCap = 'round'; // 丸みを帯びた線にする
		context.lineJoin = 'round'; // 丸みを帯びた線にする
		context.lineWidth = 5;
		context.strokeStyle = "#black";

		let mouse = {x: 0, y: 0};

		canvas.addEventListener("mousemove", function(e) {
			mouse.x = e.pageX - this.offsetLeft;
			mouse.y = e.pageY - this.offsetTop;
		}, false);

		canvas.addEventListener("mousedown", function(e) {
			console.log("mousedown=YES");
			context.beginPath();
			context.moveTo(mouse.x, mouse.y);
		
			canvas.addEventListener("mousemove", onPaint, false);
		}, false);

		canvas.addEventListener("mouseup", function() {
			canvas.removeEventListener("mousemove", onPaint, false);
		})

		const onPaint = function() {
			context.lineTo(mouse.x, mouse.y);
			context.stroke();
		}



		


		/* スライダー関係 */
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


	} else {	// 0
		console.log("mode= slider");
		swiper.allowTouchMove = 'true';  // trueに書き換え
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