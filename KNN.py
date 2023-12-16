#############################################
# 学習データとテストデータを入れると
# 機械学習し、正解率を求めるプログラム
#############################################

# k-近傍法

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

# df = pd.read_csv( 'Data/fm_Initial.csv' )
# df = pd.read_csv( 'Data/fm_Final.csv' )
# df = pd.read_csv( 'Data/pm_Initial.csv' )
# df = pd.read_csv( 'Data/pm_Final.csv' )
print("*******************")
# print(df)


df1 = df.dropna(how='any')
# print(df1)
print("*******************")


# 説明変数leran_data(特徴量)と目的変数learn_label(判別結果)に分ける
## 説明変数 適宜不要な列を削除する。削除する列を配列で指定する。################################

# learn用 ##############################
# # 速度
# learn_data = df1.drop(['aX', 'aY', 'a', 'pos_x', 'pos_y', 'msec', 'v_x/msec', 'v_y/msec', 'v/msec', 'aX/msec', 'aY/msec', 'a/msec', 'Mode'], axis=1)
# # 速度/msec
# learn_data = df1.drop(['v_x', 'v_y', 'v', 'aX', 'aY', 'a', 'pos_x', 'pos_y', 'msec', 'aX/msec', 'aY/msec', 'a/msec', 'Mode'], axis=1)
# # 加速度、加速度/msec 
# learn_data = df1.drop(['v_x', 'v_y', 'v', 'pos_x', 'pos_y', 'msec', 'v_x/msec', 'v_y/msec', 'v/msec', 'Mode'], axis=1)
# # 加速度
# learn_data = df1.drop(['v_x', 'v_y', 'v', 'pos_x', 'pos_y', 'msec', 'aX/msec', 'aY/msec', 'a/msec', 'v_x/msec', 'v_y/msec', 'v/msec', 'Mode'], axis=1)
# # 加速度/msec 
# learn_data = df1.drop(['v_x', 'v_y', 'v', 'aX', 'aY', 'a', 'pos_x', 'pos_y', 'msec', 'v_x/msec', 'v_y/msec', 'v/msec', 'Mode'], axis=1)

# learn0用 #############################
# # 全要素
# learn_data = df1.drop(['msec', 'Mode'], axis=1)
# # 全要素（gapを除く）
# learn_data = df1.drop(['gapX', 'gapY', 'gap', 'msec', 'Mode'], axis=1)

# # 筆圧、速度[px/ms]、加速度
# learn_data = df1.drop(['interval', 'gapX', 'gapY', 'gap', 'pos_x', 'pos_y', 'msec', 'Mode'], axis=1)
# # 速度[px/ms]、加速度
# learn_data = df1.drop(['pressure0', 'interval', 'gapX', 'gapY', 'gap', 'pos_x', 'pos_y', 'msec', 'Mode'], axis=1)
# # 筆圧、速度[px/ms]
# learn_data = df1.drop(['interval', 'gapX', 'gapY', 'gap', 'pos_x', 'pos_y', 'msec', 'aX', 'aY', 'a', 'Mode'], axis=1)
# # 筆圧、加速度
# learn_data = df1.drop(['interval', 'gapX', 'gapY', 'gap', 'pos_x', 'pos_y', 'msec', 'v_x', 'v_y', 'v', 'Mode'], axis=1)
# # 筆圧
# learn_data = df1.drop(['interval', 'gapX', 'gapY', 'gap', 'pos_x', 'pos_y', 'msec', 'v_x', 'v_y', 'v', 'aX', 'aY', 'a', 'Mode'], axis=1)
# # 速度[px/ms]
# learn_data = df1.drop(['pressure0', 'interval', 'gapX', 'gapY', 'gap', 'pos_x', 'pos_y', 'msec', 'aX', 'aY', 'a', 'Mode'], axis=1)
# # 加速度
# learn_data = df1.drop(['pressure0', 'interval', 'gapX', 'gapY', 'gap', 'pos_x', 'pos_y', 'msec', 'v_x', 'v_y', 'v', 'Mode'], axis=1)

