#############################################
# 6種類の判別モデル構築用プログラム

#############################################

import math
import numpy as np
# from keras.datasets import mnist
# import time
import matplotlib.pyplot as plt
# from PIL import Image
from sklearn.model_selection import train_test_split
# import glob
# import argparse
import pandas as pd
import japanize_matplotlib
import pickle


import csv

from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import accuracy_score

from sklearn.preprocessing import StandardScaler,MinMaxScaler

from sklearn.model_selection import cross_val_score
from sklearn.model_selection import KFold
from sklearn.pipeline import make_pipeline

from sklearn.model_selection import cross_val_predict
from sklearn.metrics import confusion_matrix, precision_score, recall_score


# 学習用データ #
# df = pd.read_csv( 'Data/all_fm_Initial.csv' )
# df = pd.read_csv( 'Data/all_pm_Initial.csv' )
# df = pd.read_csv( 'Data/all_fm_Final.csv' )
# df = pd.read_csv( 'Data/all_pm_Final.csv' )
# df = pd.read_csv( 'Data/all_mm_Initial.csv' )
df = pd.read_csv( 'Data/all_mm_Final.csv' )


# print(df)

df1 = df.dropna(how='any')
# print(df1)
# print("*******************")


# 特徴量選択
## fm_Initial向け ##
# X1 = df1[['intervalTime', 'gapY', 'gapR', 'velRX', 'accelerationR', 'posX','posY','Mode']]

## pm_Initial向け ##
# X1 = df1[['pressure0', 'intervalTime', 'gapX', 'gap', 'gapRY', 'posX', 'posY','Mode']]

## mm_Initial向け ##
# X1 = df1[['intervalTime', 'gapX', 'gap', 'gapRY', 'accelerationR', 'posX','posY','Mode']]

## fm_Final向け ##
# X1 = df1[['velRX_min', 'velRX_mean', 'velR_mean', 'velR_median', 'velR_last','accelerationX_max', 'acceleration_max', 'widthRX','Mode']]

## pm_Final向け ##
# X1 = df1[['vel_median', 'velRX_mean', 'velRX_median', 'velRX_last', 'velRY_last','velR_last', 'acceleration_max', 'acceleration_mean','accelerationRX_max', 'accelerationR_min', 'accelerationR_median','accelerationR_first', 'widthRX','Mode']]

## mm_Final向け ##
X1 = df1[['vel_max', 'velRX_min', 'velRX_mean', 'velRX_median', 'velR_median','velR_last', 'accelerationR_median', 'widthRX','Mode']]


# print(X1);
# X：学習用データ，y：学習用データのラベル
X = X1.drop(['Mode'],axis=1)
y = df1['Mode']
print(X);
print(y);


model = GradientBoostingClassifier()
model.fit(X, y)

############################################################################################################################

# 学習モデルの保存
# 初動用（f:指　p:ペン　m:混合）
# with open('model_f_Initial.pickle', mode='wb') as f:
#     pickle.dump(model, f, protocol=2)
    
# with open('model_p_Initial.pickle', mode='wb') as f:
#     pickle.dump(model, f, protocol=2)

# with open('model_m_Initial.pickle', mode='wb') as f:
#     pickle.dump(model, f, protocol=2)
    
# # 終了時用（f:指　p:ペン　m:混合）
# with open('model_f_Final.pickle', mode='wb') as f:
#     pickle.dump(model, f, protocol=2)
    
# with open('model_p_Final.pickle', mode='wb') as f:
#     pickle.dump(model, f, protocol=2)

with open('model_m_Final.pickle', mode='wb') as f:
    pickle.dump(model, f, protocol=2)



# # 勾配ブースティング（学習用データとテスト用データが別ファイルの場合） ###########################################################

# # df2 = pd.read_csv( 'Data/all_tasks/all_mf_Final.csv' )
# df2 = pd.read_csv( 'Data/fm_Initial/fm_Initial16EK.csv' )
# # print(df2)
# df3 = df2.dropna(how='any')

# # 特徴量選択
# ## fm_Initial向け ##
# test0 = df3[['intervalTime', 'gapY', 'gapR', 'velRX', 'accelerationR', 'posX','posY','Mode']]
# ## pm_Initial向け ##
# # test0 = df3[['pressure0', 'intervalTime', 'gapX', 'gap', 'gapRY', 'posX', 'posY','Mode']]
# ## mm_Initial向け ##
# # test0 = df3[['intervalTime', 'gapX', 'gap', 'gapRY', 'accelerationR', 'posX','posY','Mode']]

# ## fm_Final向け ##
# # test0 = df3[['velRX_min', 'velRX_mean', 'velR_mean', 'velR_median', 'velR_last','accelerationX_max', 'acceleration_max', 'widthRX','Mode']]
# ## pm_Final向け ##
# # test0 = df3[['vel_median', 'velRX_mean', 'velRX_median', 'velRX_last', 'velRY_last','velR_last', 'acceleration_max', 'acceleration_mean','accelerationRX_max', 'accelerationR_min', 'accelerationR_median','accelerationR_first', 'widthRX','Mode']]
# ## mm_Final向け ##
# # test0 = df3[['vel_max', 'velRX_min', 'velRX_mean', 'velRX_median', 'velR_median','velR_last', 'accelerationR_median', 'widthRX','Mode']]

# test_data = test0.drop(['Mode'],axis=1)
# test_label = df3['Mode']

# train_class_counts = {label: sum(y == label) for label in set(y)}
# test_class_counts = {label: sum(test_label == label) for label in set(test_label)}

# print('学習用データの各クラス数 : ')
# print(train_class_counts)
# print('テスト用データの各クラス数 : ')
# print(test_class_counts)


# # for i in range(3):
# model = GradientBoostingClassifier()
# model.fit(X, y)

# # テストデータによる予測.
# result_label = model.predict(test_data)

# print('スコア : %.4f'%(model.score(test_data, test_label)))

# # 混同行列
# # lr_tn, lr_fp, lr_fn, lr_tp = confusion_matrix(test_label, result_label).ravel()
# # print('混同行列（元データ） : %d, %d, %d, %d'%(lr_tn, lr_fp, lr_fn, lr_tp));


# # 適合率（precision）・再現率（recall）の算出
# # print('accuracy score : %.4f'%((lr_tp + lr_tn) / (lr_tp + lr_tn + lr_fp + lr_fn)))
# # print('[pen]_lr_precision : %.4f'%(lr_tp / (lr_tp + lr_fp)))
# # print('[pen]_lr_recall : %.4f'%(lr_tp / (lr_tp + lr_fn)))
# # print('[page]_lr_precision : %.4f'%(lr_tn / (lr_tn + lr_fn)))
# # print('[page]_lr_recall : %.4f'%(lr_tn / (lr_tn + lr_fp)))  
# # print('MCC : %.4f'%( ((lr_tp*lr_tn)-(lr_fp*lr_fn)) / math.sqrt((lr_tp+lr_fp)*(lr_tp+lr_fn)*(lr_tn+lr_fp)*(lr_tn+lr_fn)) ))

# ############################################################################################################################

# # 学習モデルの保存
# with open('model_f_Initial.pickle', mode='wb') as f:
#     pickle.dump(model, f, protocol=2)