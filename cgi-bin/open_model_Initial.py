#!/usr/bin/python3
# -*- coding: utf-8 -*-


######################################################
# 保存したモデルを使用し、判定結果を出力するプログラム
######################################################
import cgi
import numpy as np

# jsから値を受け取る
storage = cgi.FieldStorage()
print('Content-type: text/html\n')

# Initialの場合 ####################################
## 元データを使用する場合 #################
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


# 適用時: スケーリングパラメータを読み込む
with open('scaling_parameters_Initial.pkl', 'rb') as file:
    scaling_params = pickle.load(file)

mean_value = scaling_params['mean']
std_deviation = scaling_params['std']
# print(mean_value)
# print(std_deviation)


# 評価データ ここにその都度入ってきたデータを入れる。
# data = [[0.66015625,855.6999999284744,-6.4000244140625,-0.79998779296875,6.44982891009483,-6.4000244140625,-0.79998779296875,6.44982891009483,-0.40764486589964827,-0.05095463634006647,0.4108171267837925,-0.40764486589964827,-0.05095463634006647,0.4108171267837925,-0.025964641061245713,-0.0032455182283635735,0.02616669589401702,-0.025964641061245713,-0.0032455182283635735,0.02616669589401702,639.6374969482422,388.20001220703125,15.700000047683716],
#         [0.7265625,4745.899999976158,-18.39996337890625,-0.800018310546875,18.41734730199497,-18.39996337890625,-0.79998779296875,18.417345976388404,-1.6576543548995217,-0.07207372151608141,1.6592204740933396,-1.6576543548995217,-0.07207097218472469,1.6592203546693252,-0.14933822985036224,-0.006493128050565151,0.14947932166932207,-0.14933822985036224,-0.006492880363056068,0.14947931091040187,562.0375213623047,463.3999938964844,11.100000023841858],
#         [0.3564453125,10433.100000023842,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,526.8375091552734,461.8000183105469,11.899999976158142],
#         [0.25390625,138,-0.79998779296875,-0.800048828125,1.1313967457453629,-0.79998779296875,-0.800048828125,1.1313967457453629,-0.06779557594927924,-0.06780074842016878,0.09588108053536687,-0.06779557594927924,-0.06780074842016878,0.09588108053536687,-0.00574538781552887,-0.005745826160521282,0.00812551533244251,-0.00574538781552887,-0.005745826160521282,0.00812551533244251,550.8375091552734,437.8000183105469,11.799999952316284],
#         [0.2158203125,111.10000002384186,-0.79998779296875,0,0.79998779296875,-0.79998779296875,0,0.79998779296875,-0.07079538020748113,0,0.07079538020748113,-0.07079538020748113,0,0.07079538020748113,-0.00626507792090472,0,0.00626507792090472,-0.00626507792090472,0,0.00626507792090472,566.0375213623047,477.8000183105469,11.299999952316284]
#         ]
data = np.array( [[test1, test2, test3, test4, test5, test6, test7, test8, test9, test10, test11, test12, test13, test14, test15, test16, test17, test18, test19, test20, test21, test22, test23]] )

## データを標準化する処理 ##########
from sklearn.preprocessing import StandardScaler,MinMaxScaler
stdsc = StandardScaler()
test_data = ( data - mean_value ) / std_deviation
# test2_data = stdsc.transform(data)


# モデルを用いた予測
ans = model.predict(test_data)

 
# # 予測結果を出力
# print("予測対象：\n", data, ", \n予測結果→", ans)
# print(test_data)
# print(test2_data)
print(ans)
