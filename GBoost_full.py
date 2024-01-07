#############################################
# 学習データとテストデータを入れると
# 機械学習し、正解率を求めるプログラム

# 特徴量のパターンがたくさん書いてあるver．特徴量選定済みのみ残して軽量化してるのがGBoost.py
#############################################

# k-近傍法

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

from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

from sklearn.preprocessing import StandardScaler,MinMaxScaler

from sklearn.model_selection import cross_val_score
from sklearn.model_selection import KFold
from sklearn.pipeline import make_pipeline

from sklearn.model_selection import cross_val_predict
from sklearn.metrics import confusion_matrix, precision_score, recall_score


# 学習用データ #
df = pd.read_csv( 'Data/all_fm_Initial.csv' )
# df = pd.read_csv( 'Data/all_pm_Initial.csv' )
# df = pd.read_csv( 'Data/all_fm_Final.csv' )
# df = pd.read_csv( 'Data/all_pm_Final.csv' )
# df = pd.read_csv( 'Data/all_mm_Initial.csv' )
# df = pd.read_csv( 'Data/all_mm_Final.csv' )

# エラー出た子たち
# df = pd.read_csv( 'Data/fm_Initial/fm_Initial01AS.csv' )
# df = pd.read_csv( 'Data/fm_Initial/fm_Initial02MT.csv' )
# df = pd.read_csv( 'Data/fm_Initial/fm_Initial07SS.csv' )
# df = pd.read_csv( 'Data/fm_Final/fm_Final09SY.csv' )

# df = pd.read_csv( 'Data/fm_Final/fm_Final04KS.csv' )
# df = pd.read_csv( 'Data/pm_Initial/pm_Initial16EK.csv' )
# df = pd.read_csv( 'Data/pm_Final/pm_Final16EK.csv' )
# df = pd.read_csv( 'Data/fm_Initial.csv' )
# df = pd.read_csv( 'Data/fm_Final.csv' )
# df = pd.read_csv( 'Data/pm_Initial.csv' )
# df = pd.read_csv( 'Data/pm_Final.csv' )
print("*******************")
# print(df)


df1 = df.dropna(how='any')
print(df1)
print("*******************")


# 説明変数leran_data(特徴量)と目的変数learn_label(判別結果)に分ける

# 8:2分割する場合 #############################

## fm_Initial向け ##
# 全部（msec除く）
# X1 = df1[['pressure0','intervalTime','gapX','gapY','gap','gapRX','gapRY','gapR','velX','velY','vel','velRX','velRY','velR','accelerationX','accelerationY','acceleration','accelerationRX','accelerationRY','accelerationR','posX','posY','Mode']]
# 目的変数との相関絶対値0.05以上残し
# X1 = df1[['intervalTime','gapX','gapY','gap','gapRX','gapRY','gapR','velX','velY','vel','velRX','velRY','velR','accelerationX','acceleration','accelerationRX','accelerationR','posX','posY','Mode']]
# VIF10未満　***採用！！！！***
# X1 = df1[['intervalTime','gapX','gapY','gap','accelerationRX','posX','posY','Mode']]


# 目的変数との相関絶対値0.15以上残し
# X1 = df1[['intervalTime','gapY','gap','gapR','velX','vel','velRX','velR','acceleration','accelerationR','posX','posY','Mode']]
# VIF10未満　***採用！！！！***
X1 = df1[['intervalTime', 'gapY', 'gapR', 'velRX', 'accelerationR', 'posX','posY','Mode']]
# ****************************

## pm_Initial向け ##
# 全部（msec除く）
# X1 = df1[['pressure0','intervalTime','gapX','gapY','gap','gapRX','gapRY','gapR','velX','velY','vel','velRX','velRY','velR','accelerationX','accelerationY','acceleration','accelerationRX','accelerationRY','accelerationR','posX','posY','Mode']]
# 目的変数との相関絶対値0.05以上残し
# 消すものなかった（全部（msec除く）のときと一緒）
# VIF10未満　***採用！！！！***
# X1 = df1[['pressure0','intervalTime','gapX','gap','gapRY','posX','posY','Mode']]