# Final用 #############################
# # 全要素
# learn_data = df1.drop(['Mode'], axis=1)
###########################################################################################

# 8:2分割する場合 #############################
## Initial向け ##
# X = df1.drop(['msec','Mode'], axis=1)
# X = df1.drop(['velY','velRY','accelerationY','accelerationRY','msec','Mode'], axis=1)
# X = df1.drop(['gapX','gapY','gap','velX','velY','vel','velRX','velRY','velR','accelerationX','accelerationY','acceleration','accelerationR','msec','Mode'], axis=1)

# X = df1.drop(['gapX','gapY','gap','velX','velY','vel','accelerationX','accelerationY','acceleration','Mode'], axis=1)
# X = df1.drop(['gapRX','gapRY','gapR','velRX','velRY','velR','accelerationRX','accelerationRY','accelerationR','Mode'], axis=1)
# X = df1.drop(['gapX','gapY','gap','velX','velY','vel','accelerationX','accelerationY','acceleration','accelerationR','Mode'], axis=1)

# X = df1.drop(['gapX','gapY','gap','velX','velY','vel','velRX','velRY','velR','accelerationX','accelerationY','acceleration','accelerationR','Mode'], axis=1)
# X = df1.drop(['gapX','gapY','gap','gapRX','gapRY','gapR','velX','velY','vel','accelerationX','accelerationY','acceleration','accelerationR','Mode'], axis=1)

# X = df1.drop(['gapX','gapY','gap','gapRX','gapRY','gapR','velX','velY','vel','accelerationX','accelerationY','acceleration','accelerationRX','accelerationRY','accelerationR','Mode'], axis=1)
# X = df1.drop(['gapX','gapY','gap','gapRX','gapRY','gapR','velX','velY','vel','velRX','velRY','velR','accelerationX','accelerationY','acceleration','accelerationR','Mode'], axis=1)

# X = df1.drop(['gapX','gapY','gap','gapRX','gapRY','gapR','velX','velY','vel','velRX','velRY','velR','accelerationX','accelerationY','acceleration','accelerationRY','accelerationR','Mode'], axis=1)
# X = df1.drop(['gapX','gapY','gap','gapRX','gapRY','gapR','velX','velY','vel','velRX','velRY','velR','accelerationX','accelerationY','acceleration','accelerationRX','accelerationR','Mode'], axis=1)

# # 精度検証結果で使ってないやつ
# X = df1.drop(['gapX','gapY','gap','velX','velY','vel','velRX','velRY','velR','accelerationX','accelerationY','acceleration','accelerationR','msec','Mode'], axis=1)
# X = df1.drop(['gapX','gapY','gap','velX','velY','vel','velRX','velRY','velR','accelerationX','accelerationY','acceleration','accelerationRY','accelerationR','Mode'], axis=1)



