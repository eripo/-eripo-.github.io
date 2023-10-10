/***********************  
 * 最終更新日：2023/09/09
 ***********************
 * ※変更不可
 ***********************
 * デジタル教科書
 * 
 ** 機能 **
 * 書き込み
 * ページめくり 
 * モード切替ボタンでモード変更。
 * 書き込みの座標ずれ無し。
 * データ取得機能
 * ・test0
 *    - 圧力，前回ドラッグからの経過時間(インターバルタイム)，前回座標との差，速度[px/ms]，加速度[px/ms2]，座標，前回サンプル点からの経過時間(データ取得間隔)，ドラッグ時間，モード
 * ・test
 *    - 前回座標との差，速度[px/ms]，加速度[px/ms2]，座標，前回サンプル点からの経過時間(データ取得間隔)，モード
 *********************** 
 * 
 * startX0: タッチスタート時の座標
 * startX: ドラッグ中の座標（その区間における始点）
 * previousX: 1個前の点の座標
 * currentX: ドラッグ中の現在の座標（その区間における終点）
 * startTime: インターバルタイム開始時（前回ドラッグ終了時）
 * endTime: インターバルタイム終了時（次回ドラッグ開始時）
 * gapX: 前回座標との差
 * velX: 速さ
 * subPrevX: 前回座標保存用
 * positionPrevX: 前回座標
 * preVelX: 前回速度
 * 
 * ページめくり幅（currentX-startX0）：30
 * 書き込みは、previousXからcurrentXの線分を描いていくことで書いている 
 ***********************
 * 問題点・未実装
 * ・拡大・縮小不可（ボタンのみ有）
************************/

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
  var str = "";
  str += "pressure" + "," + "gapX" + "," + "gapY" + "," + "gap" + "," + "v_x" + "," + "v_y" + "," + "v" + "," + "aX" + "," + "aY" + "," + "a" + "," + "pos_x" + "," + "pos_y" + "," + "msec" + "," + "Mode" + "\n";  // 速度X成分、速度Y成分、合成速度、筆圧

  var str0 = "";
  str0 += "pressure0" + "," + "intervalTime" + "," + "gapX" + "," + "gapY" + "," + "gap" + "," + "v_x" + "," + "v_y" + "," + "v" + "," + "aX" + "," + "aY" + "," + "a" + "," + "pos_x" + "," + "pos_y" + "," + "msec" + "," + "dragTime" + "," + "Mode" + "\n";  // 初速度X成分、初速度Y成分、合成初速度、初筆圧


  let count = 0;
  let isDrawing = false;
  var isDrag = false;

  let mode = "page";
  let startX0;
  let startY0;
  // let startX = 0;
  // let startY = 0;
  let startTime = 0;
  // let currentX = 0;
  // let currentY = 0;

  let subPrevX;
  let subPrevY;
  let previousX;
  let previousY;
  let currentX;
  let currentY;
  let pressure;
  let pressure0;

  // 一時的なキャンバスを作成
  const tempCanvas = document.createElement('canvas');
  const tempCtx = tempCanvas.getContext('2d');

  const backgroundImageUrl = '/img/Textbook_page1.png';
  const backgroundImage = new Image();
  backgroundImage.src = backgroundImageUrl;

  // 背景画像が読み込まれた後に描画を開始する
  backgroundImage.onload = function() {
    drawPage(currentPage);
  };


  $(canvas).on('mousedown touchstart', function(event) {
    // 次回ドラッグ開始時（インターバル終了）
    endTime = performance.now();
    previousTime = endTime;
    // console.log("intervalTime：" + (endTime-startTime) + "\nstart：" + startTime + "\nend：" + endTime)
    console.log("previousTime:\n" + previousTime);

    event.preventDefault();
    isDrag = true;

    if (event.type === 'mousedown') {
      startX0 = event.clientX - elemGapX;
      startY0 = event.clientY - elemGapY;
      // startX = event.clientX - elemGapX;
      // startY = event.clientY - elemGapY;
      pressure0 = 1;
    } else if (event.type === 'touchstart') {
      const touch = event.touches[0];
      startX0 = touch.clientX - elemGapX;
      startY0 = touch.clientY - elemGapY;
      // startX = touch.clientX - elemGapX;
      // startY = touch.clientY - elemGapY;
      pressure0 = touch.force;
      console.log("Press: " + pressure);
    }
    
    isDrawing = true;
    gapX = startX0;
    gapY = startY0;
    subPrevX = startX0;
    subPrevY = startY0;
    previousX = startX0;
    previousY = startY0;
    currentX = startX0;
    currentY = startY0;
    preVelX = 0;
    preVelY = 0;
    preVel = 0;
    accelerationX = 0;
    accelerationY = 0;
    acceleration = 0;

    //1個前の座標（50ミリ秒ごと） 
    positionPrevX = startX0;
    positionPrevY = startY0;

    console.log("ドラッグ始点座標: (" + startX0 + ", " + startY0 + ")");
    // console.log("start: (" + startX + ", " + startY + ")");

    
    str0 += pressure0 + "," + (endTime-startTime);
    // console.log("圧力："+ pressure);
    speedCount();
  });


  $(canvas).on('mousemove touchmove', function(event) {
    event.preventDefault();

    if (event.type === 'mousemove') {
      currentX = event.clientX - elemGapX;
      currentY = event.clientY - elemGapY;
    } else if (event.type === 'touchmove') {
      const touch = event.touches[0];
      currentX = touch.clientX - elemGapX;
      currentY = touch.clientY - elemGapY;
      pressure = touch.force;
    }


    const page = pages[currentPage - 1];

    previousX = subPrevX / scale;
    previousY = subPrevY / scale;
    currentX = (currentX / scale);
    currentY = (currentY / scale);

    // // ドラッグ始点の座標
    // console.log("各座標\nstart0\nX座標："+ startX0 +"\nY座標："+ startY0);
    // // 1個前の座標
    // console.log("previous\nX座標："+ previousX +"\nY座標："+ previousY);
    // // 現在の座標
    // console.log("current\nX座標："+ currentX +"\nY座標："+ currentY);


    if (isDrawing && mode==="pen") {
      page.drawings.push({ previousX, previousY, currentX, currentY });

      ctx.beginPath();
      ctx.moveTo(previousX, previousY);
      ctx.lineTo(currentX, currentY);
      // console.log("start: " + startX + ", " + startY);
      // console.log("gap: " + elemGapX + ", " + elemGapY);
      // console.log("previous: " + previousX + ", " + previousY);
      // console.log("current: " + currentX + ", " + currentY);
      ctx.stroke();

      
      // previousX = currentX;
      // previousY = currentY;
    }
    subPrevX = currentX;
    subPrevY = currentY;


  });

  $(canvas).on('mouseup touchend', function(event) {
    // 前回ドラッグ終了時（インターバル開始）
    startTime = performance.now();

    // ドラッグ時間を出力
    str0 += "," + (startTime - endTime) + "," + mode + "\n";
    

    event.preventDefault();
    isDrag = false;

    if (event.type === 'mouseup') {
      currentX = event.clientX - elemGapX;
      currentY = event.clientY - elemGapY;
    } else if (event.type === 'touchend') {
      const touch = event.changedTouches[0];
      currentX = touch.clientX - elemGapX;
      currentY = touch.clientY - elemGapY;
    }
    isDrawing = false;


    // console.log("end-start: " + (currentX-startX0));
    if(mode==="page") {
      if (currentX - startX0 < -30) {
        nextPage();
      } else if (currentX - startX0 > 30) {
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
      // console.log("gapX,gapY: " + gapX + ", " + gapY + "," + currentX + previousX);
      // 普通の速さ
      gap = Math.sqrt(gapX**2 + gapY**2);
      
      nowTime = performance.now();
      msec = nowTime - previousTime;

      previousTime = nowTime;
      // console.log("msec: " + msec);

      velX = gapX / msec;
      velY = gapY / msec;
      vel = gap / msec;

      accelerationX = (velX - preVelX) / msec;
      accelerationY = (velY - preVelY) / msec;
      acceleration = (vel - preVel) / msec;

      console.log("print\n" + gapX + ", " + gapY + "," + currentX + ", " + positionPrevX + "," + currentY + ", " + positionPrevY);
      if(count > 1) {
        str += pressure + "," + gapX + "," + gapY + "," + gap + "," + velX + "," + velY + "," + vel + "," + accelerationX + "," + accelerationY + "," + acceleration + "," + currentX + "," + currentY + "," + msec + "," + mode +"\n";
      }
      if(count === 1) {
        str0 += "," + gapX + "," + gapY + "," + gap + "," + velX + "," + velY + "," + vel + "," + accelerationX + "," + accelerationY + "," + acceleration + "," + currentX + "," + currentY + "," + (nowTime-endTime);
        // str += gapX + "," + gapY + "," + gap + "," + velX + "," + velY + "," + vel + "," + accelerationX + "," + accelerationY + "," + acceleration + "," + currentX + "," + currentY + "," + msec + "," + mode +"\n";
        str += pressure0 + "," + gapX + "," + gapY + "," + gap + "," + velX + "," + velY + "," + vel + "," + accelerationX + "," + accelerationY + "," + acceleration + "," + currentX + "," + currentY + "," + (nowTime-endTime) + "," + mode +"\n";
        // str += gapX + "," + gapY + "," + gap + "," + (gapX - preGapX) + "," + (gapY - preGapY) + "," + (gap - preGap) + "," + currentX + "," + currentY + "," + (nowTime-endTime) + "," + mode +"\n";
      }
      // dpoint0 = point;

      console.log("count-previous: " + positionPrevX + ", " + positionPrevY);

      // console.log("count:" + count + "\ngap：" + gapX + ", " + gapY);
      
      // console.log("count-previous: " + positionPrevX + ", " + positionPrevY);
      // console.log("count-current: " + currentX + ", " + currentY);
      console.log("acceleration: " + acceleration + ", " + accelerationX + ", " + accelerationY);

      positionPrevX = currentX;
      positionPrevY = currentY;

      preGapX = gapX;
      preGapY = gapY;
      preGap = gap;

      preVelX = velX;
      preVelY = velY;
      preVel = vel;

    }
    
    
    
    count++;


    // var start = Date.now();
    // var now = performance.now();
    // console.log("時間1：" + start);
    // console.log("時間2：" + now);
  

    // 50ミリ秒後に再度関数を実行
    setTimeout(speedCount, 10);

  }
  

  
  



  // ページ切替用ボタン
  const prevButton = $('#prevPage');
  const nextButton = $('#nextPage');
  // ページ数によって変更
  let currentPage = 1;
  const totalPages = 13;
  prevButton.on('click', prevPage);
  nextButton.on('click', nextPage);

  function nextPage() {
    if (currentPage < totalPages) {
      currentPage++;
      // resetCoordinates();
      clearCanvas();
      drawPage(currentPage);
    }
  }
  function prevPage() {
    if (currentPage > 1) {
      currentPage--;
      // resetCoordinates();
      clearCanvas();
      drawPage(currentPage);
    }
  }



  // モード切替用ボタン
  const penButton = $('#pen-button');
  const pageButton = $('#page-button');
  penButton.on('click', changePen);
  pageButton.on('click', changePage);
  function changePen() {
    mode = "pen";
    // ボタン色変更
    penButton.css('background-color', '#d0d0d0');
    pageButton.css('background-color', '#fff');
  }
  function changePage() {
    mode = "page";
    // ボタン色変更
    pageButton.css('background-color', '#d0d0d0');
    penButton.css('background-color', '#fff');
  }


  // csvファイルダウンロード用ボタン
  $('#dl-button').on('click', function() {
    download();
  });
  function download() {
    // csvファイルへの書き出し
    var blob = new Blob([str],{type:"text/csv"}); //配列に上記の文字列(str)を設定
    var link = document.createElement('a');
    link.href = URL.createObjectURL(blob);
    link.download = "test.csv";
    link.click();
  
    // 初速度、初筆圧など
    var blob2 = new Blob([str0],{type:"text/csv"}); //配列に上記の文字列(str)を設定
    var link2 = document.createElement('a');
    link2.href = URL.createObjectURL(blob2);
    link2.download = "test0.csv";
    link2.click();
  }


  
  // 拡大・縮小
  $('#zoomIn').on('click', function() {
    if (scale < 2) {
      scale += 0.1;
      updateCanvas();
    }
  });

  $('#zoomOut').on('click', function() {
    if (scale > 0.5) {
      scale -= 0.1;
      updateCanvas();
    }
  });

  function updateCanvas() {
    const originalWidth = canvas.width;
    const originalHeight = canvas.height;
  
    const scaledWidth = originalWidth * scale;
    const scaledHeight = originalHeight * scale;
  
    tempCanvas.width = scaledWidth;
    tempCanvas.height = scaledHeight;
  
    tempCtx.clearRect(0, 0, scaledWidth, scaledHeight);
    tempCtx.drawImage(canvas, 0, 0, originalWidth, originalHeight, 0, 0, scaledWidth, scaledHeight);
  
    ctx.clearRect(0, 0, originalWidth, originalHeight);
    ctx.drawImage(backgroundImage, 0, 0);
    ctx.drawImage(tempCanvas, 0, 0);
  }
  


  const pages = [
    // { background: '#ff00ff', drawings: [] }, // ページ1のデータ
    // { background: '#ffff00', drawings: [] }, // ページ2のデータ
  	{ background: '/img/fill.SVG', drawings: [] },
    { background: '/img/underLine.SVG', drawings: [] },
    { background: '/img/writing.SVG', drawings: [] },
    { background: '/img/page1.SVG', drawings: [] },
    { background: '/img/page2.SVG', drawings: [] },
    { background: '/img/page3.SVG', drawings: [] },
    { background: '/img/page4.SVG', drawings: [] },
    { background: '/img/page5.SVG', drawings: [] },
    { background: '/img/page6.SVG', drawings: [] },
    { background: '/img/page7.SVG', drawings: [] },
    { background: '/img/page8.SVG', drawings: [] },
    { background: '/img/page9.SVG', drawings: [] },
    { background: '/img/page10.SVG', drawings: [] },
    // 他のページのデータも同様に追加
  ];

  // function resetCoordinates() {
  //   currentX = 0;
  //   currentY = 0;
  // }

  function clearCanvas() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
  }

  function drawPage(pageIndex) {
    const page = pages[pageIndex - 1];
  
    // 背景画像を読み込む
    const backgroundImage = new Image();
    backgroundImage.src = page.background;
  
    backgroundImage.onload = function() {
      // 背景画像の縮小後の幅と高さを計算する
      const scaledWidth = canvas.width * scale;
      const scaledHeight = canvas.height * scale;

      // 背景画像をキャンバスに描画する
      ctx.clearRect(0, 0, canvas.width, canvas.height);
      ctx.drawImage(backgroundImage, 0, 0, scaledWidth, scaledHeight);

      // ページの描画内容を反映する
      for (let i = 0; i < page.drawings.length; i++) {
        const drawing = page.drawings[i];
        const previousX = drawing.previousX * scale;
        const previousY = drawing.previousY * scale;
        const currentX = drawing.currentX * scale;
        const currentY = drawing.currentY * scale;
      
        ctx.beginPath();
        ctx.moveTo(previousX, previousY);
        ctx.lineTo(currentX, currentY);
        ctx.stroke();
      }
    };
  }
});