# # 目的変数との相関絶対値0.15以上残し
# # X1 = df1[['pressure0','intervalTime','gapX','gapY','gap','gapRX','gapRY','gapR','velX','velY','vel','velRX','velRY','velR','accelerationX','accelerationY','acceleration','accelerationRX','accelerationRY','accelerationR','posX','posY','Mode']]
# # VIF10未満　***採用！！！！***
# X1 = df1[['pressure0', 'intervalTime', 'gapX', 'gap', 'gapRY', 'posX', 'posY','Mode']]

# ****************************

## mm_Initial向け ##
# 全部（msec除く）
# X1 = df1[['pressure0','intervalTime','gapX','gapY','gap','gapRX','gapRY','gapR','velX','velY','vel','velRX','velRY','velR','accelerationX','accelerationY','acceleration','accelerationRX','accelerationRY','accelerationR','posX','posY','Mode']]
# 目的変数との相関絶対値0.05以上残し
# X1 = df1[['pressure0','intervalTime','gapX','gapY','gap','gapRX','gapRY','gapR','velX','velY','vel','velRX','velRY','velR','accelerationX','acceleration','accelerationRX','accelerationR','posX','posY','Mode']]
# VIF10未満　***採用！！！！***
# X1 = df1[['pressure0','intervalTime','gapX','gapY','gap','accelerationRX','posX','posY','Mode']]


# 目的変数との相関絶対値0.15以上残し
# X1 = df1[['intervalTime','gapX','gapY','gap','gapRX','gapRY','gapR','velX','vel','velRX','velR','acceleration','accelerationR','posX','posY','Mode']]
# VIF10未満　***採用！！！！***
# X1 = df1[['intervalTime', 'gapX', 'gap', 'gapRY', 'accelerationR', 'posX','posY','Mode']]
# ****************************



## fm_Final向け ##
# 全部（msec除く）
# X1 = df1[['velX_min','velX_max','velX_mean','velX_median','velX_first','velX_last','velY_min','velY_max','velY_mean','velY_median','velY_first','velY_last','vel_min','vel_max','vel_mean','vel_median','vel_first','vel_last','velRX_min','velRX_max','velRX_mean','velRX_median','velRX_first','velRX_last','velRY_min','velRY_max','velRY_mean','velRY_median','velRY_first','velRY_last','velR_min','velR_max','velR_mean','velR_median','velR_first','velR_last','accelerationX_min','accelerationX_max','accelerationX_mean','accelerationX_median','accelerationX_first','accelerationX_last','1/5_accelerationX_mean','1/5_accelerationX_median','2/5_accelerationX_mean','2/5_accelerationX_median','4/5_accelerationX_mean','4/5_accelerationX_median','accelerationY_min','accelerationY_max','accelerationY_mean','accelerationY_median','accelerationY_first','accelerationY_last','1/5_accelerationY_mean','1/5_accelerationY_median','2/5_accelerationY_mean','2/5_accelerationY_median','4/5_accelerationY_mean','4/5_accelerationY_median','acceleration_min','acceleration_max','acceleration_mean','acceleration_median','acceleration_first','acceleration_last','1/5_acceleration_mean','1/5_acceleration_median','2/5_acceleration_mean','2/5_acceleration_median','4/5_acceleration_mean','4/5_acceleration_median','accelerationRX_min','accelerationRX_max','accelerationRX_mean','accelerationRX_median','accelerationRX_first','accelerationRX_last','1/5_accelerationRX_mean','1/5_accelerationRX_median','2/5_accelerationRX_mean','2/5_accelerationRX_median','4/5_accelerationRX_mean','4/5_accelerationRX_median','accelerationRY_min','accelerationRY_max','accelerationRY_mean','accelerationRY_median','accelerationRY_first','accelerationRY_last','1/5_accelerationRY_mean','1/5_accelerationRY_median','2/5_accelerationRY_mean','2/5_accelerationRY_median','4/5_accelerationRY_mean','4/5_accelerationRY_median','accelerationR_min','accelerationR_max','accelerationR_mean','accelerationR_median','accelerationR_first','accelerationR_last','1/5_accelerationR_mean','1/5_accelerationR_median','2/5_accelerationR_mean','2/5_accelerationR_median','4/5_accelerationR_mean','4/5_accelerationR_median','pressure_min','pressure_max','pressure_mean','pressure_median','pressure_first','pressure_last','dragTime','widthX','widthY','widthRX','widthRY','Mode']]
# 目的変数との相関絶対値0.1以上残し
# X1 = df1[['velX_min','velX_max','velX_mean','velX_median','velX_first','velX_last','velY_max','velY_last','vel_max','vel_mean','vel_median','vel_first','vel_last','velRX_min','velRX_max','velRX_mean','velRX_median','velRX_first','velRX_last','velRY_max','velRY_last','velR_max','velR_mean','velR_median','velR_first','velR_last','accelerationX_min','accelerationX_max','accelerationX_first','accelerationX_last','1/5_accelerationX_mean','1/5_accelerationX_median','2/5_accelerationX_mean','accelerationY_min','accelerationY_max','accelerationY_last','1/5_accelerationY_mean','acceleration_min','acceleration_max','acceleration_mean','acceleration_median','acceleration_first','2/5_acceleration_mean','4/5_acceleration_mean','accelerationRX_min','accelerationRX_max','accelerationRX_first','accelerationRX_last','1/5_accelerationRX_mean','1/5_accelerationRX_median','2/5_accelerationRX_mean','accelerationRY_last','accelerationR_min','accelerationR_max','accelerationR_median','accelerationR_first','2/5_accelerationR_mean','4/5_accelerationR_mean','dragTime','widthX','widthY','widthRX','Mode']]
# VIF10未満
# X1 = df1[['velX_min','velX_max','velRX_median','velRX_last','velRY_max','velRY_last','velR_median','velR_last','2/5_accelerationX_mean','accelerationY_min','accelerationY_max','1/5_accelerationY_mean','2/5_acceleration_mean','accelerationRX_min','accelerationRX_max','accelerationRX_last','1/5_accelerationRX_mean','1/5_accelerationRX_median','accelerationRY_last','accelerationR_max','accelerationR_median','accelerationR_first','4/5_accelerationR_mean','dragTime','widthX','widthY','Mode']]

