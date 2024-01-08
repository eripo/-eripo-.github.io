#############################################
# 勾配ブースティング

# 特徴量選定済みのみ残して軽量化してるのがGBoost.py
# 5分割交差検証，学習データとテストデータが別ファイルの場合にも対応．適切にコメントアウト外して使ってね．
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
df = pd.read_csv( 'Data/all_mm_Initial.csv' )
# df = pd.read_csv( 'Data/all_mm_Final.csv' )


# 個別用
# df = pd.read_csv( 'Data/EK_f_Initial.csv' )
# df = pd.read_csv( 'Data/fm_Initial/fm_Initial09SY.csv' )
# df = pd.read_csv( 'Data/fm_Final/fm_Final16EK.csv' )
# df = pd.read_csv( 'Data/pm_Initial/pm_Initial01AS.csv' )
# df = pd.read_csv( 'Data/pm_Final/pm_Final04KS.csv' )

# print(df)

df1 = df.dropna(how='any')
print(df1)
# print("*******************")


# 特徴量選択
## fm_Initial向け ##
X1 = df1[['intervalTime', 'gapY', 'gapR', 'velRX', 'accelerationR', 'posX','posY','Mode']]

## pm_Initial向け ##
# X1 = df1[['pressure0', 'intervalTime', 'gapX', 'gap', 'gapRY', 'posX', 'posY','Mode']]

## mm_Initial向け ##
# X1 = df1[['intervalTime', 'gapX', 'gap', 'gapRY', 'accelerationR', 'posX','posY','Mode']]

## fm_Final向け ##
# X1 = df1[['velRX_min', 'velRX_mean', 'velR_mean', 'velR_median', 'velR_last','accelerationX_max', 'acceleration_max', 'widthRX','Mode']]

## pm_Final向け ##
# X1 = df1[['vel_median', 'velRX_mean', 'velRX_median', 'velRX_last', 'velRY_last','velR_last', 'acceleration_max', 'acceleration_mean','accelerationRX_max', 'accelerationR_min', 'accelerationR_median','accelerationR_first', 'widthRX','Mode']]

## mm_Final向け ##
# X1 = df1[['vel_max', 'velRX_min', 'velRX_mean', 'velRX_median', 'velR_median','velR_last', 'accelerationR_median', 'widthRX','Mode']]


# print(X1);
# X：学習用データ，y：学習用データのラベル
X = X1.drop(['Mode'],axis=1)
y = df1['Mode']


