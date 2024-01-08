#!/usr/bin/python3
# -*- coding: utf-8 -*-


######################################################
# 保存した初動判別モデルを使用し、判定結果を出力するプログラム
######################################################
import cgi
import numpy as np

# jsから値を受け取る
storage = cgi.FieldStorage()
print('Content-type: text/html\n')

# Initialの場合 ####################################
## 元データを使用する場合 #################
pressure0 = float(storage.getvalue('pressure0'))
print(pressure0)
intervalTime = float(storage.getvalue('intervalTime'))
gapX = float(storage.getvalue('gapX'))
gapY = float(storage.getvalue('gapY'))
gap = float(storage.getvalue('gap'))
gapRY = float(storage.getvalue('gapRY'))
gapR = float(storage.getvalue('gapR'))
velRX = float(storage.getvalue('velRX'))
accelerationR = float(storage.getvalue('accelerationR'))
posX = float(storage.getvalue('posX'))
posY = float(storage.getvalue('posY'))


import pickle

# モデルのオープン
with open('model_f_Initial.pickle', mode='rb') as f1:
    model_f = pickle.load(f1)

with open('model_p_Initial.pickle', mode='rb') as f2:
    model_p = pickle.load(f2)

with open('model_m_Initial.pickle', mode='rb') as f3:
    model_m = pickle.load(f3)
    
    
    

# 適用時: スケーリングパラメータを読み込む
# with open('scaling_parameters_Initial.pkl', 'rb') as file:
#     scaling_params = pickle.load(file)

# mean_value = scaling_params['mean']
# std_deviation = scaling_params['std']
# print(mean_value)
# print(std_deviation)


# 評価データ ここにその都度入ってきたデータを入れる。
# data = [[0.66015625,855.6999999284744,-6.4000244140625,-0.79998779296875,6.44982891009483,-6.4000244140625,-0.79998779296875,6.44982891009483,-0.40764486589964827,-0.05095463634006647,0.4108171267837925,-0.40764486589964827,-0.05095463634006647,0.4108171267837925,-0.025964641061245713,-0.0032455182283635735,0.02616669589401702,-0.025964641061245713,-0.0032455182283635735,0.02616669589401702,639.6374969482422,388.20001220703125,15.700000047683716],
#         [0.7265625,4745.899999976158,-18.39996337890625,-0.800018310546875,18.41734730199497,-18.39996337890625,-0.79998779296875,18.417345976388404,-1.6576543548995217,-0.07207372151608141,1.6592204740933396,-1.6576543548995217,-0.07207097218472469,1.6592203546693252,-0.14933822985036224,-0.006493128050565151,0.14947932166932207,-0.14933822985036224,-0.006492880363056068,0.14947931091040187,562.0375213623047,463.3999938964844,11.100000023841858],
#         [0.3564453125,10433.100000023842,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,526.8375091552734,461.8000183105469,11.899999976158142],
#         [0.25390625,138,-0.79998779296875,-0.800048828125,1.1313967457453629,-0.79998779296875,-0.800048828125,1.1313967457453629,-0.06779557594927924,-0.06780074842016878,0.09588108053536687,-0.06779557594927924,-0.06780074842016878,0.09588108053536687,-0.00574538781552887,-0.005745826160521282,0.00812551533244251,-0.00574538781552887,-0.005745826160521282,0.00812551533244251,550.8375091552734,437.8000183105469,11.799999952316284],
#         [0.2158203125,111.10000002384186,-0.79998779296875,0,0.79998779296875,-0.79998779296875,0,0.79998779296875,-0.07079538020748113,0,0.07079538020748113,-0.07079538020748113,0,0.07079538020748113,-0.00626507792090472,0,0.00626507792090472,-0.00626507792090472,0,0.00626507792090472,566.0375213623047,477.8000183105469,11.299999952316284]
#         ]
# data = np.array( [[test1, test2, test3, test4, test5, test6, test7, test8, test9, test10, test11, test12, test13, test14, test15, test16, test17, test18, test19, test20, test21, test22, test23]] )

## データを標準化する処理 ##########
# from sklearn.preprocessing import StandardScaler,MinMaxScaler
# stdsc = StandardScaler()
# test_data = ( data - mean_value ) / std_deviation
# test2_data = stdsc.transform(data)

# # 予測結果を出力
# print("予測対象：\n", data, ", \n予測結果→", ans)
# print(test_data)
# print(test2_data)


data_f = np.array( [[intervalTime, gapY, gapR, velRX, accelerationR, posX, posY]] )
ans_f = model_f.predict(data_f)
print(ans_f)
 
data_p = np.array( [[pressure0, intervalTime, gapX, gap, gapRY, posX, posY]] )
ans_p = model_p.predict(data_p)
print(ans_p)

data_m = np.array( [[intervalTime, gapX, gap, gapRY, accelerationR, posX, posY]] )
ans_m = model_m.predict(data_m)
print(ans_m)