# 目的変数との相関絶対値0.3以上残し
# X1 = df1[['velX_min','velX_mean','vel_max','vel_mean','vel_median','vel_last','velRX_min','velRX_mean','velR_max','velR_mean','velR_median','velR_last','accelerationX_max','acceleration_max','widthX','widthRX','Mode']]
# VIF10未満　これを採用！！！！
# X1 = df1[['velRX_min', 'velRX_mean', 'velR_mean', 'velR_median', 'velR_last','accelerationX_max', 'acceleration_max', 'widthRX','Mode']]
# ****************************

## pm_Final向け ##
# 全部
# X1 = df1[['velX_min','velX_max','velX_mean','velX_median','velX_first','velX_last','velY_min','velY_max','velY_mean','velY_median','velY_first','velY_last','vel_min','vel_max','vel_mean','vel_median','vel_first','vel_last','velRX_min','velRX_max','velRX_mean','velRX_median','velRX_first','velRX_last','velRY_min','velRY_max','velRY_mean','velRY_median','velRY_first','velRY_last','velR_min','velR_max','velR_mean','velR_median','velR_first','velR_last','accelerationX_min','accelerationX_max','accelerationX_mean','accelerationX_median','accelerationX_first','accelerationX_last','1/5_accelerationX_mean','1/5_accelerationX_median','2/5_accelerationX_mean','2/5_accelerationX_median','4/5_accelerationX_mean','4/5_accelerationX_median','accelerationY_min','accelerationY_max','accelerationY_mean','accelerationY_median','accelerationY_first','accelerationY_last','1/5_accelerationY_mean','1/5_accelerationY_median','2/5_accelerationY_mean','2/5_accelerationY_median','4/5_accelerationY_mean','4/5_accelerationY_median','acceleration_min','acceleration_max','acceleration_mean','acceleration_median','acceleration_first','acceleration_last','1/5_acceleration_mean','1/5_acceleration_median','2/5_acceleration_mean','2/5_acceleration_median','4/5_acceleration_mean','4/5_acceleration_median','accelerationRX_min','accelerationRX_max','accelerationRX_mean','accelerationRX_median','accelerationRX_first','accelerationRX_last','1/5_accelerationRX_mean','1/5_accelerationRX_median','2/5_accelerationRX_mean','2/5_accelerationRX_median','4/5_accelerationRX_mean','4/5_accelerationRX_median','accelerationRY_min','accelerationRY_max','accelerationRY_mean','accelerationRY_median','accelerationRY_first','accelerationRY_last','1/5_accelerationRY_mean','1/5_accelerationRY_median','2/5_accelerationRY_mean','2/5_accelerationRY_median','4/5_accelerationRY_mean','4/5_accelerationRY_median','accelerationR_min','accelerationR_max','accelerationR_mean','accelerationR_median','accelerationR_first','accelerationR_last','1/5_accelerationR_mean','1/5_accelerationR_median','2/5_accelerationR_mean','2/5_accelerationR_median','4/5_accelerationR_mean','4/5_accelerationR_median','pressure_min','pressure_max','pressure_mean','pressure_median','pressure_first','pressure_last','dragTime','widthX','widthY','widthRX','widthRY','Mode']]
# 目的変数との相関絶対値0.1以上残し
# X1 = df1[['velX_min','velX_max','velX_mean','velX_median','velX_first','velX_last','velY_max','velY_mean','velY_median','velY_first','velY_last','vel_max','vel_mean','vel_median','vel_first','vel_last','velRX_min','velRX_max','velRX_mean','velRX_median','velRX_first','velRX_last','velRY_mean','velRY_median','velRY_first','velRY_last','velR_max','velR_mean','velR_median','velR_first','velR_last','accelerationX_min','accelerationX_max','accelerationX_mean','accelerationX_median','accelerationX_first','accelerationY_min','accelerationY_max','accelerationY_mean','accelerationY_median','accelerationY_first','2/5_accelerationY_mean','4/5_accelerationY_mean','4/5_accelerationY_median','acceleration_min','acceleration_max','acceleration_mean','acceleration_median','acceleration_first','4/5_acceleration_mean','4/5_acceleration_median','accelerationRX_min','accelerationRX_max','accelerationRX_mean','accelerationRX_median','accelerationRX_first','accelerationRY_max','accelerationRY_mean','accelerationRY_median','accelerationRY_first','2/5_accelerationRY_mean','4/5_accelerationRY_mean','4/5_accelerationRY_median','accelerationR_min','accelerationR_max','accelerationR_mean','accelerationR_median','accelerationR_first','4/5_accelerationR_mean','4/5_accelerationR_median','pressure_first','dragTime','widthX','widthY','widthRX','Mode']]
# VIF10未満
# X1 = df1[['velX_max','vel_median','velRX_min','velRX_median','velRX_last','velRY_mean','velRY_median','velRY_last','velR_last','accelerationX_mean','accelerationY_max','accelerationY_mean','acceleration_mean','accelerationRX_median','accelerationRX_first','accelerationRY_median','accelerationRY_first','2/5_accelerationRY_mean','4/5_accelerationRY_mean','4/5_accelerationRY_median','accelerationR_median','accelerationR_first','4/5_accelerationR_mean','4/5_accelerationR_median','pressure_first','dragTime','widthY','widthRX','Mode']]

