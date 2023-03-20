var flag = 0;

document.addEventListener('DOMContentLoaded', function() {

	if(flag === 0) {
		/* canvas関係 */
		const canvas = document.getElementById("myCanvas");
		// const canvas = document.getElementsByClassName("swiper-slide");
		const context = canvas.getContext("2d");
		console.log("canvas="+canvas);
		console.log("context="+context);


		context.rect(0, 0, canvas.width, canvas.height);
		context.fillStyle = "#fff";	// 白
		context.fill();

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
	  
		// 	// If we need pagination
		// 	pagination: {
		// 	el: '.swiper-pagination',
		// 	},
		
		// 	// Navigation arrows
		// 	navigation: {
		// 	nextEl: '.swiper-button-next',
		// 	prevEl: '.swiper-button-prev',
		// 	},
		
		// 	// // And if we need scrollbar
		// 	// scrollbar: {
		// 	//   el: '.swiper-scrollbar',
		// 	// },
		// });
	}
	

	

	


	

	
})