## Final向け ##
# X = df1.drop(['Mode'], axis=1)
# X = df1.drop(['velRX_min','velRX_max','velRX_mean','velRX_median','velRX_first','velRX_last','velRY_min','velRY_max','velRY_mean','velRY_median','velRY_first','velRY_last','velR_min','velR_max','velR_mean','velR_median','velR_first','velR_last','accelerationRX_min','accelerationRX_max','accelerationRX_mean','accelerationRX_median','accelerationRX_first','accelerationRX_last','1/5_accelerationRX_mean','1/5_accelerationRX_median','2/5_accelerationRX_mean','2/5_accelerationRX_median','4/5_accelerationRX_mean','4/5_accelerationRX_median','accelerationRY_min','accelerationRY_max','accelerationRY_mean','accelerationRY_median','accelerationRY_first','accelerationRY_last','1/5_accelerationRY_mean','1/5_accelerationRY_median','2/5_accelerationRY_mean','2/5_accelerationRY_median','4/5_accelerationRY_mean','4/5_accelerationRY_median','accelerationR_min','accelerationR_max','accelerationR_mean','accelerationR_median','accelerationR_first','accelerationR_last','1/5_accelerationR_mean','1/5_accelerationR_median','2/5_accelerationR_mean','2/5_accelerationR_median','4/5_accelerationR_mean','4/5_accelerationR_median','widthRX','widthRY','Mode'], axis=1)
# X = df1.drop(['velX_min','velX_max','velX_mean','velX_median','velX_first','velX_last','velY_min','velY_max','velY_mean','velY_median','velY_first','velY_last','vel_min','vel_max','vel_mean','vel_median','vel_first','vel_last','accelerationX_min','accelerationX_max','accelerationX_mean','accelerationX_median','accelerationX_first','accelerationX_last','1/5_accelerationX_mean','1/5_accelerationX_median','2/5_accelerationX_mean','2/5_accelerationX_median','4/5_accelerationX_mean','4/5_accelerationX_median','accelerationY_min','accelerationY_max','accelerationY_mean','accelerationY_median','accelerationY_first','accelerationY_last','1/5_accelerationY_mean','1/5_accelerationY_median','2/5_accelerationY_mean','2/5_accelerationY_median','4/5_accelerationY_mean','4/5_accelerationY_median','acceleration_min','acceleration_max','acceleration_mean','acceleration_median','acceleration_first','acceleration_last','1/5_acceleration_mean','1/5_acceleration_median','2/5_acceleration_mean','2/5_acceleration_median','4/5_acceleration_mean','4/5_acceleration_median','widthX','widthY','Mode'], axis=1)
# X = df1.drop(['velX_min','velX_max','velX_mean','velX_median','velX_first','velX_last','velY_min','velY_max','velY_mean','velY_median','velY_first','velY_last','vel_min','vel_max','vel_mean','vel_median','vel_first','vel_last','accelerationX_min','accelerationX_max','accelerationX_mean','accelerationX_median','accelerationX_first','accelerationX_last','1/5_accelerationX_mean','1/5_accelerationX_median','2/5_accelerationX_mean','2/5_accelerationX_median','4/5_accelerationX_mean','4/5_accelerationX_median','accelerationY_min','accelerationY_max','accelerationY_mean','accelerationY_median','accelerationY_first','accelerationY_last','1/5_accelerationY_mean','1/5_accelerationY_median','2/5_accelerationY_mean','2/5_accelerationY_median','4/5_accelerationY_mean','4/5_accelerationY_median','acceleration_min','acceleration_max','acceleration_mean','acceleration_median','acceleration_first','acceleration_last','1/5_acceleration_mean','1/5_acceleration_median','2/5_acceleration_mean','2/5_acceleration_median','4/5_acceleration_mean','4/5_acceleration_median','accelerationRY_first','widthX','widthY','Mode'], axis=1)
X = df1.drop(['velX_min','velX_max','velX_mean','velX_median','velX_first','velX_last','velY_min','velY_max','velY_mean','velY_median','velY_first','velY_last','vel_min','vel_max','vel_mean','vel_median','vel_first','vel_last','accelerationX_min','accelerationX_max','accelerationX_mean','accelerationX_median','accelerationX_first','accelerationX_last','1/5_accelerationX_mean','1/5_accelerationX_median','2/5_accelerationX_mean','2/5_accelerationX_median','4/5_accelerationX_mean','4/5_accelerationX_median','accelerationY_min','accelerationY_max','accelerationY_mean','accelerationY_median','accelerationY_first','accelerationY_last','1/5_accelerationY_mean','1/5_accelerationY_median','2/5_accelerationY_mean','2/5_accelerationY_median','4/5_accelerationY_mean','4/5_accelerationY_median','acceleration_min','acceleration_max','acceleration_mean','acceleration_median','acceleration_first','acceleration_last','1/5_acceleration_mean','1/5_acceleration_median','2/5_acceleration_mean','2/5_acceleration_median','4/5_acceleration_mean','4/5_acceleration_median','velRY_first','widthX','widthY','Mode'], axis=1)
# X = df1.drop(['gapX','gapY','gap','velX','velY','vel','velRX','velRY','velR','accelerationX','accelerationY','acceleration','accelerationR','Mode'], axis=1)
# X = df1.drop(['gapX','gapY','gap','gapRX','gapRY','gapR','velRX','velRY','velR','accelerationX','accelerationY','acceleration','accelerationR','Mode'], axis=1)
# X = df1.drop(['gapX','gapY','gap','gapRX','gapRY','gapR','velX','velY','vel','accelerationX','accelerationY','acceleration','accelerationR','Mode'], axis=1)