# 目的変数との相関絶対値0.3以上残し　
# X1 = df1[['velX_min','velX_mean','velX_median','velX_last','velY_last','vel_max','vel_mean','vel_median','vel_first','vel_last','velRX_min','velRX_mean','velRX_median','velRX_last','velRY_last','velR_max','velR_mean','velR_median','velR_first','velR_last','accelerationX_min','accelerationX_max','acceleration_min','acceleration_max','acceleration_mean','acceleration_median','acceleration_first','accelerationRX_min','accelerationRX_max','accelerationR_min','accelerationR_max','accelerationR_mean','accelerationR_median','accelerationR_first','widthX','widthRX','Mode']]
# VIF10未満　これを採用！！！！
# X1 = df1[['vel_median', 'velRX_mean', 'velRX_median', 'velRX_last', 'velRY_last','velR_last', 'acceleration_max', 'acceleration_mean','accelerationRX_max', 'accelerationR_min', 'accelerationR_median','accelerationR_first', 'widthRX','Mode']]
# ****************************

## mm_Final向け ##
# 目的変数との相関絶対値0.3以上残し
# X1 = df1[['velX_min','velX_mean','velX_median','vel_max','vel_mean','vel_median','vel_last','velRX_min','velRX_mean','velRX_median','velR_max','velR_mean','velR_median','velR_last','acceleration_median','accelerationR_median','widthX','widthRX','Mode']]
# VIF10未満　***採用！！！！***
# X1 = df1[['vel_max', 'velRX_min', 'velRX_mean', 'velRX_median', 'velR_median','velR_last', 'accelerationR_median', 'widthRX','Mode']]
# ****************************


