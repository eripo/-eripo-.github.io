/******** プログラム内容 ********/

/* タッチ時の筆圧、ドラッグ速度を取得するプログラム        */

/*******************************/


// 要素を取得する
var canvas = $('#canvas');
// canvas要素を取得する
const drawArea = document.getElementById('canvas');
const context = drawArea.getContext('2d');

// ドラッグの開始時の座標を格納する変数
var startX;
var startY;



/* ドラッグ速度 */
// ドラッグ速度を求めるプログラム　※ドラッグ中の速度。ドラッグを終了したときの速さは0にならない。
// 「100msごとにドラッグの処理で使っているマウスの位置情報からドラッグ速度を割り出して記録し、箱にx,y座標の速度を表示」
// 「斜め方向の速度を出したい場合は三平方の定理とかなんとかから出してください」
// 参考：https://note.com/amanemi/n/n77774ddf19b8
var point = false;
var vpoint = Array(0, 0);
var dpoint0 = false;
var v = false;
var count = 0;
var mode = "";

var str = "";
str += "v_x" + "," + "v_y" + "," + "v" + "," + "Mode" + "\n";  // 速度X成分、速度Y成分、合成速度、筆圧

var str0 = "";
str0 += "pressure0" + "," + "v0_x" + "," + "v0_y" + "," + "v0" + "," + "Mode" + "\n";  // 初速度X成分、初速度Y成分、合成初速度、初筆圧

// 関数：速さを求める
function speedCount() {
  if (point == false) { // pointに値が入ってなかったら、速さ(0,0)
    vpoint = Array(0, 0);
  } else {
    if (dpoint0 == false) {
      dpoint0 = point;
    }

    v_x = point[0] - dpoint0[0];
    v_y = point[1] - dpoint0[1];
    // 普通の速さ
    v = Math.sqrt(v_x**2 + v_y**2);
    vpoint = Array(v_x, v_y);

    // ボックス内に(x方向の速度：y方向の速度)
    // $("#canvas").text(vpoint[0] + ":" + vpoint[1]);
    if(count != 0) {
      str += vpoint[0] + "," + vpoint[1] + "," + v + "," + mode + "\n";
    }

    if(count === 1) {
      str0 += "," + vpoint[0] + "," + vpoint[1] + "," + v + "," + mode + "\n";
    }
    dpoint0 = point;

    console.log("count:" + count);
    count++;
  }

  // 100ミリ秒ごとにspeedCount関数を実行する。
  setTimeout(
    function() {
      speedCount();
    }, 100
  );
}


// speedCount実行部
$(function() {
  speedCount();
});


// ドラッグしてるかどうかを判定し、ドラッグ中であればその動きに合わせて四角を動かす関数
// 参考：https://note.com/amanemi/n/nf7fb79e5e578
$(function() {

  $('#btn_dl').on('click', function() {
    download();
  });

  $('#btn_pen').on('click', function() {
    mode = "pen";
  });

  $('#btn_page').on('click', function() {
    mode = "page";
  });
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



/* 筆圧 */


// ドラッグ中かどうかを示すフラグ
var dragging = false;

// ドラッグの開始処理
function startDrag(event) {
  event.preventDefault();
  $("#canvas").addClass("move");

  // str += "MouseDown\n";


  // ドラッグ中フラグをtrueにする
  dragging = true;

  // event.preventDefault();
  // startX = event.clientX;
  // startY = event.clientY;
  
  startX = event.touches[0].clientX;
  startY = event.touches[0].clientY;
  var pressure = event.touches[0].force;

  str0 += pressure;
  if (pressure === undefined) {
    // マウスの場合はbuttonsプロパティを使用する
    pressure = "マウス使用";
  }
  


  console.log("X座標："+ startX +"Y座標"+ startY);
  console.log("圧力："+ pressure);

  // ドラッグ中に発生するmousemoveイベントを設定する
  $(canvas).on('touchmove mousemove', drag);
  // ドラッグが終了した際にmouseupイベントを監視する
  $(canvas).on('touchend mouseup', stopDrag);

  // デフォルトのドラッグ処理をキャンセルする
  return false;
}


// ドラッグ中の処理
function drag(event) {
  if (!dragging) {
    return;
  }

  // 速度計算のための座標取得等
  if ($("#canvas").hasClass("move")) {
    var point0 = getCursor(event);  //クリックした点の座標(x,y)
    if (point === false) {  //pointに値が入ってなかったら、クリックしたときの座標（初期値）を入れる。
      point = point0;
    }

    var touch = event.touches[0];
    context.beginPath();
    context.moveTo(point0[0] - this.offsetLeft, point0[1] - this.offsetLeft);
    // console.log("moveto((" + point0[0] + ", " + point0[1] + ", point:" +  point[0] + ", " + point[1])
    context.lineTo(point[0] - this.offsetLeft, point[1] - this.offsetTop);
    // console.log("lineto((" + touch.pageX + ", offsetLeft:" +  this.offsetLeft + ", pageY:" + touch.pageY + ", offsetTop" + this.offsetTop)
    context.stroke();

    // var dpoint = Array(point[0] - point0[0], point[1] - point0[1]); //前回の座標との差分
    // var x = $("#canvas").css("left").replace("px", "") - dpoint[0];
    // var y = $("#canvas").css("top").replace("px", "") - dpoint[1];
    // $("#canvas").css({
    //   left: x,
    //   top: y
    // });
    point = point0; //今回の座標を記録
  }
  

  // 要素の位置を移動する
  /* canvas.css({
    left: "+=" + moveX,
    top: "+=" + moveY
  }); */


  // 新しい座標を開始位置に設定する
  startX = event.touches[0].clientX;
  startY = event.touches[0].clientY;

}


// ドラッグ終了時の処理
function stopDrag(event) {
  event.preventDefault();
  count = 0;

  $("#canvas").removeClass("move");
  point = false;  //nullやNaN,undefinedなどが入ってたらfalse。
  dpoint0 = false;

  // str += "MouseLeave\n";

  // ドラッグ中フラグをfalseにする
  dragging = false;

  // ドラッグ中に発生するmousemoveイベントを解除する
  $(canvas).off('touchmove mousemove', drag);
  // mouseupイベントを解除する
  $(canvas).off('touchend mouseup', stopDrag);
}

// mousedownイベントを監視し、ドラッグ開始時の処理を呼び出す
canvas.on('touchstart mousedown', startDrag);



// クリックした座標を求める関数
// 参考：https://note.com/amanemi/n/nfbf0c99e82a1
function getCursor(e) {
  if (e.pageX !== undefined) {
    return Array(e.pageX, e.pageY);
  } else {
    if (e.pageX !== undefined) {
      return Array(e.pageX, e.pageY);
    } else if (window.event.clientX !== undefined) {
      return Array(window.event.clientX, window.event.clientY);
    } else if (e.originalEvent.changedTouches[0].pageX !== undefined) {
      return Array( e.originalEvent.changedTouches[0].pageX, e.originalEvent.changedTouches[0].pageY );
    }
  }
  return Array(false, false);
}


