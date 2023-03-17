
// 配列に値を入れていく
// var verocity =["v_x","v_y","v"];
// var TempData =[];
// TempData.push(verocity);


var vpoint = Array(0, 0);

// csvへの書き出し
var str = "";
str += "v_x" + "," + "v_y" + "," + "v" + "\n";  // 1行目
// var len_columns =Object.keys(TempData[0]).length;


// 2行目以降のデータ書き出し
var r = 0;
while(r<30) {
    vpoint[0] = r;
    vpoint[1] = r+1;
    str += vpoint[0] + "," + vpoint[1] + "," + "" + "\n";
    console.log(vpoint[0] + ":" + vpoint[1] + "\n");
    r++;
}


var blob =new Blob([str],{type:"text/csv"}); //配列に上記の文字列(str)を設定
var link =document.createElement('a');
link.href = URL.createObjectURL(blob);
link.download ="test.csv";
link.click();