# print(X1);


X = X1.drop(['Mode'],axis=1)



# X1 = df1[['velX_min','velX_max','velX_mean','velX_median','velX_first','velX_last','velY_min','velY_max','velY_mean','velY_first','velY_last','vel_min','vel_max','vel_mean','vel_median','vel_first','vel_last','velRX_min','velRX_max','velRX_mean','velRX_median','velRX_first','velRX_last','velRY_max','velRY_mean','velRY_first','velRY_last','velR_min','velR_max','velR_mean','velR_median','velR_first','velR_last','accelerationX_min','accelerationX_max','accelerationX_median','accelerationX_first','accelerationX_last','1/5_accelerationX_mean','1/5_accelerationX_median','2/5_accelerationX_mean','2/5_accelerationX_median','4/5_accelerationX_mean','accelerationY_min','accelerationY_max','accelerationY_median','accelerationY_last','1/5_accelerationY_mean','4/5_accelerationY_median','acceleration_min','acceleration_max','acceleration_mean','acceleration_median','acceleration_first','acceleration_last','1/5_acceleration_mean','2/5_acceleration_mean','4/5_acceleration_mean','4/5_acceleration_median','accelerationRX_min','accelerationRX_max','accelerationRX_median','accelerationRX_first','accelerationRX_last','1/5_accelerationRX_mean','1/5_accelerationRX_median','2/5_accelerationRX_mean','2/5_accelerationRX_median','4/5_accelerationRX_mean','accelerationRY_max','accelerationRY_median','accelerationRY_last','1/5_accelerationRY_mean','4/5_accelerationRY_median','accelerationR_min','accelerationR_max','accelerationR_median','accelerationR_first','2/5_accelerationR_mean','4/5_accelerationR_mean','4/5_accelerationR_median','pressure_max','pressure_mean','pressure_median','pressure_first','dragTime','widthX','widthY','widthRX','widthRY','Mode']]
# X1 = df1[['velX_min','velX_max','velX_mean','velX_median','velX_first','velX_last','velY_max','velY_mean','velY_last','vel_max','vel_mean','vel_median','vel_first','vel_last','velRX_min','velRX_max','velRX_mean','velRX_median','velRX_first','velRX_last','velRY_max','velRY_last','velR_max','velR_mean','velR_median','velR_first','velR_last','accelerationX_min','accelerationX_max','accelerationX_first','accelerationY_min','accelerationY_max','acceleration_min','acceleration_max','acceleration_median','acceleration_first','2/5_acceleration_mean','accelerationRX_min','accelerationRX_max','accelerationRX_first','accelerationR_min','accelerationR_max','accelerationR_median','accelerationR_first','dragTime','widthX','widthY','widthRX','Mode']]
# X1 = df1[['velX_min','velX_mean','velX_median','vel_max','vel_mean','vel_median','vel_last','velRX_min','velRX_mean','velRX_median','velR_max','velR_mean','velR_median','velR_last','acceleration_median','accelerationR_median','widthX','widthRX','Mode']]
# X1 = df1[['velX_min','vel_max','vel_mean','vel_median','velRX_min','velR_max','velR_mean','velR_median','widthX','widthRX','Mode']]
# X1 = df1[['vel_mean','velR_mean','widthX','widthRX','Mode']]

# X = X1.drop(['Mode'],axis=1)


y = df1['Mode']

for i in range(5):
    # 勾配ブースティング（標準化＆クロスバリデーション） ###########################################################
    from sklearn.ensemble import GradientBoostingClassifier

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


    ##############################################################################











# 基本上のだけ使う．
# 勾配ブースティング（元データ，正規化，標準化 ＆ クロスバリデーションなし） ###########################################################
# learn_data, test_data, learn_label, test_label = train_test_split(X, y, test_size=0.2, random_state=0)


# # アンダーサンプリングしない場合はこちらを有効に． ##########################################################################################
# from sklearn.preprocessing import StandardScaler,MinMaxScaler
# #正規化のクラスを生成
# mmsc = MinMaxScaler()
# #標準化のクラスを生成
# stdsc = StandardScaler()

