#############################################
# 学習データとテストデータを入れると
# 機械学習し、正解率を求めるプログラム

#2023/11/30作成
#・Initial系に対応（ForDigitalText_js_Finalとほぼ同じ）
#############################################


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
# import tensorflowjs as tfjss

import csv

from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score


# 学習用データ #
# df = pd.read_csv( 'Data/all_fm_Initial.csv' )
# df = pd.read_csv( 'Data/all_pm_Initial.csv' )
df = pd.read_csv( 'Data/all_mm_Initial.csv' )
print("*******************")
print(df)

df1 = df.dropna(how='any')
print(df1)
print("*******************")


# 説明変数leran_data(特徴量)と目的変数learn_label(判別結果)に分ける
## 分割しない場合．説明変数 適宜不要な列を削除する。削除する列を配列で指定する。################################

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
# learn_data = df1.drop(['Mode'], axis=1)
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
# learn_label = df1['Mode']


# 8:2分割する場合 #############################
# X = df1.drop(['gapRX','gapRY','gapR','velX','velY','vel','velRX','velRY','velR','Mode'], axis=1) //試しにやってみただけ．使いたいときが来るかもだから残しておく
X = df1.drop(['Mode'], axis=1)
y = df1['Mode']
learn_data, test_data, learn_label, test_label = train_test_split(X, y, test_size=0.2, random_state=10)

###########################################################################################

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

# 平均と標準偏差の取得(標準化用)
mean_value = stdsc.mean_
std_deviation = stdsc.scale_
# 平均と標準偏差の保存（標準化用）
with open('scaling_parameters_Initial.pkl', 'wb') as file:
    pickle.dump({'mean': mean_value, 'std': std_deviation}, file)

# data = [[0.946289063,	4486.9,	-20,	-2.399993896,	20.14348457,	-20,	-2.399993896,	20.14348457,	-1.45985401,	-0.175182036,	1.470327336,	-1.45985401,	-0.175182036,	1.470327336,	-0.106558686,	-0.01278701,	0.107323163,	-0.106558686,	-0.01278701,	0.107323163,	670.0375214,	336.2000122,	13.70000005]]
# print(stdsc.transform(data))
# print("あいうえお")
# print(mean_value)
# print(std_deviation)

#コメントアウトを外すとスケーリング後の値を確認できる
# print(train_mm)
# print(train_std)
# print(test_mm)
# print(test_std)
print("############################")
###################################################################################################################



# print(learn_data)
# print(learn_label)

# print("テストデータ***************")
# print(test_data)
# print(test_label)



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


# テストデータによる予測.
result_label_lr = lr.predict(test_data)
result_label_lr_mm = lr_mm.predict(test_mm)
result_label_lr_std = lr_std.predict(test_std)

print('元のデータのスコア :',lr.score(test_data, test_label))
print('正規化したデータのスコア :',lr_mm.score(test_mm, test_label))
print('標準化したデータのスコア :',lr_std.score(test_std, test_label))

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


# # 学習モデルの保存
# tfjs.converters.save_keras_model(model, "./my_model")
# 学習モデルの保存
with open('model_Initial.pickle', mode='wb') as f:
    pickle.dump(lr_std, f, protocol=2)



# 混同行列
from sklearn.metrics import confusion_matrix
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

