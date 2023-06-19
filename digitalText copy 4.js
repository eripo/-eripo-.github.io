/***********************  
 * 最終更新日：2023/06/18
 ***********************
 * ※変更可（データ取得機能実装済み。ただし、座標情報が正確か未確認）
 ***********************
 * デジタル教科書
 * 
 ** 機能 **
 * 書き込み
 * ページめくり 
 * モード切替ボタンでモード変更。
 * 書き込みの座標ずれ無し。
 * データ取得機能（速度など）。ただし、座標情報が正確か確認する必要あり。
 *********************** 
 * 
 * startX0: タッチスタート時の座標
 * startX: ドラッグ中の座標（その区間における始点）
 * endX: ドラッグ中の座標（その区間における終点）
 * 
 * ページめくり幅（endX-startX0）：50
 * 書き込みは、startXからendXの線分を描いていくことで書いている 
 ***********************
 * 問題点・未実装
 * ・拡大・縮小不可（ボタンのみ有）
 * ・データ取得機能（速度など）座標情報が正確か確認する必要あり。
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

  console.log('画面左上端の座標: (' + window.pageXOffset + ', ' + window.pageYOffset + ')');
  console.log('canvas要素の左上端の座標: (' + clientRect.left + ', ' + clientRect.top + ')');


  let scale = 1; // 現在の拡大率
  var str = "";
  str += "v_x" + "," + "v_y" + "," + "v" + "," + "pos_x" + "," + "pos_y" + "," + "Mode" + "\n";  // 速度X成分、速度Y成分、合成速度、筆圧

  var str0 = "";
  str0 += "pressure0" + "," + "v0_x" + "," + "v0_y" + "," + "v0" + "," + "pos_x" + "," + "pos_y" + "," + "Mode" + "\n";  // 初速度X成分、初速度Y成分、合成初速度、初筆圧


  let count = 0;
  let isDrawing = false;
  var isDrag = false;

  let mode = "page";
  let startX0 = 0;
  let startY0 = 0;
  let startX = 0;
  let startY = 0;
  let endX = 0;
  let endY = 0;

  let previousX;
  let previousY;
  let currentX;
  let currentY;

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
    event.preventDefault();
    isDrag = true;

    if (event.type === 'mousedown') {
      startX0 = event.clientX - elemGapX;
      startY0 = event.clientY - elemGapY;
      startX = event.clientX - elemGapX;
      startY = event.clientY - elemGapY;
      var pressure = 1;
    } else if (event.type === 'touchstart') {
      const touch = event.touches[0];
      startX0 = touch.clientX - elemGapX;
      startY0 = touch.clientY - elemGapY;
      startX = touch.clientX - elemGapX;
      startY = touch.clientY - elemGapY;
      var pressure = touch.force;
    }
    
    isDrawing = true;
    velX = startX0;
    velY = startY0;
    previousX = startX0;
    previousY = startY0;
    currentX = startX0;
    currentY = startY0;
    console.log("start0: (" + startX0 + ", " + startY0 + ")");
    console.log("start: (" + startX + ", " + startY + ")");

    
    str0 += pressure;
    console.log("圧力："+ pressure);
    speedCount();
  });


  $(canvas).on('mousemove touchmove', function(event) {
    event.preventDefault();

    if (event.type === 'mousemove') {
      endX = event.clientX - elemGapX;
      endY = event.clientY - elemGapY;
    } else if (event.type === 'touchmove') {
      const touch = event.touches[0];
      endX = touch.clientX - elemGapX;
      endY = touch.clientY - elemGapY;
    }
    // console.log("X座標："+ startX +"Y座標"+ startY);



    const page = pages[currentPage - 1];

    previousX = startX / scale;
    previousY = startY / scale;
    currentX = (endX / scale) - elemGapX;
    currentY = (endY / scale) - elemGapY;
    console.log("あ: " + currentX + ", " + previousX);

    if (isDrawing && mode==="pen") {
      page.drawings.push({ previousX, previousY, currentX, currentY });

      ctx.beginPath();
      ctx.moveTo(previousX, previousY);
      ctx.lineTo(currentX, currentY);
      console.log("start: " + startX + ", " + startY);
      console.log("gap: " + elemGapX + ", " + elemGapY);
      console.log("previous: " + previousX + ", " + previousY);
      console.log("current: " + currentX + ", " + currentY);
      ctx.stroke();

      startX = currentX;
      startY = currentY;
    }


  });

  $(canvas).on('mouseup touchend', function(event) {
    event.preventDefault();
    isDrag = false;

    if (event.type === 'mouseup') {
      endX = event.clientX;
      endY = event.clientY;
    } else if (event.type === 'touchend') {
      const touch = event.changedTouches[0];
      endX = touch.clientX;
      endY = touch.clientY;
    }
    isDrawing = false;

    console.log("end-start: " + (endX-startX0));
    if(mode==="page") {
      if (endX - startX0 < -50) {
        nextPage();
      } else if (endX - startX0 > 50) {
        prevPage();
      }
    }

    count = 0;
  });



  function speedCount() {
    // 速度を計算する処理を記述
    // if (vel == false) { // pointに値が入ってなかったら、速さ(0,0)
    //   velX = 0;
    //   velY = 0;
    // } else {
    //   if (dpoint0 == false) {
    //     dpoint0 = point;
    //   }
    if(!isDrag) {
      return;
    }

    velX = currentX - previousX;
    velY = currentY - previousY;
    console.log("velX,velY: " + velX + ", " + velY + "," + currentX + previousX);
    // 普通の速さ
    vel = Math.sqrt(velX**2 + velY**2);

    // ボックス内に(x方向の速度：y方向の速度)
    // $("#canvas").text(vpoint[0] + ":" + vpoint[1]);
    if(count != 0) {
      str += velX + "," + velY + "," + vel + "," + currentX + "," + currentY + "," + mode + "\n";
    }

    if(count === 1) {
      str0 += "," + velX + "," + velY + "," + vel + "," + currentX + "," + currentY + "," + mode + "\n";
    }
    // dpoint0 = point;

    console.log("count:" + count);
    console.log("座標: " + currentX + ", " + currentY);
    count++;
  
    // 100ミリ秒後に再度関数を実行
    setTimeout(speedCount, 100);
  }
  

  
  



  // ページ切替用ボタン
  const prevButton = $('#prevPage');
  const nextButton = $('#nextPage');
  // ページ数によって変更
  let currentPage = 1;
  const totalPages = 2;
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
  	{ background: '/img/Textbook_page1.png', drawings: [] }, // ページ1のデータ
    { background: '/img/Textbook_page2.png', drawings: [] }, // ページ2のデータ
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