# print("############################")
# #注意 →訓練データでfitした変換器を用いて検証データを変換すること
# #訓練用のデータを正規化
# train_mm = mmsc.fit_transform(learn_data)
# #訓練用のデータを標準化
# train_std = stdsc.fit_transform(learn_data)
# #訓練用データを基にテストデータを正規化
# test_mm=mmsc.transform(test_data)
# #訓練用データを基にテストデータを標準化
# test_std = stdsc.transform(test_data)
# #コメントアウトを外すとスケーリング後の値を確認できる
# # print(train_mm)
# # print(train_std)
# # print(test_mm)
# # print(test_std)
# print("############################")
# ###################################################################################################################


# # learn_label = df1['Mode']

# # print(learn_data)
# # print(learn_label)
# # print(test_data)
# # print(test_label)


# #元のデータ用
# lr = GradientBoostingClassifier()
# #正規化したデータ用
# lr_mm = GradientBoostingClassifier()
# #標準化したデータ用
# lr_std = GradientBoostingClassifier()

# ### 全サンプル使う場合 ##################
# #元のデータの適用
# lr.fit(learn_data, learn_label)
# #正規化したデータの適用
# lr_mm.fit(train_mm, learn_label)
# #標準化したデータの適用
# lr_std.fit(train_std, learn_label)
# train_class_counts = {label: sum(learn_label == label) for label in set(learn_label)}
# test_class_counts = {label: sum(test_label == label) for label in set(test_label)}

# print('学習用データの各クラス数 : ')
# print(train_class_counts)
# print('テスト用データの各クラス数 : ')
# print(test_class_counts)


# # テストデータによる予測.
# result_label_lr = lr.predict(test_data)
# result_label_lr_mm = lr_mm.predict(test_mm)
# result_label_lr_std = lr_std.predict(test_std)

# print('元のデータのスコア :',lr.score(test_data, test_label))
# print('正規化したデータのスコア :',lr_mm.score(test_mm, test_label))
# print('標準化したデータのスコア :',lr_std.score(test_std, test_label))

# # 混同行列
# lr_tn, lr_fp, lr_fn, lr_tp = confusion_matrix(test_label, result_label_lr).ravel()
# lr_mm_tn, lr_mm_fp, lr_mm_fn, lr_mm_tp = confusion_matrix(test_label, result_label_lr_mm).ravel()
# lr_std_tn, lr_std_fp, lr_std_fn, lr_std_tp = confusion_matrix(test_label, result_label_lr_std).ravel()

# print('混同行列（元データ） : %d, %d, %d, %d'%(lr_tn, lr_fp, lr_fn, lr_tp));
# print('混同行列（正規化） : %d, %d, %d, %d'%(lr_mm_tn, lr_mm_fp, lr_mm_fn, lr_mm_tp));
# print('混同行列（標準化） : %d, %d, %d, %d'%(lr_std_tn, lr_std_fp, lr_std_fn, lr_std_tp));


# # 適合率（precision）・再現率（recall）の算出
# print('[pen]_lr_precision : %.4f'%(lr_tp / (lr_tp + lr_fp)))
# print('[pen]_lr_recall : %.4f'%(lr_tp / (lr_tp + lr_fn)))
# print('[page]_lr_precision : %.4f'%(lr_tn / (lr_tn + lr_fn)))
# print('[page]_lr_recall : %.4f'%(lr_tn / (lr_tn + lr_fp)))
# print('[pen]_lr_mm_precision : %.4f'%(lr_mm_tp / (lr_mm_tp + lr_mm_fp)))
# print('[pen]_lr_mm_recall : %.4f'%(lr_mm_tp / (lr_mm_tp + lr_mm_fn)))
# print('[page]_lr_precision : %.4f'%(lr_mm_tn / (lr_mm_tn + lr_mm_fn)))
# print('[page]_lr_recall : %.4f'%(lr_mm_tn / (lr_mm_tn + lr_mm_fp)))
# print('[pen]_lr_std_precision : %.4f'%(lr_std_tp / (lr_std_tp + lr_std_fp)))
# print('[pen]_lr_std_recall : %.4f'%(lr_std_tp / (lr_std_tp + lr_std_fn)))
# print('[page]_lr_precision : %.4f'%(lr_std_tn / (lr_std_tn + lr_std_fn)))
# print('[page]_lr_recall : %.4f'%(lr_std_tn / (lr_std_tn + lr_std_fp)))