y = df1['Mode']
learn_data, test_data, learn_label, test_label = train_test_split(X, y, test_size=0.2, random_state=0)


# アンダーサンプリングする場合はこちらを有効に．#######################################################################
# from imblearn.under_sampling import RandomUnderSampler
# # アンダーサンプリングを実行
# rus = RandomUnderSampler(random_state=42)
# X_resampled, y_resampled = rus.fit_resample(learn_data, learn_label)

# # アンダーサンプリング後のクラスごとのサンプル数を確認
# print("クラスごとのサンプル数（アンダーサンプリング後）:", dict(zip(*np.unique(y_resampled, return_counts=True))))

# from sklearn.preprocessing import StandardScaler,MinMaxScaler
# #正規化のクラスを生成
# mmsc = MinMaxScaler()
# #標準化のクラスを生成
# stdsc = StandardScaler()

# #注意 →訓練データでfitした変換器を用いて検証データを変換すること
# #訓練用のデータを正規化
# train_mm = mmsc.fit_transform(X_resampled)
# #訓練用のデータを標準化
# train_std = stdsc.fit_transform(X_resampled)
# #訓練用データを基にテストデータを正規化
# test_mm = mmsc.transform(test_data)
# #訓練用データを基にテストデータを標準化
# test_std = stdsc.transform(test_data)
###################################################################################################################

# アンダーサンプリングしない場合はこちらを有効に． ##########################################################################################
from sklearn.preprocessing import StandardScaler,MinMaxScaler
#正規化のクラスを生成
mmsc = MinMaxScaler()
#標準化のクラスを生成
stdsc = StandardScaler()

print("############################")
#注意 →訓練データでfitした変換器を用いて検証データを変換すること
#訓練用のデータを正規化
train_mm = mmsc.fit_transform(learn_data)
#訓練用のデータを標準化
train_std = stdsc.fit_transform(learn_data)
#訓練用データを基にテストデータを正規化
test_mm=mmsc.transform(test_data)
#訓練用データを基にテストデータを標準化
test_std = stdsc.transform(test_data)
#コメントアウトを外すとスケーリング後の値を確認できる
# print(train_mm)
# print(train_std)
# print(test_mm)
# print(test_std)
print("############################")
###################################################################################################################


# learn_label = df1['Mode']

# print(learn_data)
# print(learn_label)


## 8:2で分割する場合，ここを消す #############################################################################################################################
# print("てすとてすと")

# # テストデータ
# # df2 = pd.read_csv( 'Data/Initial(1).csv' )
# # df2 = pd.read_csv( 'Data/Mid(1).csv' )
# df2 = pd.read_csv( 'Data/Final(1).csv' )
# print(df2)
# df3 = df2.dropna(how='any')
# print(df3)

# # 説明変数leran_data(特徴量3つ)と目的変数leran_label(判別結果)に分ける
# ## 説明変数 適宜不要な列を削除する。削除する列を配列で指定する。################################

# # test用 ##############################
# # # test用   速度、加速度、速度/msec、加速度/msec 
# # test_data = df3.drop(['pos_x', 'pos_y', 'msec', 'Mode'], axis=1)

# # test0用 #############################
# # # 全要素
# # test_data = df3.drop(['msec', 'Mode'], axis=1)
# # # 全要素（gapを除く）
# # test_data = df3.drop(['gapX', 'gapY', 'gap', 'msec', 'Mode'], axis=1)

