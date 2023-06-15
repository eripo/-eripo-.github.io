/***********************  
 * 最終更新日：2023/06/16
 ***********************
 * ※変更可 拡大・縮小機能　大苦戦中
 ***********************
 * デジタル教科書
 * モード切替ボタンでモード変更。
 * 書き込みの座標ずれ無し。
 *********************** 
 * 
 * startX0: タッチスタート時の座標
 * startX: ドラッグ中の座標（その区間における始点）
 * endX: ドラッグ中の座標（その区間における終点）
 * 
 * ページめくり幅（endX-startX0）：50
 * 書き込みは、startXからendXの線分を描いていくことで書いている 
 ***********************
 * 問題点
 * ・拡大・縮小不可
 * 
************************/

$(document).ready(function() {
  const canvas = document.getElementById('canvas');
  const ctx = canvas.getContext('2d');

  const drawingCanvas = document.createElement('canvas');
  const drawingCtx = drawingCanvas.getContext('2d');

  // 要素の位置座標を取得
  var clientRect = canvas.getBoundingClientRect() ;

  // ページの左端から、要素の左端までの距離
  var elemGapX = window.pageXOffset + clientRect.left ;

  // ページの上端から、要素の上端までの距離
  var elemGapY = window.pageYOffset + clientRect.top ;

  console.log('画面左上端の座標: (' + window.pageXOffset + ', ' + window.pageYOffset + ')');
  console.log('canvas要素の左上端の座標: (' + clientRect.left + ', ' + clientRect.top + ')');


  let scale = 1; // 現在の拡大率

  let isDrawing = false;
  let mode = 0;
  let startX0 = 0;
  let startY0 = 0;
  let startX = 0;
  let startY = 0;
  let endX = 0;
  let endY = 0;

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

    if (event.type === 'mousedown') {
      startX0 = event.clientX;
      startY0 = event.clientY;
      startX = event.clientX - elemGapX;
      startY = event.clientY;
    } else if (event.type === 'touchstart') {
      const touch = event.touches[0];
      startX0 = touch.clientX;
      startY0 = touch.clientY;
      startX = touch.clientX - elemGapX;
      startY = touch.clientY;
    }
    
    isDrawing = true;
    // console.log("start: (" + startX + ", " + startY + ")");
  });


  $(canvas).on('mousemove touchmove', function(event) {
    event.preventDefault();

    if (event.type === 'mousemove') {
      endX = event.clientX;
      endY = event.clientY;
    } else if (event.type === 'touchmove') {
      const touch = event.touches[0];
      endX = touch.clientX;
      endY = touch.clientY;
    }

    if (isDrawing && mode===1) {
      const page = pages[currentPage - 1];

      // const previousX = startX / scale - elemGapX;
      // const previousY = startY / scale - elemGapY;
      // const currentX = endX / scale - elemGapX;
      // const currentY = endY / scale - elemGapY;
      const previousX = (startX / scale);
      const previousY = startY / scale;
      const currentX = (endX / scale) - elemGapX;
      const currentY = endY / scale;

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
    if(mode===0) {
      if (endX - startX0 < -50) {
        nextPage();
      } else if (endX - startX0 > 50) {
        prevPage();
      }
    }
    
  });


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

  // ページ切替用ボタン
  const prevButton = $('#prevPage');
  const nextButton = $('#nextPage');
  let currentPage = 1;
  const totalPages = 10;
  
  prevButton.on('click', prevPage);
  nextButton.on('click', nextPage);



  // モード切替用ボタン
  const penButton = $('#pen-button');
  const pageButton = $('#page-button');
  penButton.on('click', changePen);
  pageButton.on('click', changePage);

  function changePen() {
    mode = 1;
    // ボタン色変更
    penButton.css('background-color', '#d0d0d0');
    pageButton.css('background-color', '#fff');
  }
  function changePage() {
    mode = 0;
    // ボタン色変更
    pageButton.css('background-color', '#d0d0d0');
    penButton.css('background-color', '#fff');
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
  
    // 描画データを反映する
    const page = pages[currentPage - 1];
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
