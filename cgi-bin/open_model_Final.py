#!/usr/bin/python3
# -*- coding: utf-8 -*-


######################################################
# 保存した終了時判別モデルを使用し、判定結果を出力するプログラム
######################################################

import cgi
import json
import numpy as np

# jsから値を受け取る
storage = cgi.FieldStorage()

# print("Content-Type: application/json")
print('Content-type: text/html\n')

# # Finalの場合 ####################################
## 元データを使用する場合 #################
vel_max = float(storage.getvalue('vel_max'))
vel_median = float(storage.getvalue('vel_median'))
velRX_min = float(storage.getvalue('velRX_min'))
velRX_mean = float(storage.getvalue('velRX_mean'))
velRX_median = float(storage.getvalue('velRX_median'))
velRX_last = float(storage.getvalue('velRX_last'))
velRY_last = float(storage.getvalue('velRY_last'))
velR_mean = float(storage.getvalue('velR_mean'))
velR_median = float(storage.getvalue('velR_median'))
velR_last = float(storage.getvalue('velR_last'))
accelerationX_max = float(storage.getvalue('accelerationX_max'))
acceleration_max = float(storage.getvalue('acceleration_max'))
acceleration_mean = float(storage.getvalue('acceleration_mean'))
accelerationRX_max = float(storage.getvalue('accelerationRX_max'))
accelerationR_min = float(storage.getvalue('accelerationR_min'))
accelerationR_median = float(storage.getvalue('accelerationR_median'))
accelerationR_first = float(storage.getvalue('accelerationR_first'))
widthRX = float(storage.getvalue('widthRX'))


import pickle

# モデルのオープン
with open('model_f_Final.pickle', mode='rb') as f1:
    model_f = pickle.load(f1)

with open('model_p_Final.pickle', mode='rb') as f2:
    model_p = pickle.load(f2)

with open('model_m_Final.pickle', mode='rb') as f3:
    model_m = pickle.load(f3)
    

data_f = np.array( [[velRX_min, velRX_mean, velR_mean, velR_median, velR_last, accelerationX_max, acceleration_max, widthRX]] )
ans_f = model_f.predict(data_f)
# print(ans_f)

 
data_p = np.array( [[vel_median, velRX_mean, velRX_median, velRX_last, velRY_last, velR_last, acceleration_max, acceleration_mean, accelerationRX_max, accelerationR_min, accelerationR_median, accelerationR_first, widthRX]] )
ans_p = model_p.predict(data_p)
# print(ans_p)

data_m = np.array( [[vel_max, velRX_min, velRX_mean, velRX_median, velR_median, velR_last, accelerationR_median, widthRX]] )
ans_m = model_m.predict(data_m)
# print(ans_m)

# result_data = [ans_f, ans_p, ans_m]
# print(result_data)
result_data = {
    'ans_f': ans_f.tolist(), 'ans_p': ans_p.tolist(), 'ans_m': ans_m.tolist()
}

json_str = json.dumps(result_data)

print(json_str)















# import cgi
# import json
# import numpy as np

# # jsから値を受け取る
# storage = cgi.FieldStorage()
# # CGIヘッダーを出力
# print("Content-Type: application/json")

# # Finalの場合 ####################################
# ## 元データを使用する場合 #################
# vel_max = float(storage.getvalue('vel_max'))
# vel_median = float(storage.getvalue('vel_median'))
# velRX_min = float(storage.getvalue('velRX_min'))
# velRX_mean = float(storage.getvalue('velRX_mean'))
# velRX_median = float(storage.getvalue('velRX_median'))
# velRX_last = float(storage.getvalue('velRX_last'))
# velRY_last = float(storage.getvalue('velRY_last'))
# velR_mean = float(storage.getvalue('velR_mean'))
# velR_median = float(storage.getvalue('velR_median'))
# velR_last = float(storage.getvalue('velR_last'))
# accelerationX_max = float(storage.getvalue('accelerationX_max'))
# acceleration_max = float(storage.getvalue('acceleration_max'))
# acceleration_mean = float(storage.getvalue('acceleration_mean'))
# accelerationRX_max = float(storage.getvalue('accelerationRX_max'))
# accelerationR_min = float(storage.getvalue('accelerationR_min'))
# accelerationR_median = float(storage.getvalue('accelerationR_median'))
# accelerationR_first = float(storage.getvalue('accelerationR_first'))
# widthRX = float(storage.getvalue('widthRX'))


