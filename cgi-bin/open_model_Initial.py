#!/usr/bin/python3
# -*- coding: utf-8 -*-


######################################################
# 保存したモデルを使用し、判定結果を出力するプログラム
######################################################
import cgi

# jsから値を受け取る
storage = cgi.FieldStorage()
print('Content-type: text/html\n')

# Initialの場合 ####################################
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

import pickle

# モデルのオープン
with open('model_Initial.pickle', mode='rb') as f:
    model = pickle.load(f)

# 評価データ ここにその都度入ってきたデータを入れる。
# data = [[0.979492, -6.687562, 1.180157, 6.790895]]
data = [[test1, test2, test3, test4, test5, test6, test7, test8, test9, test10, test11, test12, test13, test14, test15, test16, test17, test18, test19, test20, test21, test22, test23]]

# モデルを用いた予測
ans = model.predict(data)

 
# # 予測結果を出力
# print("予測対象：\n", data, ", \n予測結果→", ans)
print(ans)
