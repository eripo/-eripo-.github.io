/***********************  
 * 最終更新日：2023/11/10
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
 * ・strMid その都度（変位，速度，加速度については，画面上での動きだけでなく現実の動きに合わせたものも取得）
 *    - 筆圧，変位X，変位Y，変位，速度X，速度Y，速度，加速度X，加速度Y，加速度，座標X，座標Y，処理時間，モード
 * ・strInitial 初動（変位，速度，加速度については，画面上での動きだけでなく現実の動きに合わせたものも取得）
 *    - 筆圧，経過時間，変位X，変位Y，変位，速度X，速度Y，速度，加速度X，加速度Y，加速度，座標X，座標Y，処理時間，モード
  * ・strFinal 終了時（速度，加速度，外接矩形幅については，画面上での動きだけでなく現実の動きに合わせたものも取得）
 *    - 速度X最小値，速度X最大値，速度X平均，速度X中央値，速度Y最小値，速度Y最大値，速度Y平均，速度Y中央値，速度最小値，速度最大値，速度平均，速度中央値，
 *      加速度X最小値，加速度X最大値，加速度X平均，加速度X中央値，加速度Y最小値，加速度Y最大値，加速度Y平均，加速度Y中央値，加速度最小値，加速度最大値，加速度平均，加速度中央値，
 *      筆圧最小値，筆圧最大値，筆圧平均，筆圧中央値，ドラッグ時間，外接矩形幅X，外接矩形幅Y，モード
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
 * ページめくり幅（currentX-startX0）：10
 * 書き込みは、previousXからcurrentXの線分を描いていくことで書いている 
 ***********************
 * 問題点・未実装
 * ・拡大・縮小不可（ボタンはコメントアウト中）
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

  // 筆圧，変位X，変位Y，変位，速度X，速度Y，速度，加速度X，加速度Y，加速度，座標X，座標Y，処理時間，モード
  var strMid = "";
  strMid += "pressure" + "," + "gapX" + "," + "gapY" + "," + "gap" + "," + "gapRX" + "," + "gapRY" + "," + "gapR" + "," + "velX" + "," + "velY" + "," + "vel" + "," + "velRX" + "," + "velRY" + "," + "velR" + "," + "accelerationX" + "," + "accelerationY" + "," + "acceleration" + "," + "accelerationRX" + "," + "accelerationRY" + "," + "accelerationR" + "," + "posX" + "," + "posY" + "," + "msec" + "," + "nowTime" + "," + "elapsed_time" + "," + "count" + "," + "Mode" + "\n";

  // 筆圧，経過時間，変位X，変位Y，変位，速度X，速度Y，速度，加速度X，加速度Y，加速度，座標X，座標Y，処理時間，モード
  var strInitial = "";
  strInitial += "pressure0" + "," + "intervalTime" + "," + "gapX" + "," + "gapY" + "," + "gap" + "," + "gapRX" + "," + "gapRY" + "," + "gapR" + "," + "velX" + "," + "velY" + "," + "vel" + "," + "velRX" + "," + "velRY" + "," + "velR" + "," + "accelerationX" + "," + "accelerationY" + "," + "acceleration" + "," + "accelerationRX" + "," + "accelerationRY" + "," + "accelerationR" + "," + "posX" + "," + "posY" + "," + "msec" + "," + "Mode" + "\n";

  // 速度X最小値，速度X最大値，速度X平均，速度X中央値，速度Y最小値，速度Y最大値，速度Y平均，速度Y中央値，速度最小値，速度最大値，速度平均，速度中央値，
  // 加速度X最小値，加速度X最大値，加速度X平均，加速度X中央値，加速度Y最小値，加速度Y最大値，加速度Y平均，加速度Y中央値，加速度最小値，加速度最大値，加速度平均，加速度中央値，
  // 筆圧最小値，筆圧最大値，筆圧平均，筆圧中央値，ドラッグ時間，外接矩形幅X，外接矩形幅Y，モード
  var strFinal = "";
  strFinal += "velX_min" + "," + "velX_max" + "," + "velX_mean" + "," + "velX_median" + "," + "velX_first" + "," + "velX_last"
           + "," + "velY_min" + "," + "velY_max" + "," + "velY_mean" + "," + "velY_median" + "," + "velY_first" + "," + "velY_last"
           + "," + "vel_min" + "," + "vel_max" + "," + "vel_mean" + "," + "vel_median" + "," + "vel_first" + "," + "vel_last"
           + "," + "velRX_min" + "," + "velRX_max" + "," + "velRX_mean" + "," + "velRX_median" + "," + "velRX_first" + "," + "velRX_last"
           + "," + "velRY_min" + "," + "velRY_max" + "," + "velRY_mean" + "," + "velRY_median" + "," + "velRY_first" + "," + "velRY_last"
           + "," + "velR_min" + "," + "velR_max" + "," + "velR_mean" + "," + "velR_median" + "," + "velR_first" + "," + "velR_last" 
           + "," + "accelerationX_min" + "," + "accelerationX_max" + "," + "accelerationX_mean" + "," + "accelerationX_median" + "," + "accelerationX_first" + "," + "accelerationX_last" + "," + "1/5_accelerationX_mean" + "," + "1/5_accelerationX_median" + "," + "2/5_accelerationX_mean" + "," + "2/5_accelerationX_median" + "," + "4/5_accelerationX_mean" + "," + "4/5_accelerationX_median"
           + "," + "accelerationY_min" + "," + "accelerationY_max" + "," + "accelerationY_mean" + "," + "accelerationY_median" + "," + "accelerationY_first" + "," + "accelerationY_last" + "," + "1/5_accelerationY_mean" + "," + "1/5_accelerationY_median" + "," + "2/5_accelerationY_mean" + "," + "2/5_accelerationY_median" + "," + "4/5_accelerationY_mean" + "," + "4/5_accelerationY_median"
           + "," + "acceleration_min" + "," + "acceleration_max" + "," + "acceleration_mean" + "," + "acceleration_median" + "," + "acceleration_first" + "," + "acceleration_last" + "," + "1/5_acceleration_mean" + "," + "1/5_acceleration_median" + "," + "2/5_acceleration_mean" + "," + "2/5_acceleration_median" + "," + "4/5_acceleration_mean" + "," + "4/5_acceleration_median"
           + "," + "accelerationRX_min" + "," + "accelerationRX_max" + "," + "accelerationRX_mean" + "," + "accelerationRX_median" + "," + "accelerationRX_first" + "," + "accelerationRX_last" + "," + "1/5_accelerationRX_mean" + "," + "1/5_accelerationRX_median" + "," + "2/5_accelerationRX_mean" + "," + "2/5_accelerationRX_median" + "," + "4/5_accelerationRX_mean" + "," + "4/5_accelerationRX_median"
           + "," + "accelerationRY_min" + "," + "accelerationRY_max" + "," + "accelerationRY_mean" + "," + "accelerationRY_median" + "," + "accelerationRY_first" + "," + "accelerationRY_last" + "," + "1/5_accelerationRY_mean" + "," + "1/5_accelerationRY_median" + "," + "2/5_accelerationRY_mean" + "," + "2/5_accelerationRY_median" + "," + "4/5_accelerationRY_mean" + "," + "4/5_accelerationRY_median"
           + "," + "accelerationR_min" + "," + "accelerationR_max" + "," + "accelerationR_mean" + "," + "accelerationR_median" + "," + "accelerationR_first" + "," + "accelerationR_last" + "," + "1/5_accelerationR_mean" + "," + "1/5_accelerationR_median" + "," + "2/5_accelerationR_mean" + "," + "2/5_accelerationR_median" + "," + "4/5_accelerationR_mean" + "," + "4/5_accelerationR_median"
           + "," + "pressure_min" + "," + "pressure_max" + "," + "pressure_mean" + "," + "pressure_median" + "," + "pressure_first"  + "," + "pressure_last" 
           + "," + "dragTime" + "," + "widthX" + "," + "widthY" + "," + "widthRX" + "," + "widthRY" + "," + "Mode" + "\n";


  var strInitialModel = "";
  strInitialModel += "real_Mode" + ","	+ "f_Initial_result" + ","	+ "p_Initial_result" + "," + "mix_Initial_result" + "," + "count" + "," + "\n";

  var strFinalModel = "";
  strFinalModel += "real_Mode" + ","	+ "f_Final_result" + ","	+ "p_Final_result" + ","	+ "mix_Final_result" + "," + "count" + "," + "\n";;

  let count = 0;
  let isDrawing = false;
  var isDrag = false;

  let mode = "page";
  let startX0;
  let startY0;
  let startPosX;
  let startPosY;
  // let startX = 0;
  // let startY = 0;
  let startTime = 0;
  let endTime;
  let nowTime;
  let previousTime;
  // let currentX = 0;
  // let currentY = 0;

  
  let subPrevX;
  let subPrevY;
  let subPrevPosX;
  let subPrevPosY;
  let previousX;
  let previousY;
  let prePosX;
  let prePosY;
  let currentX;
  let currentY;
  let curPosX;
  let curPosY;
  let pressure;
  let pressure0;
  let velX;
  let velY;
  let vel;
  let velRX;
  let velRY;
  let velR;
  let accelerationX;
  let accelerationY;
  let acceleration;
  let accelerationRX;
  let accelerationRY;
  let accelerationR;

  let VelX = [];
  let VelY = [];
  let Vel = [];
  let VelRX = [];
  let VelRY = [];
  let VelR = [];
  let AccelerationX = [];
  let AccelerationY = [];
  let Acceleration = [];
  let AccelerationRX = [];
  let AccelerationRY = [];
  let AccelerationR = [];
  let Pressure = [];
  let PositionX = [];
  let PositionY = [];
  let PositionRX = [];
  let PositionRY = [];

  let res1;
  let res2;
  let res3;
  let res4;
  let res5;
  let res6;
  dragCountI = 1;
  dragCountF = 1;

  var intervalId;

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
    // console.log("マウスダウン")
    
    // 次回ドラッグ開始時（インターバル終了）
    endTime = performance.now();
    previousTime = endTime;
    nowTime = endTime;
    // console.log("intervalTime：" + (endTime-startTime));
    // console.log("intervalTime：" + (endTime-startTime) + "\nstart：" + startTime + "\nend：" + endTime)
    // console.log("previousTime:\n" + previousTime);

    event.preventDefault();
    isDrag = true;

    // posX,posYは速度や加速度を求めるための座標．startX0やcurrentXなどelemGapを引いているものは，紙面上の座標を求めるためのもの．
    
    if (event.type === 'mousedown') {
      startX0 = event.clientX - elemGapX;
      startY0 = event.clientY - elemGapY;
      startPosX = event.screenX;
      startPosY = event.screenY;
      pressure0 = 1;
    } else if (event.type === 'touchstart') {
      const touch = event.touches[0];
      startX0 = touch.clientX - elemGapX;
      startY0 = touch.clientY - elemGapY;
      startPosX = touch.screenX;
      startPosY = touch.screenY;
      pressure0 = touch.force;
      pressure = pressure0;
      // console.log("Press: " + pressure0);

      // // 接触面積を求める（デバイス対応なし？）
      // const touch2 = event.touches[0];
      // var touchArea = touch2.radiusX * touch2.radiusY * Math.PI;
      // console.log("Touch Area: " + touchArea + " pixels squared\n" + touch2.radiusX + "\n" + touch2.radiusY);

    }

    // console.log("endTime：" + endTime + "\nstartTime：" + startTime + "\npreviousTime：" + previousTime + "\nnowTime：" + nowTime);
    


    
    isDrawing = true;
    // 紙面上
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

    // リアル
    gapRX = startPosX;
    gapRY = startPosY;    
    subPrevPosX = startPosX;
    subPrevPosY = startPosY;
    prePosX = startPosX;
    prePosY = startPosY;
    curPosX = startPosX;
    curPosY = startPosY;
    preVelRX = 0;
    preVelRY = 0;
    preVelR = 0;
    accelerationRX = 0;
    accelerationRY = 0;
    accelerationR = 0;

    

    VelX = [];
    VelY = [];
    Vel = [];
    VelRX = [];
    VelRY = [];
    VelR = [];
    AccelerationX = [];
    AccelerationY = [];
    Acceleration = [];
    AccelerationRX = [];
    AccelerationRY = [];
    AccelerationR = [];
    Pressure = [];
    PositionX = [];
    PositionY = [];
    PositionRX = [];
    PositionRY = [];

    //1個前の座標（50ミリ秒ごと） 
    positionPrevX = startX0;
    positionPrevY = startY0;
    posPrevX = startPosX;
    posPrevY = startPosY;


    // console.log("ドラッグ始点座標: (" + startX0 + ", " + startY0 + ")");
    // console.log("start: (" + startX + ", " + startY + ")");

    
    strInitial += pressure0 + "," + (endTime-startTime);
    // console.log("圧力："+ pressure);
    speedCount();
    intervalId = window.setInterval(speedCount, 10);
  });


  $(canvas).on('mousemove touchmove', function(event) {
    event.preventDefault();

    if (event.type === 'mousemove') {
      currentX = event.clientX - elemGapX;
      currentY = event.clientY - elemGapY;
      curPosX = event.screenX;
      curPosY = event.screenY;
      pressure = 1;
    } else if (event.type === 'touchmove') {
      const touch = event.touches[0];
      currentX = touch.clientX - elemGapX;
      currentY = touch.clientY - elemGapY;
      curPosX = touch.screenX;
      curPosY = touch.screenY;
      pressure = touch.force;

      // const touch2 = event.touches[0];
      // var touchArea = touch2.radiusX * touch2.radiusY * Math.PI;
      // console.log("Touch Area: " + touchArea + " pixels squared\n" + touch2.radiusX + "\n" + touch2.radiusY);
    }


    const page = pages[currentPage - 1];

    previousX = subPrevX / scale;
    previousY = subPrevY / scale;
    currentX = (currentX / scale);
    currentY = (currentY / scale);

    // scaleは使ってないのでここでもとりあえずなしで．
    prePosX = subPrevPosX;
    prePosY = subPrevPosY;

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

    subPrevPosX = curPosX;
    subPrevPosY = curPosY;


  });

  $(canvas).on('mouseup touchend', function(event) {
    // 前回ドラッグ終了時（インターバル開始）
    startTime = performance.now();

    // ドラッグ時間を出力
    strInitial += "," + mode + "\n";
    

    event.preventDefault();
    isDrag = false;
    clearInterval(intervalId);

    if (event.type === 'mouseup') {
      currentX = event.clientX - elemGapX;
      currentY = event.clientY - elemGapY;
      curPosX = event.screenX;
      curPosY = event.screenY;
    } else if (event.type === 'touchend') {
      const touch = event.changedTouches[0];
      currentX = touch.clientX - elemGapX;
      currentY = touch.clientY - elemGapY;
      curPosX = touch.screenX;
      curPosY = touch.screenY;
    }
    isDrawing = false;

    PositionX.push(currentX);
    PositionY.push(currentY);
    PositionRX.push(curPosX);
    PositionRY.push(curPosY);


    
    $(function(){
      console.log("FFFFF\n")
    
      $.ajax({
          url: 'cgi-bin/open_model_Final.py',
          type: 'get',
          dataType: 'json',
          data: {
              // 最低限ver
              vel_max: ss.max(Vel), vel_median: ss.median(Vel), velRX_min: ss.min(VelRX), velRX_mean: ss.mean(VelRX), velRX_median: ss.median(VelRX), velRX_last: VelRX[VelRX.length - 1], velRY_last: VelRY[VelRY.length - 1], velR_mean: ss.mean(VelR), velR_median: ss.median(VelR), velR_last: VelR[VelR.length - 1], accelerationX_max: ss.max(AccelerationX), acceleration_max: ss.max(Acceleration), acceleration_mean: ss.mean(Acceleration), accelerationRX_max: ss.max(AccelerationRX), accelerationR_min: ss.min(AccelerationR), accelerationR_median: ss.median(AccelerationR), accelerationR_first: AccelerationR[0], widthRX: ss.max(PositionRX) - ss.min(PositionRX)


              // 全データ送りたいとき用
              // test1: ss.min(VelX), test2: ss.max(VelX), test3: ss.mean(VelX), test4: ss.median(VelX), test5: VelX[0], test6: VelX[VelX.length - 1], 
              // test7: ss.min(VelY), test8: ss.max(VelY), test9: ss.mean(VelY), test10: ss.median(VelY), test11: VelY[0], test12: VelY[VelY.length - 1], 
              // test13: ss.min(Vel), test14: ss.max(Vel), test15: ss.mean(Vel), test16: ss.median(Vel), test17: Vel[0], test18: Vel[Vel.length - 1], 
              // test19: ss.min(VelRX), test20: ss.max(VelRX), test21: ss.mean(VelRX), test22: ss.median(VelRX), test23: VelRX[0], test24: VelRX[VelRX.length - 1], 
              // test25: ss.min(VelRY), test26: ss.max(VelRY), test27: ss.mean(VelRY), test28: ss.median(VelRY), test29: VelRY[0], test30: VelRY[VelRY.length - 1], 
              // test31: ss.min(VelR), test32: ss.max(VelR), test33: ss.mean(VelR), test34: ss.median(VelR), test35: VelR[0], test36: VelR[VelR.length - 1], 
              // test37: ss.min(AccelerationX), test38: ss.max(AccelerationX), test39: ss.mean(AccelerationX), test40: ss.median(AccelerationX), test41: AccelerationX[0], test42: AccelerationX[AccelerationX.length - 1], 
              // test43: ss.mean(AccelerationX.slice( -Math.round(AccelerationX.length * 1/5) )), test44: ss.median(AccelerationX.slice( -Math.round(AccelerationX.length * 1/5) )), 
              // test45: ss.mean(AccelerationX.slice( -Math.round(AccelerationX.length * 2/5) )), test46: ss.median(AccelerationX.slice( -Math.round(AccelerationX.length * 2/5) )), 
              // test47: ss.mean(AccelerationX.slice( -Math.round(AccelerationX.length * 4/5) )), test48: ss.median(AccelerationX.slice( -Math.round(AccelerationX.length * 4/5) )), 
              // test49: ss.min(AccelerationY), test50: ss.max(AccelerationY), test51: ss.mean(AccelerationY), test52: ss.median(AccelerationY), test53: AccelerationY[0], test54: AccelerationY[AccelerationY.length - 1], 
              // test55: ss.mean(AccelerationY.slice( -Math.round(AccelerationY.length * 1/5) )), test56: ss.median(AccelerationY.slice( -Math.round(AccelerationY.length * 1/5) )), 
              // test57: ss.mean(AccelerationY.slice( -Math.round(AccelerationY.length * 2/5) )), test58: ss.median(AccelerationY.slice( -Math.round(AccelerationY.length * 2/5) )), 
              // test59: ss.mean(AccelerationY.slice( -Math.round(AccelerationY.length * 4/5) )), test60: ss.median(AccelerationY.slice( -Math.round(AccelerationY.length * 4/5) )), 
              // test61: ss.min(Acceleration), test62: ss.max(Acceleration), test63: ss.mean(Acceleration), test64: ss.median(Acceleration), test65: Acceleration[0], test66: Acceleration[Acceleration.length - 1], 
              // test67: ss.mean(Acceleration.slice( -Math.round(Acceleration.length * 1/5) )), test68: ss.median(Acceleration.slice( -Math.round(Acceleration.length * 1/5) )), 
              // test69: ss.mean(Acceleration.slice( -Math.round(Acceleration.length * 2/5) )), test70: ss.median(Acceleration.slice( -Math.round(Acceleration.length * 2/5) )), 
              // test71: ss.mean(Acceleration.slice( -Math.round(Acceleration.length * 4/5) )), test72: ss.median(Acceleration.slice( -Math.round(Acceleration.length * 4/5) )), 
              // test73: ss.min(AccelerationRX), test74: ss.max(AccelerationRX), test75: ss.mean(AccelerationRX), test76: ss.median(AccelerationRX), test77: AccelerationRX[0], test78: AccelerationRX[AccelerationRX.length - 1], 
              // test79: ss.mean(AccelerationRX.slice( -Math.round(AccelerationRX.length * 1/5) )), test80: ss.median(AccelerationRX.slice( -Math.round(AccelerationRX.length * 1/5) )), 
              // test81: ss.mean(AccelerationRX.slice( -Math.round(AccelerationRX.length * 2/5) )), test82: ss.median(AccelerationRX.slice( -Math.round(AccelerationRX.length * 2/5) )), 
              // test83: ss.mean(AccelerationRX.slice( -Math.round(AccelerationRX.length * 4/5) )), test84: ss.median(AccelerationRX.slice( -Math.round(AccelerationRX.length * 4/5) )), 
              // test85: ss.min(AccelerationRY), test86: ss.max(AccelerationRY), test87: ss.mean(AccelerationRY), test88: ss.median(AccelerationRY), test89: AccelerationRY[0], test90: AccelerationRY[AccelerationRY.length - 1], 
              // test91: ss.mean(AccelerationRY.slice( -Math.round(AccelerationRY.length * 1/5) )), test92: ss.median(AccelerationRY.slice( -Math.round(AccelerationRY.length * 1/5) )), 
              // test93: ss.mean(AccelerationRY.slice( -Math.round(AccelerationRY.length * 2/5) )), test94: ss.median(AccelerationRY.slice( -Math.round(AccelerationRY.length * 2/5) )), 
              // test95: ss.mean(AccelerationRY.slice( -Math.round(AccelerationRY.length * 4/5) )), test96: ss.median(AccelerationRY.slice( -Math.round(AccelerationRY.length * 4/5) )), 
              // test97: ss.min(AccelerationR), test98: ss.max(AccelerationR), test99: ss.mean(AccelerationR), test100: ss.median(AccelerationR), test101: AccelerationR[0], test102: AccelerationR[AccelerationR.length - 1], 
              // test103: ss.mean(AccelerationR.slice( -Math.round(AccelerationR.length * 1/5) )), test104: ss.median(AccelerationR.slice( -Math.round(AccelerationR.length * 1/5) )), 
              // test105: ss.mean(AccelerationR.slice( -Math.round(AccelerationR.length * 2/5) )), test106: ss.median(AccelerationR.slice( -Math.round(AccelerationR.length * 2/5) )), 
              // test107: ss.mean(AccelerationR.slice( -Math.round(AccelerationR.length * 4/5) )), test108: ss.median(AccelerationR.slice( -Math.round(AccelerationR.length * 4/5) )), 
              // test109: ss.min(Pressure), test110: ss.max(Pressure), test111: ss.mean(Pressure), test112: ss.median(Pressure), test113: Pressure[0], test114: Pressure[Pressure.length - 1], 
              // test115: (startTime - endTime), 
              // test116: ss.max(PositionX) - ss.min(PositionX), test117: ss.max(PositionY) - ss.min(PositionY), 
              // test118: ss.max(PositionRX) - ss.min(PositionRX), test119: ss.max(PositionRY) - ss.min(PositionRY)
          }
      }).done(function(dataF){
        console.log(dataF)
        const ans_Ff = dataF.ans_Ff;
        const ans_Fp = dataF.ans_Fp;
        const ans_Fm = dataF.ans_Fm;
        if(ans_Ff[0] === 'page') {
          console.log("ページめくり")
          res1 = "ページめくり"
          $('#JudgeText_Ff').css('color', 'blue');
        } else if(ans_Ff[0] === 'pen') {
          console.log("書き込み")
          res1 = "書き込み"
          $('#JudgeText_Ff').css('color', 'red');
        }
        if(ans_Fp[0] === 'page') {
          console.log("ページめくり")
          res2 = "ページめくり"
          $('#JudgeText_Fp').css('color', 'blue');
        } else if(ans_Fp[0] === 'pen') {
          console.log("書き込み")
          res2 = "書き込み"
          $('#JudgeText_Fp').css('color', 'red');
        }
        if(ans_Fm[0] === 'page') {
          console.log("ページめくり")
          res3 = "ページめくり"
          $('#JudgeText_Fm').css('color', 'blue');
        } else if(ans_Fm[0] === 'pen') {
          console.log("書き込み")
          res3 = "書き込み"
          $('#JudgeText_Fm').css('color', 'red');
        }
        strFinalModel += mode + "," + ans_Ff[0] + "," + ans_Fp[0] + "," + ans_Fm[0] + "," + dragCountF + "\n"
        console.log("strFinalModel: " + strFinalModel)
        // テキストを変更
        $('#Judge_CountF').text(dragCountF);
        $('#JudgeText_Ff').text(res1);
        $('#JudgeText_Fp').text(res2);
        $('#JudgeText_Fm').text(res3);
        console.log(dragCountF)
        dragCountF++;
      }).fail(function(){
          console.log('failed');
      });
    });
    

    // ドラッグ終了時の判別で使用するデータを出力
    strFinal += ss.min(VelX) + "," + ss.max(VelX) + "," + ss.mean(VelX) + "," + ss.median(VelX) + "," + VelX[0] + "," + VelX[VelX.length - 1]
               + "," + ss.min(VelY) + "," + ss.max(VelY) + "," + ss.mean(VelY) + "," + ss.median(VelY) + "," + VelY[0] + "," + VelY[VelY.length - 1]
               + "," + ss.min(Vel) + "," + ss.max(Vel) + "," + ss.mean(Vel) + "," + ss.median(Vel) + "," + Vel[0] + "," + Vel[Vel.length - 1]
               + "," + ss.min(VelRX)+ "," + ss.max(VelRX) + "," + ss.mean(VelRX) + "," + ss.median(VelRX) + "," + VelRX[0] + "," + VelRX[VelRX.length - 1]
               + "," + ss.min(VelRY) + "," + ss.max(VelRY) + "," + ss.mean(VelRY) + "," + ss.median(VelRY) + "," + VelRY[0] + "," + VelRY[VelRY.length - 1]
               + "," + ss.min(VelR) + "," + ss.max(VelR) + "," + ss.mean(VelR) + "," + ss.median(VelR) + "," + VelR[0] + "," + VelR[VelR.length - 1]
               + "," + ss.min(AccelerationX) + "," + ss.max(AccelerationX) + "," + ss.mean(AccelerationX) + "," + ss.median(AccelerationX) + "," + AccelerationX[0] + "," + AccelerationX[AccelerationX.length - 1]
               + "," + ss.mean(AccelerationX.slice( -Math.round(AccelerationX.length * 1/5) )) + "," + ss.median(AccelerationX.slice( -Math.round(AccelerationX.length * 1/5) ))
               + "," + ss.mean(AccelerationX.slice( -Math.round(AccelerationX.length * 2/5) )) + "," + ss.median(AccelerationX.slice( -Math.round(AccelerationX.length * 2/5) ))
               + "," + ss.mean(AccelerationX.slice( -Math.round(AccelerationX.length * 4/5) )) + "," + ss.median(AccelerationX.slice( -Math.round(AccelerationX.length * 4/5) ))
               + "," + ss.min(AccelerationY) + "," + ss.max(AccelerationY) + "," + ss.mean(AccelerationY) + "," + ss.median(AccelerationY) + "," + AccelerationY[0] + "," + AccelerationY[AccelerationY.length - 1]
               + "," + ss.mean(AccelerationY.slice( -Math.round(AccelerationY.length * 1/5) )) + "," + ss.median(AccelerationY.slice( -Math.round(AccelerationY.length * 1/5) ))
               + "," + ss.mean(AccelerationY.slice( -Math.round(AccelerationY.length * 2/5) )) + "," + ss.median(AccelerationY.slice( -Math.round(AccelerationY.length * 2/5) ))
               + "," + ss.mean(AccelerationY.slice( -Math.round(AccelerationY.length * 4/5) )) + "," + ss.median(AccelerationY.slice( -Math.round(AccelerationY.length * 4/5) ))
               + "," + ss.min(Acceleration) + "," + ss.max(Acceleration) + "," + ss.mean(Acceleration) + "," + ss.median(Acceleration) + "," + Acceleration[0] + "," + Acceleration[Acceleration.length - 1]
               + "," + ss.mean(Acceleration.slice( -Math.round(Acceleration.length * 1/5) )) + "," + ss.median(Acceleration.slice( -Math.round(Acceleration.length * 1/5) ))
               + "," + ss.mean(Acceleration.slice( -Math.round(Acceleration.length * 2/5) )) + "," + ss.median(Acceleration.slice( -Math.round(Acceleration.length * 2/5) ))
               + "," + ss.mean(Acceleration.slice( -Math.round(Acceleration.length * 4/5) )) + "," + ss.median(Acceleration.slice( -Math.round(Acceleration.length * 4/5) ))
               + "," + ss.min(AccelerationRX) + "," + ss.max(AccelerationRX) + "," + ss.mean(AccelerationRX) + "," + ss.median(AccelerationRX) + "," + AccelerationRX[0] + "," + AccelerationRX[AccelerationRX.length - 1]
               + "," + ss.mean(AccelerationRX.slice( -Math.round(AccelerationRX.length * 1/5) )) + "," + ss.median(AccelerationRX.slice( -Math.round(AccelerationRX.length * 1/5) ))
               + "," + ss.mean(AccelerationRX.slice( -Math.round(AccelerationRX.length * 2/5) )) + "," + ss.median(AccelerationRX.slice( -Math.round(AccelerationRX.length * 2/5) ))
               + "," + ss.mean(AccelerationRX.slice( -Math.round(AccelerationRX.length * 4/5) )) + "," + ss.median(AccelerationRX.slice( -Math.round(AccelerationRX.length * 4/5) ))
               + "," + ss.min(AccelerationRY) + "," + ss.max(AccelerationRY) + "," + ss.mean(AccelerationRY) + "," + ss.median(AccelerationRY) + "," + AccelerationRY[0] + "," + AccelerationRY[AccelerationRY.length - 1]
               + "," + ss.mean(AccelerationRY.slice( -Math.round(AccelerationRY.length * 1/5) )) + "," + ss.median(AccelerationRY.slice( -Math.round(AccelerationRY.length * 1/5) ))
               + "," + ss.mean(AccelerationRY.slice( -Math.round(AccelerationRY.length * 2/5) )) + "," + ss.median(AccelerationRY.slice( -Math.round(AccelerationRY.length * 2/5) ))
               + "," + ss.mean(AccelerationRY.slice( -Math.round(AccelerationRY.length * 4/5) )) + "," + ss.median(AccelerationRY.slice( -Math.round(AccelerationRY.length * 4/5) ))
               + "," + ss.min(AccelerationR) + "," + ss.max(AccelerationR) + "," + ss.mean(AccelerationR) + "," + ss.median(AccelerationR) + "," + AccelerationR[0] + "," + AccelerationR[AccelerationR.length - 1]
               + "," + ss.mean(AccelerationR.slice( -Math.round(AccelerationR.length * 1/5) )) + "," + ss.median(AccelerationR.slice( -Math.round(AccelerationR.length * 1/5) ))
               + "," + ss.mean(AccelerationR.slice( -Math.round(AccelerationR.length * 2/5) )) + "," + ss.median(AccelerationR.slice( -Math.round(AccelerationR.length * 2/5) ))
               + "," + ss.mean(AccelerationR.slice( -Math.round(AccelerationR.length * 4/5) )) + "," + ss.median(AccelerationR.slice( -Math.round(AccelerationR.length * 4/5) ))
               + "," + ss.min(Pressure) + "," + ss.max(Pressure) + "," + ss.mean(Pressure) + "," + ss.median(Pressure) + "," + Pressure[0] + "," + Pressure[Pressure.length - 1]
               + "," + (startTime - endTime) 
               + "," + (ss.max(PositionX) - ss.min(PositionX)) + "," + (ss.max(PositionY) - ss.min(PositionY)) 
               + "," + (ss.max(PositionRX) - ss.min(PositionRX)) + "," + (ss.max(PositionRY) - ss.min(PositionRY)) 
               + "," + mode + "\n";

    // console.log(currentX + "\n" + currentY);
    // console.log("end-start: " + (currentX-startX0));
    if(mode==="page") {
      if (currentX - startX0 < -1) {
        nextPage();
      } else if (currentX - startX0 > 1) {
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
    // console.log("count: " + count)

    if(count != 0){
      gapX = currentX - positionPrevX;
      gapY = currentY - positionPrevY;
      gap = Math.sqrt(gapX**2 + gapY**2);
      // console.log("gapX,gapY: " + gapX + ", " + gapY + ",\n" + currentX + "," + positionPrevX + ",\n" + currentY + "," + positionPrevY);

      gapRX = (curPosX - posPrevX);
      gapRY = (curPosY - posPrevY);
      gapR = Math.sqrt(gapRX**2 + gapRY**2);
      // console.log("gapRX,gapRY: " + gapRX + ", " + gapRY + ",\n" + curPosX + "," + posPrevX + ",\n" + curPosY + "," + posPrevY);


      nowTime = performance.now();
      msec = nowTime - previousTime;
      // console.log("previousTime：" + previousTime + "\nnowTime：" + nowTime);

      previousTime = nowTime;
      // console.log("msec: " + msec);
      // console.log("endTime：" + endTime + "\nstartTime：" + startTime + "\npreviousTime：" + previousTime + "\nnowTime：" + nowTime);
      

      velX = gapX / msec;
      velY = gapY / msec;
      vel = gap / msec;
      velRX = gapRX / msec;
      velRY = gapRY / msec;
      velR = gapR / msec;


      accelerationX = (velX - preVelX) / msec;
      accelerationY = (velY - preVelY) / msec;
      acceleration = (vel - preVel) / msec;
      accelerationRX = (velRX - preVelRX) / msec;
      accelerationRY = (velRY - preVelRY) / msec;
      accelerationR = (velR - preVelR) / msec;


      // console.log("print\n" + msec + "," + pressure + "," + gapX + ", " + gapY + "," + currentX + ", " + positionPrevX + "," + currentY + ", " + positionPrevY);
      if(count > 1) {
        strMid += pressure + "," + gapX + "," + gapY + "," + gap + "," + gapRX + "," + gapRY + "," + gapR + "," + velX + "," + velY + "," + vel + "," + velRX + "," + velRY + "," + velR + "," + accelerationX + "," + accelerationY + "," + acceleration + "," + accelerationRX + "," + accelerationRY + "," + accelerationR + "," + currentX + "," + currentY + "," + msec + "," + nowTime + "," + (nowTime-endTime) + "," + count + "," + mode +"\n";
        VelX.push(velX);
        VelY.push(velY);
        Vel.push(vel);
        VelRX.push(velRX);
        VelRY.push(velRY);
        VelR.push(velR);
        AccelerationX.push(accelerationX);
        AccelerationY.push(accelerationY);
        Acceleration.push(acceleration);
        AccelerationRX.push(accelerationRX);
        AccelerationRY.push(accelerationRY);
        AccelerationR.push(accelerationR);
        Pressure.push(pressure);
        PositionX.push(currentX);
        PositionY.push(currentY);
        PositionRX.push(curPosX);
        PositionRY.push(curPosY);
      }
      if(count === 1) {
        $(function(){
          console.log("IIIII")
        
          $.ajax({
              url: 'cgi-bin/open_model_Initial.py',
              type: 'get',
              dataType: 'json',
              data: {
                // 最低限ver
                pressure0: pressure0, intervalTime: (endTime-startTime), gapX: gapX, gapY: gapY, gap: gap, gapRY: gapRY, gapR: gapR, velRX: velRX, accelerationR: accelerationR, posX: currentX, posY: currentY

                // test1: pressure0,
                // test2: (endTime-startTime),
                // test3: gapX, test4: gapY, test5: gap,
                // test6: gapRX, test7: gapRY, test8: gapR,
                // test9: velX, test10: velY, test11: vel,
                // test12: velRX, test13: velRY, test14: velR,
                // test15: accelerationX, test16: accelerationY, test17: acceleration,
                // test18: accelerationRX, test19: accelerationRY, test20: accelerationR,
                // test21: currentX, test22: currentY, 
                // test23: (nowTime-endTime)
              }
          }).done(function(dataI){
            console.log(dataI)
            const ans_If = dataI.ans_If;
            const ans_Ip = dataI.ans_Ip;
            const ans_Im = dataI.ans_Im;              
            if(ans_If[0] === 'page') {
              console.log("ページめくり")
              res4 = "ページめくり"
              $('#JudgeText_If').css('color', 'blue');
            } else if(ans_If[0] === 'pen') {
              console.log("書き込み")
              res4 = "書き込み"
              $('#JudgeText_If').css('color', 'red');
            }
            if(ans_Ip[0] === 'page') {
              console.log("ページめくり")
              res5 = "ページめくり"
              $('#JudgeText_Ip').css('color', 'blue');
            } else if(ans_Ip[0] === 'pen') {
              console.log("書き込み")
              res5 = "書き込み"
              $('#JudgeText_Ip').css('color', 'red');
            }
            if(ans_Im[0] === 'page') {
              console.log("ページめくり")
              res6 = "ページめくり"
              $('#JudgeText_Im').css('color', 'blue');
            } else if(ans_Im[0] === 'pen') {
              console.log("書き込み")
              res6 = "書き込み"
              $('#JudgeText_Im').css('color', 'red');
            }
            strInitialModel += mode + "," + ans_If[0] + "," + ans_Ip[0] + "," + ans_Im[0] + "," + dragCountI + "\n"
            console.log("strInitialModel: " + strInitialModel)
            // テキストを変更
            $('#Judge_CountI').text(dragCountI);
            $('#JudgeText_If').text(res4);
            $('#JudgeText_Ip').text(res5);
            $('#JudgeText_Im').text(res6);
            console.log(dragCountI)
            dragCountI++;
          }).fail(function(){
              console.log('failed');
          });
        });
        strInitial += "," + gapX + "," + gapY + "," + gap + "," + gapRX + "," + gapRY + "," + gapR + "," + velX + "," + velY + "," + vel + "," + velRX + "," + velRY + "," + velR + "," + accelerationX + "," + accelerationY + "," + acceleration + "," + accelerationRX + "," + accelerationRY + "," + accelerationR + "," + currentX + "," + currentY + "," + (nowTime-endTime);
        // str += gapX + "," + gapY + "," + gap + "," + velX + "," + velY + "," + vel + "," + accelerationX + "," + accelerationY + "," + acceleration + "," + currentX + "," + currentY + "," + msec + "," + mode +"\n";
        strMid += pressure0 + "," + gapX + "," + gapY + "," + gap + "," + gapRX + "," + gapRY + "," + gapR + "," + velX + "," + velY + "," + vel + "," + velRX + "," + velRY + "," + velR + "," + accelerationX + "," + accelerationY + "," + acceleration + "," + accelerationRX + "," + accelerationRY + "," + accelerationR + "," + currentX + "," + currentY + "," + (nowTime-endTime) + "," + nowTime + "," + (nowTime-endTime) + "," + count + "," + mode +"\n";
        // str += gapX + "," + gapY + "," + gap + "," + (gapX - preGapX) + "," + (gapY - preGapY) + "," + (gap - preGap) + "," + currentX + "," + currentY + "," + (nowTime-endTime) + "," + mode +"\n";

        // console.log("現： " + (nowTime-endTime));
        // console.log("msec: " + msec);


        VelX.push(velX);
        VelY.push(velY);
        Vel.push(vel);
        VelRX.push(velRX);
        VelRY.push(velRY);
        VelR.push(velR);
        AccelerationX.push(accelerationX);
        AccelerationY.push(accelerationY);
        Acceleration.push(acceleration);
        AccelerationRX.push(accelerationRX);
        AccelerationRY.push(accelerationRY);
        AccelerationR.push(accelerationR);
        Pressure.push(pressure0);
        PositionX.push(currentX);
        PositionY.push(currentY);
        PositionRX.push(curPosX);
        PositionRY.push(curPosY);
        // stroke.push(currentX, currentY, velX, velY, vel, accelerationX, accelerationY, acceleration, pressure)
      }
      // dpoint0 = point;

      // console.log("count-previous: " + positionPrevX + ", " + positionPrevY);

      // console.log("count:" + count + "\ngap：" + gapX + ", " + gapY);
      
      // console.log("count-previous: " + positionPrevX + ", " + positionPrevY);
      // console.log("count-current: " + currentX + ", " + currentY);
      // console.log("acceleration: " + acceleration + ", " + accelerationX + ", " + accelerationY);

      positionPrevX = currentX;
      positionPrevY = currentY;
      posPrevX = curPosX;
      posPrevY = curPosY;

      preGapX = gapX;
      preGapY = gapY;
      preGap = gap;
      preGapRX = gapRX;
      preGapRY = gapRY;
      preGapR = gapR;

      preVelX = velX;
      preVelY = velY;
      preVel = vel;
      preVelRX = velRX;
      preVelRY = velRY;
      preVelR = velR;

    }
    
    
    
    count++;


    // var start = Date.now();
    // var now = performance.now();
    // console.log("時間1：" + start);
    // console.log("時間2：" + now);
  

    // 10ミリ秒後に再度関数を実行
    // setTimeout(speedCount, 10);
    // intervalId = window.setInterval(speedCount, 10);

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
  $('#dl-Ini').on('click', function() {    downloadI("Ini");  });
  $('#dl-Fin').on('click', function() {    downloadF("Fin");  });
  function downloadI(filename) {
    // csvファイルへの書き出し
    // 初動判別用のデータファイル
    var blob2 = new Blob([strInitialModel],{type:"text/csv"}); //配列に上記の文字列(strInitial)を設定
    var link2 = document.createElement('a');
    link2.href = URL.createObjectURL(blob2);
    link2.download = filename +  "_Model_res.csv";
    link2.click();
  }
  function downloadF(filename) {  
    // ドラッグ終了時判別用のデータファイル
    var blob = new Blob([strFinalModel],{type:"text/csv"}); //配列に上記の文字列(strFinal)を設定
    var link = document.createElement('a');
    link.href = URL.createObjectURL(blob);
    link.download = filename +  "_Model_res.csv";
    link.click();
  }

  

  $('#section-button').on('click', function() {
    strInitial += "\n";
    strMid += "\n";
    strFinal += "\n";
  });


   
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
    { background: '/img/page1.jpg', drawings: [] },
    { background: '/img/page2.jpg', drawings: [] },
    { background: '/img/page3.jpg', drawings: [] },
    { background: '/img/page4.jpg', drawings: [] },
    { background: '/img/page5.jpg', drawings: [] },
    { background: '/img/page6.jpg', drawings: [] },
    { background: '/img/page7.jpg', drawings: [] },
    { background: '/img/page8.jpg', drawings: [] },
    { background: '/img/page9.jpg', drawings: [] },
    { background: '/img/page10.jpg', drawings: [] },
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