# import pickle

# # モデルのオープン
# with open('model_f_Final.pickle', mode='rb') as f1:
#     model_f = pickle.load(f1)

# with open('model_p_Final.pickle', mode='rb') as f2:
#     model_p = pickle.load(f2)

# with open('model_m_Final.pickle', mode='rb') as f3:
#     model_m = pickle.load(f3)
    

# data_f = np.array( [[velRX_min, velRX_mean, velR_mean, velR_median, velR_last, accelerationX_max, acceleration_max, widthRX]] )
# ans_f = model_f.predict(data_f)
# # print(ans_f)
 
# data_p = np.array( [[vel_median, velRX_mean, velRX_median, velRX_last, velRY_last, velR_last, acceleration_max, acceleration_mean, accelerationRX_max, accelerationR_min, accelerationR_median, accelerationR_first, widthRX]] )
# ans_p = model_p.predict(data_p)
# # print(ans_p)

# data_m = np.array( [[vel_max, velRX_min, velRX_mean, velRX_median, velR_median, velR_last, accelerationR_median, widthRX]] )
# ans_m = model_m.predict(data_m)
# # print(ans_m)


# # 例: クライアントに返すデータ
# response_data = {'ans_f': ans_f, 'ans_p': ans_p, 'ans_m': ans_m}
# # json_response_data = response_data.tolist()

# # # print()
# # print(json.dumps(json_response_data))

# # NumPy配列をリストに変換する関数
# def convert_to_list(item):
#     if isinstance(item, np.ndarray):
#         return item.tolist()
#     else:
#         return item

# # 辞書内の各要素についてNumPy配列をリストに変換
# json_response_data = {key: convert_to_list(value) for key, value in response_data.items()}
# print("************************" + response_data)
# print(json_response_data)

# # JSONシリアライズ
# print(json.dumps(json_response_data))









# import cgi
# import numpy as np

# # jsから値を受け取る
# storage = cgi.FieldStorage()
# print('Content-type: text/html\n')

# # Finalの場合 ####################################
# ## 元データを使用する場合 #################
# vel_max = float(storage.getvalue('vel_max'))
# vel_median = float(storage.getvalue('vel_median'))
# velRX_min = float(storage.getvalue('velRX_min'))
# velRX_mean = float(storage.getvalue('velRX_mean'))
# velRX_median = float(storage.getvalue('velRX_median'))
# velRX_last = float(storage.getvalue('velRX_last'))
# velRY_last = float(storage.getvalue('velRY_last'))
# velR_mean = float(storage.getvalue('velR_mean'))
# velR_median = float(storage.getvalue('velR_median'))
# velR_last = float(storage.getvalue('velR_last'))
# accelerationX_max = float(storage.getvalue('accelerationX_max'))
# acceleration_max = float(storage.getvalue('acceleration_max'))
# acceleration_mean = float(storage.getvalue('acceleration_mean'))
# accelerationRX_max = float(storage.getvalue('accelerationRX_max'))
# accelerationR_min = float(storage.getvalue('accelerationR_min'))
# accelerationR_median = float(storage.getvalue('accelerationR_median'))
# accelerationR_first = float(storage.getvalue('accelerationR_first'))
# widthRX = float(storage.getvalue('widthRX'))


# import pickle

# # モデルのオープン
# with open('model_f_Final.pickle', mode='rb') as f1:
#     model_f = pickle.load(f1)

# with open('model_p_Final.pickle', mode='rb') as f2:
#     model_p = pickle.load(f2)

# with open('model_m_Final.pickle', mode='rb') as f3:
#     model_m = pickle.load(f3)
    

# data_f = np.array( [[velRX_min, velRX_mean, velR_mean, velR_median, velR_last, accelerationX_max, acceleration_max, widthRX]] )
# ans_f = model_f.predict(data_f)
# print(ans_f)

 
# data_p = np.array( [[vel_median, velRX_mean, velRX_median, velRX_last, velRY_last, velR_last, acceleration_max, acceleration_mean, accelerationRX_max, accelerationR_min, accelerationR_median, accelerationR_first, widthRX]] )
# ans_p = model_p.predict(data_p)
# print(ans_p)

# data_m = np.array( [[vel_max, velRX_min, velRX_mean, velRX_median, velR_median, velR_last, accelerationR_median, widthRX]] )
# ans_m = model_m.predict(data_m)
# print(ans_m)