# # # 筆圧、速度[px/ms]、加速度
# # test_data = df3.drop(['interval', 'gapX', 'gapY', 'gap', 'pos_x', 'pos_y', 'msec', 'Mode'], axis=1)
# # # 速度[px/ms]、加速度
# # test_data = df3.drop(['pressure0', 'interval', 'gapX', 'gapY', 'gap', 'pos_x', 'pos_y', 'msec', 'Mode'], axis=1)
# # # 筆圧、速度[px/ms]
# # test_data = df3.drop(['interval', 'gapX', 'gapY', 'gap', 'pos_x', 'pos_y', 'msec', 'aX', 'aY', 'a', 'Mode'], axis=1)
# # # 筆圧、加速度
# # test_data = df3.drop(['interval', 'gapX', 'gapY', 'gap', 'pos_x', 'pos_y', 'msec', 'v_x', 'v_y', 'v', 'Mode'], axis=1)
# # # 筆圧
# # test_data = df3.drop(['interval', 'gapX', 'gapY', 'gap', 'pos_x', 'pos_y', 'msec', 'v_x', 'v_y', 'v', 'aX', 'aY', 'a', 'Mode'], axis=1)
# # # 速度[px/ms]
# # test_data = df3.drop(['pressure0', 'interval', 'gapX', 'gapY', 'gap', 'pos_x', 'pos_y', 'msec', 'aX', 'aY', 'a', 'Mode'], axis=1)
# # # 加速度
# # test_data = df3.drop(['pressure0', 'interval', 'gapX', 'gapY', 'gap', 'pos_x', 'pos_y', 'msec', 'v_x', 'v_y', 'v', 'Mode'], axis=1)

# # Final用 #############################
# # 全要素
# test_data = df3.drop(['Mode'], axis=1)
# ###########################################################################################
# test_label = df3['Mode']

############################################################################################################################################################

# print(test_data)
# print(test_label)

 

# # 学習用のデータと結果を学習する,fit()
# model.fit(learn_data, learn_label)

# # 学習モデルの保存
# with open('model.pickle', mode='wb') as f:
#     pickle.dump(model, f, protocol=2)


# # テストデータによる予測,predict()
# result_label = model.predict(test_data)


# # テスト結果を評価する,accuracy_score()
# print("学習用データ：", learn_data)
# print("予測対象：\n", test_data, ", \n予測結果→", result_label)
# print("正解率＝", accuracy_score(test_label, result_label))



# 勾配ブースティング ###########################################################
from sklearn.ensemble import GradientBoostingClassifier

#元のデータ用
lr = GradientBoostingClassifier()
#正規化したデータ用
lr_mm = GradientBoostingClassifier()
#標準化したデータ用
lr_std = GradientBoostingClassifier()

### 全サンプル使う場合 ##################
#元のデータの適用
lr.fit(learn_data, learn_label)
#正規化したデータの適用
lr_mm.fit(train_mm, learn_label)
#標準化したデータの適用
lr_std.fit(train_std, learn_label)
train_class_counts = {label: sum(learn_label == label) for label in set(learn_label)}
test_class_counts = {label: sum(test_label == label) for label in set(test_label)}
### アンダーサンプリングする場合 #########
#元のデータの適用
# lr.fit(X_resampled, y_resampled)
# #正規化したデータの適用
# lr_mm.fit(train_mm, y_resampled)
# #標準化したデータの適用
# lr_std.fit(train_std, y_resampled)
# train_class_counts = {label: sum(y_resampled == label) for label in set(y_resampled)}
# test_class_counts = {label: sum(test_label == label) for label in set(test_label)}
########################################


print('学習用データの各クラス数 : ')
print(train_class_counts)
print('テスト用データの各クラス数 : ')
print(test_class_counts)


