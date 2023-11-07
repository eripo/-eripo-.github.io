$(document).ready(function() {
  const canvas = document.getElementById('canvas');
  const ctx = canvas.getContext('2d');

  const drawingCanvas = document.createElement('canvas');
  const drawingCtx = drawingCanvas.getContext('2d');

  // 要素の位置座標を取得
  var clientRect = canvas.getBoundingClientRect() ;
  console.log(clientRect);

  // ページの左端から、canvasの左端までの距離
  var elemGapX = clientRect.left ;
  console.log(elemGapX);

  // ページの上端から、canvasの上端までの距離
  var elemGapY = clientRect.top ;



  let count = 0;
  let startX0;
  let startY0;
  let startPosX;
  let startPosY;

  let subPrevX;
  let subPrevY;
  let subPrevPosX;
  let subPrevPosY;
  let previousX;
  let previousY;
  let prePosX;
  let prePosY;
  let currentX;
  let currentY;
  let curPosX;
  let curPosY;



$(canvas).on('mousedown touchstart', function(event) {
  event.preventDefault();
  isDrag = true;

  // posX,posYは速度や加速度を求めるための座標．startX0やcurrentXなどelemGapを引いているものは，紙面上の座標を求めるためのもの．
  
  if (event.type === 'mousedown') {
    startX0 = event.clientX - elemGapX;
    startY0 = event.clientY - elemGapY;
    startPosX = event.clientX;
    startPosY = event.clientY;
    
  } else if (event.type === 'touchstart') {
    const touch = event.touches[0];
    startX0 = touch.clientX - elemGapX;
    startY0 = touch.clientY - elemGapY;
    startPosX = touch.clientX;
    startPosY = touch.clientY;
    // console.log(startX0);
    // console.log(startPosX);
    // console.log(touch.offsetX);
  }

  


  
  isDrawing = true;
  // 紙面上
  gapX = startX0;
  gapY = startY0;
  subPrevX = startX0;
  subPrevY = startY0;
  previousX = startX0;
  previousY = startY0;
  currentX = startX0;
  currentY = startY0;

  // リアル
  gapRX = startPosX;
  gapRY = startPosY;    
  subPrevPosX = startPosX;
  subPrevPosY = startPosY;
  prePosX = startPosX;
  prePosY = startPosY;
  curPosX = startPosX;
  curPosY = startPosY;

  //1個前の座標（50ミリ秒ごと） 
  positionPrevX = startX0;
  positionPrevY = startY0;
  posPrevX = startPosX;
  posPrevY = startPosY;


  speedCount();
});


$(canvas).on('mousemove touchmove', function(event) {
  event.preventDefault();

  if (event.type === 'mousemove') {
    currentX = event.clientX - elemGapX;
    currentY = event.clientY - elemGapY;
    curPosX = event.screenX;
    curPosY = event.screenY;
  } else if (event.type === 'touchmove') {
    const touch = event.touches[0];
    currentX = touch.clientX - elemGapX;
    currentY = touch.clientY - elemGapY;
    curPosX = touch.screenX;
    curPosY = touch.screenY;

  }



  previousX = subPrevX;
  previousY = subPrevY;
  currentX = currentX;
  currentY = currentY;

  // scaleは使ってないのでここでもとりあえずなしで．
  prePosX = subPrevPosX;
  prePosY = subPrevPosY;


  subPrevX = currentX;
  subPrevY = currentY;

  subPrevPosX = curPosX;
  subPrevPosY = curPosY;


});

$(canvas).on('mouseup touchend', function(event) {

  

  event.preventDefault();
  isDrag = false;

  if (event.type === 'mouseup') {
    currentX = event.clientX - elemGapX;
    currentY = event.clientY - elemGapY;
    curPosX = event.screenX;
    curPosY = event.screenY;
  } else if (event.type === 'touchend') {
    const touch = event.changedTouches[0];
    currentX = touch.clientX - elemGapX;
    currentY = touch.clientY - elemGapY;
    curPosX = touch.screenX;
    curPosY = touch.screenY;
  }
  isDrawing = false;
  

  count = 0;
});



function speedCount() {
  if(!isDrag) {
    return;
  }

  if(count != 0){
    gapX = currentX - positionPrevX;
    gapY = currentY - positionPrevY;
    gap = Math.sqrt(gapX**2 + gapY**2);
    console.log("gapX,gapY: " + gapX + ", " + gapY + ",\n" + currentX + "," + positionPrevX + ",\n" + currentY + "," + positionPrevY);

    gapRX = (curPosX - posPrevX);
    gapRY = (curPosY - posPrevY);
    gapR = Math.sqrt(gapRX**2 + gapRY**2);
    console.log("gapRX,gapRY: " + gapRX + ", " + gapRY + ",\n" + curPosX + "," + posPrevX + ",\n" + curPosY + "," + posPrevY);
    

    positionPrevX = currentX;
    positionPrevY = currentY;
    posPrevX = curPosX;
    posPrevY = curPosY;

    preGapX = gapX;
    preGapY = gapY;
    preGap = gap;
    preGapRX = gapRX;
    preGapRY = gapRY;
    preGapR = gapR;

  }
  
  count++;

  // 10ミリ秒後に再度関数を実行
  setTimeout(speedCount, 10);

}

});