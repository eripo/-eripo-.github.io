/***********************  
 * 最終更新日：2023/06/15
 ***********************
 * ※変更可 拡大・縮小機能試すも、うまくいかず、copy 4で再挑戦。
 ***********************
 * デジタル教科書
 * モード切替ボタンでモード変更。
 *********************** 
 * 
 * startX0: タッチスタート時の座標
 * startX: ドラッグ中の座標（その区間における始点）
 * endX: ドラッグ中の座標（その区間における終点）
 * 
 * ページめくり幅（endX-startX0）：50
 * 書き込みは、startXからendXの線分を描いていくことで書いている 
************************/

$(document).ready(function() {
  const canvas = document.getElementById('canvas');
  const ctx = canvas.getContext('2d');

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
  const originalImage = new Image();
  originalImage.src = backgroundImageUrl;

  // 背景画像が読み込まれた後に描画を開始する
  originalImage.onload = function() {
    drawPage(currentPage);
  };



  $(canvas).on('mousedown touchstart', function(event) {
    event.preventDefault();

    if (event.type === 'mousedown') {
      startX0 = event.clientX;
      startY0 = event.clientY;
      startX = event.clientX;
      startY = event.clientY;
    } else if (event.type === 'touchstart') {
      const touch = event.touches[0];
      startX0 = touch.clientX;
      startY0 = touch.clientY;
      startX = touch.clientX;
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

      const previousX = startX / scale;
      const previousY = startY / scale;
      const currentX = endX / scale;
      const currentY = endY / scale;

      page.drawings.push({ previousX, previousY, currentX, currentY });

      ctx.beginPath();
      ctx.moveTo(previousX, previousY);
      ctx.lineTo(currentX, currentY);
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
    tempCtx.drawImage(originalImage, 0, 0, originalWidth, originalHeight, 0, 0, scaledWidth, scaledHeight);

    ctx.clearRect(0, 0, canvas.width, canvas.height);
    ctx.drawImage(tempCanvas, 0, 0);
  }


  const pages = [
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

      // ページに保存されている描画データを再描画する
      for (const drawing of page.drawings) {
        draw(drawing.startX, drawing.startY, drawing.endX, drawing.endY);
      }
      // for (let i = 0; i < page.drawings.length; i++) {
      //   const drawing = page.drawings[i];
      //   ctx.beginPath();
      //   ctx.moveTo(drawing.previousX, drawing.previousY);
      //   ctx.lineTo(drawing.currentX, drawing.currentY);
      //   ctx.stroke();
      // }
    };
  }
});