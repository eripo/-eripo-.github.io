#!/usr/bin/python3
# -*- coding: utf-8 -*-


######################################################
# 保存した初動判別モデルを使用し、判定結果を出力するプログラム
######################################################

import cgi
import json
import numpy as np

# jsから値を受け取る
storage = cgi.FieldStorage()

# print("Content-Type: application/json")
print('Content-type: text/html\n')

# Initialの場合 ####################################
## 元データを使用する場合 #################
pressure0 = float(storage.getvalue('pressure0'))
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
# with open('model_f_Initial.pickle', mode='rb') as f1:
#     model_f = pickle.load(f1)

# with open('model_p_Initial.pickle', mode='rb') as f2:
#     model_p = pickle.load(f2)

with open('model_m_Initial.pickle', mode='rb') as f3:
    model_m = pickle.load(f3)


# data_f = np.array( [[intervalTime, gapY, gapR, velRX, accelerationR, posX, posY]] )
# ans_f = model_f.predict(data_f)
 
# data_p = np.array( [[pressure0, intervalTime, gapX, gap, gapRY, posX, posY]] )
# ans_p = model_p.predict(data_p)

data_m = np.array( [[intervalTime, gapX, gap, gapRY, accelerationR, posX, posY]] )
ans_m = model_m.predict(data_m)


result_data = {
    # 'ans_If': ans_f.tolist(), 
    # 'ans_Ip': ans_p.tolist(), 
    'ans_Im': ans_m.tolist()
}

json_str = json.dumps(result_data)

print(json_str)