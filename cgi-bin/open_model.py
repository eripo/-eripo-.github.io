#!/usr/bin/python3
# -*- coding: utf-8 -*-


######################################################
# 保存したモデルを使用し、判定結果を出力するプログラム
######################################################
import cgi

# jsから値を受け取る
storage = cgi.FieldStorage()
print('Content-type: text/html\n')

test1 = float(storage.getvalue('test1'))
test2 = float(storage.getvalue('test2'))
test3 = float(storage.getvalue('test3'))
test4 = float(storage.getvalue('test4'))

import pickle


# モデルのオープン
with open('model.pickle', mode='rb') as f:
    model = pickle.load(f)

# 評価データ ここにその都度入ってきたデータを入れる。
# data = [[0.979492, -6.687562, 1.180157, 6.790895]]
data = [[test1, test2, test3, test4]]

# モデルを用いた予測
ans = model.predict(data)

 
# # 予測結果を出力
# print("予測対象：\n", data, ", \n予測結果→", ans)
print(ans)
