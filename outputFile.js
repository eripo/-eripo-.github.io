
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



/* WScriptはブラウザで実行できるものではない！ */
// // Excel内をパース
// var CSVStr = "";
// var r = 0;
// var vpoint = Array(0, 0);
// while(r<30) {
//     var ary = new Array;
//     var c = 0;
//         vpoint[0] = r;
//         vpoint[1] = r+1;
//         var str = vpoint[0] + ":" + vpoint[1];
//         console.log(vpoint[0] + ":" + vpoint[1] + "\n");
//         ary.push(str);
//     CSVStr += ary.join(",") + "\n";
//     r++;
// }

// // ファイルに書き込み
// var fs = WScript.CreateObject("Scripting.FileSystemObject");
// fs.CreateTextFile("table.csv");
// var file = fs.OpenTextFile("table.csv", 2, true,0);
// file.Write(CSVStr);
// file.Close();