# データを標準化するパイプラインを作成
model = make_pipeline(StandardScaler(), GradientBoostingClassifier())
# k-fold cross-validationを実行
kfold = KFold(n_splits=2, shuffle=True, random_state=42)  # 5-fold cross-validationを行う例
scores = cross_val_score(model, X, y, cv=kfold)
# scores = cross_val_score(lr_std, train_std, learn_label, cv = 5)
print('クロスバリデーションの結果 ： ')
print(np.mean(scores))

# クロスバリデーションの結果から予測結果を取得
y_pred = cross_val_predict(model, X, y, cv=kfold)
# 混同行列を計算
conf_matrix = confusion_matrix(y, y_pred)

# 適合率と再現率を計算
precision = precision_score(y, y_pred, pos_label='pen')
recall = recall_score(y, y_pred, pos_label='pen')


# 混同行列
cv_tn, cv_fp, cv_fn, cv_tp = confusion_matrix(y, y_pred).ravel()

print('混同行列（標準化） : %d, %d, %d, %d'%(cv_tn, cv_fp, cv_fn, cv_tp));


# 適合率（precision）・再現率（recall）の算出
print('[pen]_lr_std_precision : %.4f'%(cv_tp / (cv_tp + cv_fp)))
print('[pen]_lr_std_recall : %.4f'%(cv_tp / (cv_tp + cv_fn)))
print('[page]_lr_precision : %.4f'%(cv_tn / (cv_tn + cv_fn)))
print('[page]_lr_recall : %.4f'%(cv_tn / (cv_tn + cv_fp)))



# クロスバリデーションの結果を表示
print('混同行列：')
print(conf_matrix)
print('適合率:', precision)
print('再現率:', recall)
print('*******************************')


# テストデータによる予測.
result_label_lr = lr.predict(test_data)
result_label_lr_mm = lr_mm.predict(test_mm)
result_label_lr_std = lr_std.predict(test_std)

print('元のデータのスコア :',lr.score(test_data, test_label))
print('正規化したデータのスコア :',lr_mm.score(test_mm, test_label))
print('標準化したデータのスコア :',lr_std.score(test_std, test_label))

##############################################################################



# K近傍法 #####################################################################
# from sklearn.neighbors import KNeighborsClassifier
# #元のデータ用(kの指定なしはk=5)
# lr = KNeighborsClassifier()
# #正規化したデータ用
# lr_mm = KNeighborsClassifier()
# #標準化したデータ用
# lr_std = KNeighborsClassifier()

# ### 全サンプル使う場合 ##################
# # #元のデータの適用
# # lr.fit(learn_data, learn_label)
# # #正規化したデータの適用
# # lr_mm.fit(train_mm, learn_label)
# # #標準化したデータの適用
# # lr_std.fit(train_std, learn_label)
# # train_class_counts = {label: sum(learn_label == label) for label in set(learn_label)}
# # test_class_counts = {label: sum(test_label == label) for label in set(test_label)}
# ### アンダーサンプリングする場合 #########
# #元のデータの適用
# lr.fit(X_resampled, y_resampled)
# #正規化したデータの適用
# lr_mm.fit(train_mm, y_resampled)
# #標準化したデータの適用
# lr_std.fit(train_std, y_resampled)
# train_class_counts = {label: sum(y_resampled == label) for label in set(y_resampled)}
# test_class_counts = {label: sum(test_label == label) for label in set(test_label)}
# ########################################

# print('学習用データの各クラス数 : ')
# print(train_class_counts)
# print('テスト用データの各クラス数 : ')
# print(test_class_counts)


# # テストデータによる予測.
# result_label_lr = lr.predict(test_data)
# result_label_lr_mm = lr_mm.predict(test_mm)
# result_label_lr_std = lr_std.predict(test_std)

# print('元のデータのスコア : %.4f'% lr.score(test_data, test_label))
# print('正規化したデータのスコア : %.4f'% lr_mm.score(test_mm, test_label))
# print('標準化したデータのスコア : %.4f'% lr_std.score(test_std, test_label))



# # kの値ごとの正解率を求める ##################################################
# from sklearn import metrics

