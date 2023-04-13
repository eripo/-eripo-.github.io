

// 要素を取得する
var box = $('#box');

// ドラッグの開始時の座標を格納する変数
var startX;
var startY;

// ドラッグ中かどうかを示すフラグ
var dragging = false;

// ドラッグの開始処理
function startDrag(event) {
  // ドラッグ中フラグをtrueにする
  dragging = true;

  // event.preventDefault();
  startX = event.clientX;
  startY = event.clientY;
  const pressure = event.pressure;
  console.log("X座標："+ startX +"Y座標"+ startY);
  console.log("圧力："+ pressure);

  // ドラッグ中に発生するmousemoveイベントを設定する
  $(document).on('mousemove', drag);
  // ドラッグが終了した際にmouseupイベントを監視する
  $(document).on('mouseup', stopDrag);

  // デフォルトのドラッグ処理をキャンセルする
  return false;
}

// ドラッグ中の処理
function drag(event) {
  if (!dragging) {
    return;
  }

  // マウスの現在位置と開始位置から、移動量を計算する
  var moveX = event.clientX - startX;
  var moveY = event.clientY - startY;
  // pressure = event.pressure;
  // タッチデバイスの場合はforce、マウスの場合はundefinedになる
  var pressure = event.force;
  if (pressure === undefined) {
    // マウスの場合はbuttonsプロパティを使用する
    pressure = "マウス使用";
  }
  console.log("X座標："+ startX +"Y座標"+ startY);
  console.log("圧力："+ pressure);

  // 要素の位置を移動する
  box.css({
    left: "+=" + moveX,
    top: "+=" + moveY
  });

  // 新しい座標を開始位置に設定する
  startX = event.clientX;
  startY = event.clientY;
}

// ドラッグ終了時の処理
function stopDrag(event) {
  // ドラッグ中フラグをfalseにする
  dragging = false;

  // ドラッグ中に発生するmousemoveイベントを解除する
  $(document).off('mousemove', drag);
  // mouseupイベントを解除する
  $(document).off('mouseup', stopDrag);
}

// mousedownイベントを監視し、ドラッグ開始時の処理を呼び出す
box.on('mousedown', startDrag);
