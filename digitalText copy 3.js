/***********************  
 * 最終更新日：2023/06/13
 ***********************
 * ※変更可 
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

  let isDrawing = false;
  let mode = 0;
  let startX0 = 0;
  let startY0 = 0;
  let startX = 0;
  let startY = 0;
  let endX = 0;
  let endY = 0;

  $(canvas).on('touchstart', function(event) {
    const touch = event.touches[0];
    startX0 = touch.clientX;
    startY0 = touch.clientY;
    startX = touch.clientX;
    startY = touch.clientY;
    isDrawing = true;
    // console.log("start: (" + startX + ", " + startY + ")");
  });


  $(canvas).on('touchmove', function(event) {
    event.preventDefault();
    const touch = event.touches[0];
    endX = touch.clientX;
    endY = touch.clientY;

    if (isDrawing && mode===1) {
      const page = pages[currentPage - 1];

      const previousX = startX;
      const previousY = startY;
      const currentX = endX;
      const currentY = endY;

      page.drawings.push({ previousX, previousY, currentX, currentY });

      ctx.beginPath();
      ctx.moveTo(previousX, previousY);
      ctx.lineTo(currentX, currentY);
      ctx.stroke();

      startX = currentX;
      startY = currentY;
    }
  });

  $(canvas).on('touchend', function(event) {
    const touch = event.changedTouches[0];
    endX = touch.clientX;
    endY = touch.clientY;
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
  

  const pages = [
  	{ background: '#ff00ff', drawings: [] }, // ページ1のデータ
    { background: '#ffff00', drawings: [] }, // ページ2のデータ
    // 他のページのデータも同様に追加
  ];

  // function resetCoordinates() {
  //   currentX = 0;
  //   currentY = 0;
  // }

  function clearCanvas() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
  }

  function drawPage(pageNumber) {
    const page = pages[pageNumber - 1];

    ctx.clearRect(0, 0, canvas.width, canvas.height);

    ctx.fillStyle = page.background;
    ctx.fillRect(0, 0, canvas.width, canvas.height);

    ctx.strokeStyle = '#000000';
    ctx.lineWidth = 2;

    page.drawings.forEach(function(drawing) {
      ctx.beginPath();
      ctx.moveTo(drawing.previousX, drawing.previousY);
      ctx.lineTo(drawing.currentX, drawing.currentY);
      ctx.stroke();
    });
  }
});