# ### 全サンプル使用時はこちら ###############################################
# k_range = range(1, 50)
# accuracy = []
# for k in k_range:
#     knn = KNeighborsClassifier(n_neighbors=k) # インスタンス生成。
#     knn.fit(learn_data, learn_label)             # モデル作成実行（元データ）
#     Y_pred = knn.predict(test_data)               # 予測実行
#     # knn.fit(train_mm, learn_label)               # モデル作成実行(正規化) 
#     # Y_pred = knn.predict(test_mm)                 # 予測実行
#     # knn.fit(train_std, learn_label)                # モデル作成実行（標準化）
#     # Y_pred = knn.predict(test_std)                  # 予測実行
#     accuracy.append(metrics.accuracy_score(test_label, Y_pred)) # 精度格納

# plt.plot(k_range, accuracy)
# plt.show()

### アンダーサンプリングする場合はこちら ####################################
# k_range = range(1, 50)
# accuracy = []
# for k in k_range:
#     knn = KNeighborsClassifier(n_neighbors=k) # インスタンス生成。
#     knn.fit(X_resampled, y_resampled)           # モデル作成実行（元データ）
#     Y_pred = knn.predict(test_data)               # 予測実行
#     # knn.fit(train_mm, y_resampled)              # モデル作成実行(正規化) 
#     # Y_pred = knn.predict(test_mm)                 # 予測実行
#     # knn.fit(train_std, y_resampled)             # モデル作成実行（標準化）
#     # Y_pred = knn.predict(test_std)                # 予測実行
#     accuracy.append(metrics.accuracy_score(test_label, Y_pred)) # 精度格納

# plt.plot(k_range, accuracy)
# plt.show()

##############################################################################




# ランダムフォレスト ###########################################################
# from sklearn.ensemble import RandomForestClassifier
# #元のデータ用
# lr = RandomForestClassifier(random_state = 0)
# #正規化したデータ用
# lr_mm = RandomForestClassifier(random_state = 0)
# #標準化したデータ用
# lr_std = RandomForestClassifier(random_state = 0)


# ### 全サンプル使う場合 ##################
# #元のデータの適用
# lr.fit(learn_data, learn_label)
# #正規化したデータの適用
# lr_mm.fit(train_mm, learn_label)
# #標準化したデータの適用
# lr_std.fit(train_std, learn_label)
# ### アンダーサンプリングする場合 #########
# # #元のデータの適用
# # lr.fit(X_resampled, y_resampled)
# # #正規化したデータの適用
# # lr_mm.fit(train_mm, y_resampled)
# # #標準化したデータの適用
# # lr_std.fit(train_std, y_resampled)
# ########################################


# # テストデータによる予測.
# result_label_lr = lr.predict(test_data)
# result_label_lr_mm = lr_mm.predict(test_mm)
# result_label_lr_std = lr_std.predict(test_std)

# print('元のデータのスコア :',lr.score(test_data, test_label))
# print('正規化したデータのスコア :',lr_mm.score(test_mm, test_label))
# print('標準化したデータのスコア :',lr_std.score(test_std, test_label))

##############################################################################


# サポートベクトルマシン（SVM） ###########################################################
# from sklearn.svm import SVC

# #元のデータ用
# lr = SVC()
# #正規化したデータ用
# lr_mm = SVC()
# #標準化したデータ用
# lr_std = SVC()

# ### 全サンプル使う場合 ##################
# # #元のデータの適用
# # lr.fit(learn_data, learn_label)
# # #正規化したデータの適用
# # lr_mm.fit(train_mm, learn_label)
# # #標準化したデータの適用
# # lr_std.fit(train_std, learn_label)
# ### アンダーサンプリングする場合 #########
# #元のデータの適用
# lr.fit(X_resampled, y_resampled)
# #正規化したデータの適用
# lr_mm.fit(train_mm, y_resampled)
# #標準化したデータの適用
# lr_std.fit(train_std, y_resampled)
# # ########################################


# # テストデータによる予測.
# result_label_lr = lr.predict(test_data)
# result_label_lr_mm = lr_mm.predict(test_mm)
# result_label_lr_std = lr_std.predict(test_std)