# 勾配ブースティング（クロスバリデーション） ###########################################################
for i in range(5):
    
    # データを標準化するパイプラインを作成
    # model = make_pipeline(StandardScaler(), GradientBoostingClassifier()) //標準化する場合
    model = make_pipeline(GradientBoostingClassifier())
    # k-fold cross-validationを実行
    kfold = KFold(n_splits=5, shuffle=True, random_state=42)  # 5-fold cross-validationを行う例


    # クロスバリデーションの各分割ごとに混同行列を保存するためのリストを作成
    conf_matrices = []

    # クロスバリデーションの各分割ごとに混同行列を計算
    for train_index, test_index in kfold.split(X):
        X_train, X_test = X.iloc[train_index], X.iloc[test_index]
        y_train, y_test = y.iloc[train_index], y.iloc[test_index]

        # print(X_train)
        # print(X_test)
        # print(y_train)
        # print(y_test)
        # モデルを学習
        model.fit(X_train, y_train)

        # テストデータに対して予測
        y_pred = model.predict(X_test)

        # 混同行列を計算してリストに追加
        conf_matrix = confusion_matrix(y_test, y_pred)
        conf_matrices.append(conf_matrix)
        
    # 混同行列を合算して平均を取得
    # print("混同行列")
    # print(conf_matrices)
    average_conf_matrix = np.mean(conf_matrices, axis=0)
    av_tn, av_fp, av_fn, av_tp = average_conf_matrix[0,0],average_conf_matrix[0,1],average_conf_matrix[1,0],average_conf_matrix[1,1]


    for conf_matrix in conf_matrices:
        cv_tn = conf_matrix[0, 0]  # True Negative
        cv_fp = conf_matrix[0, 1]  # False Positive
        cv_fn = conf_matrix[1, 0]  # False Negative
        cv_tp = conf_matrix[1, 1]  # True Positive
        
        # # 各回の混合行列，正解率（accuracy score），適合率（precision），再現率（recall）の算出および出力
        # print('###')
        # print('混同行列（各回） : %d, %d, %d, %d'%(cv_tn, cv_fp, cv_fn, cv_tp));    
        # print('accuracy score : %.4f'%((cv_tp + cv_tn) / (cv_tp + cv_tn + cv_fp + cv_fn)))
        # print('[pen]_lr_std_precision : %.4f'%(cv_tp / (cv_tp + cv_fp)))
        # print('[pen]_lr_std_recall : %.4f'%(cv_tp / (cv_tp + cv_fn)))
        # print('[page]_lr_precision : %.4f'%(cv_tn / (cv_tn + cv_fn)))
        # print('[page]_lr_recall : %.4f'%(cv_tn / (cv_tn + cv_fp)))
        

    # 最終的な混同行列を表示
    # print('混同行列（平均） : %f, %f, %f, %f'%(av_tn, av_fp, av_fn, av_tp));
    # print('Average Confusion Matrix:')
    # print(average_conf_matrix)
    print('** ↓ average *****************************')
    print('accuracy score : %.4f'%((av_tp + av_tn) / (av_tp + av_tn + av_fp + av_fn)))
    print('[pen]_lr_std_precision : %.4f'%(av_tp / (av_tp + av_fp)))
    print('[pen]_lr_std_recall : %.4f'%(av_tp / (av_tp + av_fn)))
    print('[page]_lr_precision : %.4f'%(av_tn / (av_tn + av_fn)))
    print('[page]_lr_recall : %.4f'%(av_tn / (av_tn + av_fp)))
    print('MCC : %.4f'%( ((av_tp*av_tn)-(av_fp*av_fn)) / math.sqrt((av_tp+av_fp)*(av_tp+av_fn)*(av_tn+av_fp)*(av_tn+av_fn)) ))


    ####################################################################################################


# 勾配ブースティング（学習用データとテスト用データが別ファイルの場合） ###########################################################

# df2 = pd.read_csv( 'Data/all_tasks/all_mp_Final.csv' )
# # df2 = pd.read_csv( 'Data/fm_Initial/fm_Initial16EK.csv' )
# # print(df2)
# df3 = df2.dropna(how='any')

# # 特徴量選択
# ## fm_Initial向け ##
# # test0 = df3[['intervalTime', 'gapY', 'gapR', 'velRX', 'accelerationR', 'posX','posY','Mode']]
# ## pm_Initial向け ##
# # test0 = df3[['pressure0', 'intervalTime', 'gapX', 'gap', 'gapRY', 'posX', 'posY','Mode']]
# ## mm_Initial向け ##
# # test0 = df3[['intervalTime', 'gapX', 'gap', 'gapRY', 'accelerationR', 'posX','posY','Mode']]

# ## fm_Final向け ##
# # test0 = df3[['velRX_min', 'velRX_mean', 'velR_mean', 'velR_median', 'velR_last','accelerationX_max', 'acceleration_max', 'widthRX','Mode']]
# ## pm_Final向け ##
# # test0 = df3[['vel_median', 'velRX_mean', 'velRX_median', 'velRX_last', 'velRY_last','velR_last', 'acceleration_max', 'acceleration_mean','accelerationRX_max', 'accelerationR_min', 'accelerationR_median','accelerationR_first', 'widthRX','Mode']]
# ## mm_Final向け ##
# test0 = df3[['vel_max', 'velRX_min', 'velRX_mean', 'velRX_median', 'velR_median','velR_last', 'accelerationR_median', 'widthRX','Mode']]

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