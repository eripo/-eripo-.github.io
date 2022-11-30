

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
var pointdd = Array(0, 0);
var pointd0 = false;
function spcount() {
  if (point == false) {
    pointdd = Array(0, 0);
  } else {
    if (pointd0 == false) {
      pointd0 = point;
    }
    pointdd = Array(point[0] - pointd0[0], point[1] - pointd0[1]);
    $("#box").text(pointdd[0] + ":" + pointdd[1]);
    pointd0 = point;
  }
  setTimeout(function() {
    spcount();
  }, 100);
}
$(function() {
  spcount();
});


// ドラッグしてるかどうかを判定し、ドラッグ中であればその動きに合わせて四角を動かす関数
// 参考：https://note.com/amanemi/n/nf7fb79e5e578
$(function() {
  $(document).on("mousedown touchstart", "#box", function() {
    $("#box").addClass("move");
  });
  $(document).on("mouseup mouseleave touchend", function() {
    $("#box").removeClass("move");
    point = false;
  });
  $(document).on("mousemove touchmove", function(e) {
    if ($("#box").hasClass("move")) {
      var point0 = getCursor(e);
      if (point === false) {
        point = point0;
      }
      var pointd = Array(point[0] - point0[0], point[1] - point0[1]);
      var x =
        $("#box")
          .css("left")
          .replace("px", "") - pointd[0];
      var y =
        $("#box")
          .css("top")
          .replace("px", "") - pointd[1];
      $("#box").css({
        left: x,
        top: y
      });
      point = point0;
    }
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
      return Array(
        e.originalEvent.changedTouches[0].pageX,
        e.originalEvent.changedTouches[0].pageY
      );
    }
  }
  return Array(false, false);
}