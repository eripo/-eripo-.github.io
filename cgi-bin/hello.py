#!/usr/bin/python3
# -*- coding: utf-8 -*-


######################################################
# 保存した終了時判別モデルを使用し、判定結果を出力するプログラム
######################################################

import numpy as np
import pandas as pd
import math

# # Finalの場合 ####################################
## 元データを使用する場合 #################
df2 = pd.read_csv( 'Data/all_tasks/all_mf_Final.csv' )
# df2 = pd.read_csv( 'Data/fm_Initial/fm_Initial16EK.csv' )
# print(df2)
df3 = df2.dropna(how='any')

# 特徴量選択
## fm_Initial向け ##
# test0 = df3[['intervalTime', 'gapY', 'gapR', 'velRX', 'accelerationR', 'posX','posY','Mode']]
## pm_Initial向け ##
# test0 = df3[['pressure0', 'intervalTime', 'gapX', 'gap', 'gapRY', 'posX', 'posY','Mode']]
## mm_Initial向け ##
# test0 = df3[['intervalTime', 'gapX', 'gap', 'gapRY', 'accelerationR', 'posX','posY','Mode']]

## fm_Final向け ##
# test0 = df3[['velRX_min', 'velRX_mean', 'velR_mean', 'velR_median', 'velR_last','accelerationX_max', 'acceleration_max', 'widthRX','Mode']]
## pm_Final向け ##
# test0 = df3[['vel_median', 'velRX_mean', 'velRX_median', 'velRX_last', 'velRY_last','velR_last', 'acceleration_max', 'acceleration_mean','accelerationRX_max', 'accelerationR_min', 'accelerationR_median','accelerationR_first', 'widthRX','Mode']]
## mm_Final向け ##
test0 = df3[['vel_max', 'velRX_min', 'velRX_mean', 'velRX_median', 'velR_median','velR_last', 'accelerationR_median', 'widthRX','Mode']]

test_data = test0.drop(['Mode'],axis=1)
test_label = df3['Mode']

test_class_counts = {label: sum(test_label == label) for label in set(test_label)}

print('テスト用データの各クラス数 : ')
print(test_class_counts)


import pickle

# モデルのオープン
# with open('model_f_Final.pickle', mode='rb') as f1:
#     model_f = pickle.load(f1)

# with open('model_p_Final.pickle', mode='rb') as f2:
#     model_p = pickle.load(f2)

with open('model_m_Final.pickle', mode='rb') as f3:
    model_m = pickle.load(f3)
    

# data_f = np.array( [[velRX_min, velRX_mean, velR_mean, velR_median, velR_last, accelerationX_max, acceleration_max, widthRX]] )
# ans_f = model_f.predict(data_f)

# data_p = np.array( [[vel_median, velRX_mean, velRX_median, velRX_last, velRY_last, velR_last, acceleration_max, acceleration_mean, accelerationRX_max, accelerationR_min, accelerationR_median, accelerationR_first, widthRX]] )
# ans_p = model_p.predict(data_p)

ans_m = model_m.predict(test_data)

print('スコア : %.4f'%(model_m.score(test_data, test_label)))

from sklearn.metrics import confusion_matrix, precision_score, recall_score
# 混同行列
lr_tn, lr_fp, lr_fn, lr_tp = confusion_matrix(test_label, ans_m).ravel()
print('混同行列（元データ） : %d, %d, %d, %d'%(lr_tn, lr_fp, lr_fn, lr_tp));


# 適合率（precision）・再現率（recall）の算出
print('accuracy score : %.4f'%((lr_tp + lr_tn) / (lr_tp + lr_tn + lr_fp + lr_fn)))
print('[pen]_lr_precision : %.4f'%(lr_tp / (lr_tp + lr_fp)))
print('[pen]_lr_recall : %.4f'%(lr_tp / (lr_tp + lr_fn)))
print('[page]_lr_precision : %.4f'%(lr_tn / (lr_tn + lr_fn)))
print('[page]_lr_recall : %.4f'%(lr_tn / (lr_tn + lr_fp)))  
print('MCC : %.4f'%( ((lr_tp*lr_tn)-(lr_fp*lr_fn)) / math.sqrt((lr_tp+lr_fp)*(lr_tp+lr_fn)*(lr_tn+lr_fp)*(lr_tn+lr_fn)) ))

