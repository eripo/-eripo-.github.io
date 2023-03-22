/* メインプログラム */

/******** プログラム内容 ********/

/* 速さを求めるプログラム        */

/*******************************/

/* 変数リスト */
// v_x   x方向の速さ
// v_y   y方向の速さ
// v     xy合成成分の速さ




// 関数を実行し、クリックした座標をコンソールに出力
// 参考：https://note.com/amanemi/n/nfbf0c99e82a1
$(function(){
    $(document).on("mousedown touchstart",function(e){
        var cur = getCursor(e);
        console.log(cur[0]+":"+cur[1]);
    });
});


// ドラッグ速度を求めるプログラム　※ドラッグ中の速度。ドラッグを終了したときの速さは0にならない。
// 「100msごとにドラッグの処理で使っているマウスの位置情報からドラッグ速度を割り出して記録し、箱にx,y座標の速度を表示」
// 「斜め方向の速度を出したい場合は三平方の定理とかなんとかから出してください」
// 参考：https://note.com/amanemi/n/n77774ddf19b8
var point = false;
var vpoint = Array(0, 0);
var dpoint0 = false;
var v = false;

var str = "";
str += "v_x" + "," + "v_y" + "," + "v" + "\n";

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
    // ボックス内に(x方向の速さ：y方向の速さ)
    $("#box").text(vpoint[0] + ":" + vpoint[1]);
    str += vpoint[0] + "," + vpoint[1] + "," + v + "\n";
    dpoint0 = point;
  }

  // 100ミリ秒ごとにspeedCount関数を実行する。
  setTimeout(
    function() {
      speedCount();
    }, 100
  );
}

function download() {
  // csvファイルへの書き出し
  var blob = new Blob([str],{type:"text/csv"}); //配列に上記の文字列(str)を設定
  var link = document.createElement('a');
  link.href = URL.createObjectURL(blob);
  link.download = "test.csv";
  link.click();
}


// speedCount実行部
$(function() {
  speedCount();
});


// ドラッグしてるかどうかを判定し、ドラッグ中であればその動きに合わせて四角を動かす関数
// 参考：https://note.com/amanemi/n/nf7fb79e5e578
$(function() {
  // マウスダウン　でid=boxにclass=moveを付与
  $(document).on("mousedown touchstart", "#box", function() {
    $("#box").addClass("move");

    str += "MouseDown\n";
  });

  // マウスアップ　でid=boxのclass=moveを取り外す
  $(document).on("mouseup mouseleave touchend", function() {
    $("#box").removeClass("move");
    point = false;  //nullやNaN,undefinedなどが入ってたらfalse。

    str += "MouseLeave\n";

  });

  // ドラッグ操作中
  $(document).on("mousemove touchmove", function(e) {
    if ($("#box").hasClass("move")) {
      var point0 = getCursor(e);  //クリックした点の座標(x,y)
      if (point === false) {  //pointに値が入ってなかったら、クリックしたときの座標（初期値）を入れる。
        point = point0;
      }
      var dpoint = Array(point[0] - point0[0], point[1] - point0[1]); //前回の座標との差分
      var x = $("#box").css("left").replace("px", "") - dpoint[0];
      var y = $("#box").css("top").replace("px", "") - dpoint[1];
      $("#box").css({
        left: x,
        top: y
      });
      point = point0; //今回の座標を記録
    }
  });

  $('#btn_dl').on('click', function() {
    download();
  });

  $('#btn_pen').on('click', function() {
    str += "Mode: pen\n";
  });

  $('#btn_page').on('click', function() {
    str += "Mode: page\n";
  });

});


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