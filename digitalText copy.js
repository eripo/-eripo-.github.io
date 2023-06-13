$(document).ready(function() {
  const canvas = document.getElementById('canvas');
  const ctx = canvas.getContext('2d');

  let isDrawing = false;
  let currentX = 0;
  let currentY = 0;

  $(canvas).on('mousedown', function(event) {
    isDrawing = true;
    currentX = event.clientX;
    currentY = event.clientY;
  });

  $(canvas).on('mousemove', function(event) {
    if (!isDrawing) return;

    const page = pages[currentPage - 1];

    const previousX = currentX;
    const previousY = currentY;
    currentX = event.clientX;
    currentY = event.clientY;

    page.drawings.push({
      previousX,
      previousY,
      currentX,
      currentY
    });

    ctx.beginPath();
    ctx.moveTo(previousX, previousY);
    ctx.lineTo(currentX, currentY);
    ctx.stroke();
  });

  $(canvas).on('mouseup', function() {
    isDrawing = false;
  });

  const prevButton = $('#prevPage');
  const nextButton = $('#nextPage');
  let currentPage = 1;
  const totalPages = 10;

  prevButton.on('click', function() {
    if (currentPage > 1) {
      currentPage--;
      clearCanvas();
      drawPage(currentPage);
    }
  });

  nextButton.on('click', function() {
    if (currentPage < totalPages) {
      currentPage++;
      clearCanvas();
      drawPage(currentPage);
    }
  });

  const pages = [
  	{ background: '#ff00ff', drawings: [] }, // ページ1のデータ
    { background: '#ffff00', drawings: [] }, // ページ2のデータ
    // 他のページのデータも同様に追加
  ];

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
