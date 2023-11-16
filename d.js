

$(document).ready(function() {
  const canvas = document.getElementById('canvas');
  const ctx = canvas.getContext('2d');

  const drawingCanvas = document.createElement('canvas');
  const drawingCtx = drawingCanvas.getContext('2d');

  // 要素の位置座標を取得
  var clientRect = canvas.getBoundingClientRect() ;

  // ページの左端から、canvasの左端までの距離
  var elemGapX = window.pageXOffset + clientRect.left ;

  // ページの上端から、canvasの上端までの距離
  var elemGapY = window.pageYOffset + clientRect.top ;

  // console.log('画面左上端の座標: (' + window.pageXOffset + ', ' + window.pageYOffset + ')');
  // console.log('canvas要素の左上端の座標: (' + clientRect.left + ', ' + clientRect.top + ')');


  let scale = 1; // 現在の拡大率

  // 筆圧，変位X，変位Y，変位，速度X，速度Y，速度，加速度X，加速度Y，加速度，座標X，座標Y，処理時間，モード
  var strMid = "";
  strMid += "pressure" + "," + "gapX" + "," + "gapY" + "," + "gap" + "," + "gapRX" + "," + "gapRY" + "," + "gapR" + "," + "velX" + "," + "velY" + "," + "vel" + "," + "velRX" + "," + "velRY" + "," + "velR" + "," + "accelerationX" + "," + "accelerationY" + "," + "acceleration" + "," + "accelerationRX" + "," + "accelerationRY" + "," + "accelerationR" + "," + "posX" + "," + "posY" + "," + "msec" + "," + "Mode" + "\n";

  // 筆圧，経過時間，変位X，変位Y，変位，速度X，速度Y，速度，加速度X，加速度Y，加速度，座標X，座標Y，処理時間，モード
  var strInitial = "";
  strInitial += "pressure0" + "," + "intervalTime" + "," + "gapX" + "," + "gapY" + "," + "gap" + "," + "gapRX" + "," + "gapRY" + "," + "gapR" + "," + "velX" + "," + "velY" + "," + "vel" + "," + "velRX" + "," + "velRY" + "," + "velR" + "," + "accelerationX" + "," + "accelerationY" + "," + "acceleration" + "," + "accelerationRX" + "," + "accelerationRY" + "," + "accelerationR" + "," + "posX" + "," + "posY" + "," + "msec" + "," + "Mode" + "\n";


  


  let count = 0;
  let isDrawing = false;
  var isDrag = false;

  let mode = "page";
  let startX0;
  let startY0;
  let startPosX;
  let startPosY;
  // let startX = 0;
  // let startY = 0;
  let startTime = 0;
  let endTime;
  let nowTime;
  let previousTime;
  // let currentX = 0;
  // let currentY = 0;

  $(canvas).on('mousedown touchstart', function(event) {
    console.log("マウスダウン")
    
    // 次回ドラッグ開始時（インターバル終了）
    endTime = performance.now();
    previousTime = endTime;
    nowTime = endTime;
    console.log("intervalTime：" + (endTime-startTime));
    // console.log("intervalTime：" + (endTime-startTime) + "\nstart：" + startTime + "\nend：" + endTime)
    // console.log("previousTime:\n" + previousTime);

    event.preventDefault();
    isDrag = true;

    // posX,posYは速度や加速度を求めるための座標．startX0やcurrentXなどelemGapを引いているものは，紙面上の座標を求めるためのもの．
    


    console.log("endTime：" + endTime + "\nstartTime：" + startTime + "\npreviousTime：" + previousTime + "\nnowTime：" + nowTime);
    


    //1個前の座標（50ミリ秒ごと） 
    positionPrevX = startX0;
    positionPrevY = startY0;
    posPrevX = startPosX;
    posPrevY = startPosY;


    // console.log("ドラッグ始点座標: (" + startX0 + ", " + startY0 + ")");
    // console.log("start: (" + startX + ", " + startY + ")");

    
    strInitial += pressure0 + "," + (endTime-startTime);
    // console.log("圧力："+ pressure);
    speedCount();
  });


  $(canvas).on('mousemove touchmove', function(event) {
    event.preventDefault();




  });

  $(canvas).on('mouseup touchend', function(event) {
    // 前回ドラッグ終了時（インターバル開始）
    startTime = performance.now();

    // ドラッグ時間を出力
    strInitial += "," + mode + "\n";
    

    event.preventDefault();
    isDrag = false;


    isDrawing = false;

    PositionX.push(currentX);
    PositionY.push(currentY);
    PositionRX.push(curPosX);
    PositionRY.push(curPosY);
    
    // console.log(currentX + "\n" + currentY);
    // console.log("end-start: " + (currentX-startX0));
    if(mode==="page") {
      if (currentX - startX0 < -1) {
        nextPage();
      } else if (currentX - startX0 > 1) {
        prevPage();
      }
    }

    count = 0;
  });



  function speedCount() {
    // 速度を計算する処理を記述
    // if (vel == false) { // pointに値が入ってなかったら、速さ(0,0)
    //   gapX = 0;
    //   gapY = 0;
    // } else {
    //   if (dpoint0 == false) {
    //     dpoint0 = point;
    //   }
    if(!isDrag) {
      return;
    }

    if(count != 0){
      gapX = currentX - positionPrevX;
      gapY = currentY - positionPrevY;
      gap = Math.sqrt(gapX**2 + gapY**2);
      // console.log("gapX,gapY: " + gapX + ", " + gapY + ",\n" + currentX + "," + positionPrevX + ",\n" + currentY + "," + positionPrevY);

      gapRX = (curPosX - posPrevX);
      gapRY = (curPosY - posPrevY);
      gapR = Math.sqrt(gapRX**2 + gapRY**2);
      // console.log("gapRX,gapRY: " + gapRX + ", " + gapRY + ",\n" + curPosX + "," + posPrevX + ",\n" + curPosY + "," + posPrevY);


      nowTime = performance.now();
      msec = nowTime - previousTime;
      console.log("previousTime：" + previousTime + "\nnowTime：" + nowTime);

      previousTime = nowTime;
      console.log("msec: " + msec);
      // console.log("endTime：" + endTime + "\nstartTime：" + startTime + "\npreviousTime：" + previousTime + "\nnowTime：" + nowTime);
      

      // console.log("print\n" + msec + "," + pressure + "," + gapX + ", " + gapY + "," + currentX + ", " + positionPrevX + "," + currentY + ", " + positionPrevY);
      if(count > 1) {
        strMid += pressure + "," + gapX + "," + gapY + "," + gap + "," + gapRX + "," + gapRY + "," + gapR + "," + velX + "," + velY + "," + vel + "," + velRX + "," + velRY + "," + velR + "," + accelerationX + "," + accelerationY + "," + acceleration + "," + accelerationRX + "," + accelerationRY + "," + accelerationR + "," + currentX + "," + currentY + "," + msec + "," + mode +"\n";

      }
      if(count === 1) {
        strInitial += "," + gapX + "," + gapY + "," + gap + "," + gapRX + "," + gapRY + "," + gapR + "," + velX + "," + velY + "," + vel + "," + velRX + "," + velRY + "," + velR + "," + accelerationX + "," + accelerationY + "," + acceleration + "," + accelerationRX + "," + accelerationRY + "," + accelerationR + "," + currentX + "," + currentY + "," + (nowTime-endTime);
        // str += gapX + "," + gapY + "," + gap + "," + velX + "," + velY + "," + vel + "," + accelerationX + "," + accelerationY + "," + acceleration + "," + currentX + "," + currentY + "," + msec + "," + mode +"\n";
        strMid += pressure0 + "," + gapX + "," + gapY + "," + gap + "," + gapRX + "," + gapRY + "," + gapR + "," + velX + "," + velY + "," + vel + "," + velRX + "," + velRY + "," + velR + "," + accelerationX + "," + accelerationY + "," + acceleration + "," + accelerationRX + "," + accelerationRY + "," + accelerationR + "," + currentX + "," + currentY + "," + (nowTime-endTime) + "," + mode +"\n";
        // str += gapX + "," + gapY + "," + gap + "," + (gapX - preGapX) + "," + (gapY - preGapY) + "," + (gap - preGap) + "," + currentX + "," + currentY + "," + (nowTime-endTime) + "," + mode +"\n";

        console.log("現： " + (nowTime-endTime));


        // stroke.push(currentX, currentY, velX, velY, vel, accelerationX, accelerationY, acceleration, pressure)
      }

    }
    
    
    
    count++;


    // var start = Date.now();
    // var now = performance.now();
    // console.log("時間1：" + start);
    // console.log("時間2：" + now);
  

    // 10ミリ秒後に再度関数を実行
    setTimeout(speedCount, 10);

  }
  



});
