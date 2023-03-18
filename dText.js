// 2023年3月18日～

document.addEventListener('DOMContentLoaded', function() {


	const canvas = document.getElementById("myCanvas");
	const context = canvas.getContext("2d");

	context.rect(0, 0, canvas.width, canvas.height);
	context.fillStyle = "#fff";
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



});