# print('元のデータのスコア :',lr.score(test_data, test_label))
# print('正規化したデータのスコア :',lr_mm.score(test_mm, test_label))
# print('標準化したデータのスコア :',lr_std.score(test_std, test_label))

##############################################################################



# ロジスティック回帰 ###########################################################
# from sklearn.linear_model import LogisticRegression

# #元のデータ用
# lr = LogisticRegression()
# #正規化したデータ用
# lr_mm = LogisticRegression()
# #標準化したデータ用
# lr_std = LogisticRegression()

# ### 全サンプル使う場合 ##################
# # #元のデータの適用
# # lr.fit(learn_data, learn_label)
# # #正規化したデータの適用
# # lr_mm.fit(train_mm, learn_label)
# # #標準化したデータの適用
# # lr_std.fit(train_std, learn_label)
# ### アンダーサンプリングする場合 #########
# #元のデータの適用
# lr.fit(X_resampled, y_resampled)
# #正規化したデータの適用
# lr_mm.fit(train_mm, y_resampled)
# #標準化したデータの適用
# lr_std.fit(train_std, y_resampled)
# ########################################


# # テストデータによる予測.
# result_label_lr = lr.predict(test_data)
# result_label_lr_mm = lr_mm.predict(test_mm)
# result_label_lr_std = lr_std.predict(test_std)

# print('元のデータのスコア :',lr.score(test_data, test_label))
# print('正規化したデータのスコア :',lr_mm.score(test_mm, test_label))
# print('標準化したデータのスコア :',lr_std.score(test_std, test_label))

##############################################################################


# 混同行列
lr_tn, lr_fp, lr_fn, lr_tp = confusion_matrix(test_label, result_label_lr).ravel()
lr_mm_tn, lr_mm_fp, lr_mm_fn, lr_mm_tp = confusion_matrix(test_label, result_label_lr_mm).ravel()
lr_std_tn, lr_std_fp, lr_std_fn, lr_std_tp = confusion_matrix(test_label, result_label_lr_std).ravel()

print('混同行列（元データ） : %d, %d, %d, %d'%(lr_tn, lr_fp, lr_fn, lr_tp));
print('混同行列（正規化） : %d, %d, %d, %d'%(lr_mm_tn, lr_mm_fp, lr_mm_fn, lr_mm_tp));
print('混同行列（標準化） : %d, %d, %d, %d'%(lr_std_tn, lr_std_fp, lr_std_fn, lr_std_tp));


# 適合率（precision）・再現率（recall）の算出
print('[pen]_lr_precision : %.4f'%(lr_tp / (lr_tp + lr_fp)))
print('[pen]_lr_recall : %.4f'%(lr_tp / (lr_tp + lr_fn)))
print('[page]_lr_precision : %.4f'%(lr_tn / (lr_tn + lr_fn)))
print('[page]_lr_recall : %.4f'%(lr_tn / (lr_tn + lr_fp)))
print('[pen]_lr_mm_precision : %.4f'%(lr_mm_tp / (lr_mm_tp + lr_mm_fp)))
print('[pen]_lr_mm_recall : %.4f'%(lr_mm_tp / (lr_mm_tp + lr_mm_fn)))
print('[page]_lr_precision : %.4f'%(lr_mm_tn / (lr_mm_tn + lr_mm_fn)))
print('[page]_lr_recall : %.4f'%(lr_mm_tn / (lr_mm_tn + lr_mm_fp)))
print('[pen]_lr_std_precision : %.4f'%(lr_std_tp / (lr_std_tp + lr_std_fp)))
print('[pen]_lr_std_recall : %.4f'%(lr_std_tp / (lr_std_tp + lr_std_fn)))
print('[page]_lr_precision : %.4f'%(lr_std_tn / (lr_std_tn + lr_std_fn)))
print('[page]_lr_recall : %.4f'%(lr_std_tn / (lr_std_tn + lr_std_fp)))
