#!/usr/bin/python3
# -*- coding: utf-8 -*-


######################################################
# 保存したモデルを使用し、判定結果を出力するプログラム
######################################################
import cgi

# jsから値を受け取る
storage = cgi.FieldStorage()
print('Content-type: text/html\n')

# Finalの場合 ####################################
test1 = float(storage.getvalue('test1'))
test2 = float(storage.getvalue('test2'))
test3 = float(storage.getvalue('test3'))
test4 = float(storage.getvalue('test4'))
test5 = float(storage.getvalue('test5'))
test6 = float(storage.getvalue('test6'))
test7 = float(storage.getvalue('test7'))
test8 = float(storage.getvalue('test8'))
test9 = float(storage.getvalue('test9'))
test10 = float(storage.getvalue('test10'))
test11 = float(storage.getvalue('test11'))
test12 = float(storage.getvalue('test12'))
test13 = float(storage.getvalue('test13'))
test14 = float(storage.getvalue('test14'))
test15 = float(storage.getvalue('test15'))
test16 = float(storage.getvalue('test16'))
test17 = float(storage.getvalue('test17'))
test18 = float(storage.getvalue('test18'))
test19 = float(storage.getvalue('test19'))
test20 = float(storage.getvalue('test20'))
test21 = float(storage.getvalue('test21'))
test22 = float(storage.getvalue('test22'))
test23 = float(storage.getvalue('test23'))
test24 = float(storage.getvalue('test24'))
test25 = float(storage.getvalue('test25'))
test26 = float(storage.getvalue('test26'))
test27 = float(storage.getvalue('test27'))
test28 = float(storage.getvalue('test28'))
test29 = float(storage.getvalue('test29'))
test30 = float(storage.getvalue('test30'))
test31 = float(storage.getvalue('test31'))
test32 = float(storage.getvalue('test32'))
test33 = float(storage.getvalue('test33'))
test34 = float(storage.getvalue('test34'))
test35 = float(storage.getvalue('test35'))
test36 = float(storage.getvalue('test36'))
test37 = float(storage.getvalue('test37'))
test38 = float(storage.getvalue('test38'))
test39 = float(storage.getvalue('test39'))
test40 = float(storage.getvalue('test40'))
test41 = float(storage.getvalue('test41'))
test42 = float(storage.getvalue('test42'))
test43 = float(storage.getvalue('test43'))
test44 = float(storage.getvalue('test44'))
test45 = float(storage.getvalue('test45'))
test46 = float(storage.getvalue('test46'))
test47 = float(storage.getvalue('test47'))
test48 = float(storage.getvalue('test48'))
test49 = float(storage.getvalue('test49'))
test50 = float(storage.getvalue('test50'))
test51 = float(storage.getvalue('test51'))
test52 = float(storage.getvalue('test52'))
test53 = float(storage.getvalue('test53'))
test54 = float(storage.getvalue('test54'))
test55 = float(storage.getvalue('test55'))
test56 = float(storage.getvalue('test56'))
test57 = float(storage.getvalue('test57'))
test58 = float(storage.getvalue('test58'))
test59 = float(storage.getvalue('test59'))
test60 = float(storage.getvalue('test60'))
test61 = float(storage.getvalue('test61'))
test62 = float(storage.getvalue('test62'))
test63 = float(storage.getvalue('test63'))
test64 = float(storage.getvalue('test64'))
test65 = float(storage.getvalue('test65'))
test66 = float(storage.getvalue('test66'))
test67 = float(storage.getvalue('test67'))
test68 = float(storage.getvalue('test68'))
test69 = float(storage.getvalue('test69'))
test70 = float(storage.getvalue('test70'))
test71 = float(storage.getvalue('test71'))
test72 = float(storage.getvalue('test72'))
test73 = float(storage.getvalue('test73'))
test74 = float(storage.getvalue('test74'))
test75 = float(storage.getvalue('test75'))
test76 = float(storage.getvalue('test76'))
test77 = float(storage.getvalue('test77'))
test78 = float(storage.getvalue('test78'))
test79 = float(storage.getvalue('test79'))
test80 = float(storage.getvalue('test80'))
test81 = float(storage.getvalue('test81'))
test82 = float(storage.getvalue('test82'))
test83 = float(storage.getvalue('test83'))
test84 = float(storage.getvalue('test84'))
test85 = float(storage.getvalue('test85'))
test86 = float(storage.getvalue('test86'))
test87 = float(storage.getvalue('test87'))
test88 = float(storage.getvalue('test88'))
test89 = float(storage.getvalue('test89'))
test90 = float(storage.getvalue('test90'))
test91 = float(storage.getvalue('test91'))
test92 = float(storage.getvalue('test92'))
test93 = float(storage.getvalue('test93'))
test94 = float(storage.getvalue('test94'))
test95 = float(storage.getvalue('test95'))
test96 = float(storage.getvalue('test96'))
test97 = float(storage.getvalue('test97'))
test98 = float(storage.getvalue('test98'))
test99 = float(storage.getvalue('test99'))
test100 = float(storage.getvalue('test100'))
test101 = float(storage.getvalue('test101'))
test102 = float(storage.getvalue('test102'))
test103 = float(storage.getvalue('test103'))
test104 = float(storage.getvalue('test104'))
test105 = float(storage.getvalue('test105'))
test106 = float(storage.getvalue('test106'))
test107 = float(storage.getvalue('test107'))
test108 = float(storage.getvalue('test108'))
test109 = float(storage.getvalue('test109'))
test110 = float(storage.getvalue('test110'))
test111 = float(storage.getvalue('test111'))
test112 = float(storage.getvalue('test112'))
test113 = float(storage.getvalue('test113'))
test114 = float(storage.getvalue('test114'))
test115 = float(storage.getvalue('test115'))
test116 = float(storage.getvalue('test116'))
test117 = float(storage.getvalue('test117'))
test118 = float(storage.getvalue('test118'))
test119 = float(storage.getvalue('test119'))



import pickle

# モデルのオープン
with open('model_Final.pickle', mode='rb') as f:
    model = pickle.load(f)

# 評価データ ここにその都度入ってきたデータを入れる。
# data = [[0.979492, -6.687562, 1.180157, 6.790895]]
data = [
    [test1, test2, test3, test4, test5, test6, test7, test8, test9, test10,
    test11, test12, test13, test14, test15, test16, test17, test18, test19, test20,
    test21, test22, test23, test24, test25, test26, test27, test28, test29, test30,
    test31, test32, test33, test34, test35, test36, test37, test38, test39, test40,
    test41, test42, test43, test44, test45, test46, test47, test48, test49, test50,
    test51, test52, test53, test54, test55, test56, test57, test58, test59, test60,
    test61, test62, test63, test64, test65, test66, test67, test68, test69, test70,
    test71, test72, test73, test74, test75, test76, test77, test78, test79, test80,
    test81, test82, test83, test84, test85, test86, test87, test88, test89, test90,
    test91, test92, test93, test94, test95, test96, test97, test98, test99, test100,
    test101, test102, test103, test104, test105, test106, test107, test108, test109, test110,
    test111, test112, test113, test114, test115, test116, test117, test118, test119]
]



# モデルを用いた予測
ans = model.predict(data)

 
# # 予測結果を出力
# print("予測対象：\n", data, ", \n予測結果→", ans)
print(ans)
