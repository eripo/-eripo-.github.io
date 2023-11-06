#############################################
# 学習データとテストデータを入れると
# 機械学習し、正解率を求めるプログラム
#############################################

# k-近傍法

import numpy as np
# from keras.datasets import mnist
# import time
# import matplotlib.pyplot as plt
# from PIL import Image
from sklearn.model_selection import train_test_split
# import glob
# import argparse
import pandas as pd
# import japanize_matplotlib
import pickle


import csv

from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score


# 学習用データ #
df = pd.read_csv( 'Data/Initial (5).csv' )
# df = pd.read_csv( 'Data/Mid (5).csv' )
# df = pd.read_csv( 'Data/Final (5).csv' )
print(df)



# 説明変数leran_data(特徴量)と目的変数learn_label(判別結果)に分ける
## 説明変数 適宜不要な列を削除する。削除する列を配列で指定する。################################

# learn用 ##############################
# # 速度
# learn_data = df.drop(['aX', 'aY', 'a', 'pos_x', 'pos_y', 'msec', 'v_x/msec', 'v_y/msec', 'v/msec', 'aX/msec', 'aY/msec', 'a/msec', 'Mode'], axis=1)
# # 速度/msec
# learn_data = df.drop(['v_x', 'v_y', 'v', 'aX', 'aY', 'a', 'pos_x', 'pos_y', 'msec', 'aX/msec', 'aY/msec', 'a/msec', 'Mode'], axis=1)
# # 加速度、加速度/msec 
# learn_data = df.drop(['v_x', 'v_y', 'v', 'pos_x', 'pos_y', 'msec', 'v_x/msec', 'v_y/msec', 'v/msec', 'Mode'], axis=1)
# # 加速度
# learn_data = df.drop(['v_x', 'v_y', 'v', 'pos_x', 'pos_y', 'msec', 'aX/msec', 'aY/msec', 'a/msec', 'v_x/msec', 'v_y/msec', 'v/msec', 'Mode'], axis=1)
# # 加速度/msec 
# learn_data = df.drop(['v_x', 'v_y', 'v', 'aX', 'aY', 'a', 'pos_x', 'pos_y', 'msec', 'v_x/msec', 'v_y/msec', 'v/msec', 'Mode'], axis=1)

# learn0用 #############################
# # 全要素
# learn_data = df.drop(['msec', 'Mode'], axis=1)
# # 全要素（gapを除く）
# learn_data = df.drop(['gapX', 'gapY', 'gap', 'msec', 'Mode'], axis=1)

# # 筆圧、速度[px/ms]、加速度
# learn_data = df.drop(['interval', 'gapX', 'gapY', 'gap', 'pos_x', 'pos_y', 'msec', 'Mode'], axis=1)
# # 速度[px/ms]、加速度
# learn_data = df.drop(['pressure0', 'interval', 'gapX', 'gapY', 'gap', 'pos_x', 'pos_y', 'msec', 'Mode'], axis=1)
# # 筆圧、速度[px/ms]
# learn_data = df.drop(['interval', 'gapX', 'gapY', 'gap', 'pos_x', 'pos_y', 'msec', 'aX', 'aY', 'a', 'Mode'], axis=1)
# # 筆圧、加速度
# learn_data = df.drop(['interval', 'gapX', 'gapY', 'gap', 'pos_x', 'pos_y', 'msec', 'v_x', 'v_y', 'v', 'Mode'], axis=1)
# # 筆圧
# learn_data = df.drop(['interval', 'gapX', 'gapY', 'gap', 'pos_x', 'pos_y', 'msec', 'v_x', 'v_y', 'v', 'aX', 'aY', 'a', 'Mode'], axis=1)
# # 速度[px/ms]
# learn_data = df.drop(['pressure0', 'interval', 'gapX', 'gapY', 'gap', 'pos_x', 'pos_y', 'msec', 'aX', 'aY', 'a', 'Mode'], axis=1)
# # 加速度
# learn_data = df.drop(['pressure0', 'interval', 'gapX', 'gapY', 'gap', 'pos_x', 'pos_y', 'msec', 'v_x', 'v_y', 'v', 'Mode'], axis=1)

# Final用 #############################
# # 全要素
# learn_data = df.drop(['Mode'], axis=1)
###########################################################################################

# 8:2分割する場合 #############################
X = df.drop(['Mode'], axis=1)
y = df['Mode']
learn_data, test_data, learn_label, test_label = train_test_split(X, y, test_size=0.2, random_state=0)
###########################################################################################

# learn_label = df['Mode']

print(learn_data)
print(learn_label)


## 8:2で分割する場合，ここを消す #############################################################################################################################
# print("てすとてすと")

# # テストデータ
# # df2 = pd.read_csv( 'Data/Initial(1).csv' )
# # df2 = pd.read_csv( 'Data/Mid(1).csv' )
# df2 = pd.read_csv( 'Data/Final(1).csv' )
# print(df2)
# # 説明変数leran_data(特徴量3つ)と目的変数leran_label(判別結果)に分ける
# ## 説明変数 適宜不要な列を削除する。削除する列を配列で指定する。################################

# # test用 ##############################
# # # test用   速度、加速度、速度/msec、加速度/msec 
# # test_data = df2.drop(['pos_x', 'pos_y', 'msec', 'Mode'], axis=1)

# # test0用 #############################
# # # 全要素
# # test_data = df2.drop(['msec', 'Mode'], axis=1)
# # # 全要素（gapを除く）
# # test_data = df2.drop(['gapX', 'gapY', 'gap', 'msec', 'Mode'], axis=1)

# # # 筆圧、速度[px/ms]、加速度
# # test_data = df2.drop(['interval', 'gapX', 'gapY', 'gap', 'pos_x', 'pos_y', 'msec', 'Mode'], axis=1)
# # # 速度[px/ms]、加速度
# # test_data = df2.drop(['pressure0', 'interval', 'gapX', 'gapY', 'gap', 'pos_x', 'pos_y', 'msec', 'Mode'], axis=1)
# # # 筆圧、速度[px/ms]
# # test_data = df2.drop(['interval', 'gapX', 'gapY', 'gap', 'pos_x', 'pos_y', 'msec', 'aX', 'aY', 'a', 'Mode'], axis=1)
# # # 筆圧、加速度
# # test_data = df2.drop(['interval', 'gapX', 'gapY', 'gap', 'pos_x', 'pos_y', 'msec', 'v_x', 'v_y', 'v', 'Mode'], axis=1)
# # # 筆圧
# # test_data = df2.drop(['interval', 'gapX', 'gapY', 'gap', 'pos_x', 'pos_y', 'msec', 'v_x', 'v_y', 'v', 'aX', 'aY', 'a', 'Mode'], axis=1)
# # # 速度[px/ms]
# # test_data = df2.drop(['pressure0', 'interval', 'gapX', 'gapY', 'gap', 'pos_x', 'pos_y', 'msec', 'aX', 'aY', 'a', 'Mode'], axis=1)
# # # 加速度
# # test_data = df2.drop(['pressure0', 'interval', 'gapX', 'gapY', 'gap', 'pos_x', 'pos_y', 'msec', 'v_x', 'v_y', 'v', 'Mode'], axis=1)

# # Final用 #############################
# # 全要素
# test_data = df2.drop(['Mode'], axis=1)
# ###########################################################################################
# test_label = df2['Mode']

############################################################################################################################################################

print(test_data)
print(test_label)


 
# アルゴリズムを指定。K最近傍法を採用
model = KNeighborsClassifier(n_neighbors=1)

# 学習用のデータと結果を学習する,fit()
model.fit(learn_data, learn_label)

# 学習モデルの保存
with open('model.pickle', mode='wb') as f:
    pickle.dump(model, f, protocol=2)


# テストデータによる予測,predict()
# test_data = [[-63, -21, 66]]
result_label = model.predict(test_data)


# テスト結果を評価する,accuracy_score()
print("学習用データ：", learn_data)
print("予測対象：\n", test_data, ", \n予測結果→", result_label)
print("正解率＝", accuracy_score(test_label, result_label))






# (https://qiita.com/hikaru_/items/3d64af35769235471d9c)
# # データ加工・処理・分析モジュール
# import numpy as np
# import numpy.random as random
# import scipy as sp
# import pandas as pd
# from pandas import Series, DataFrame

# # 学習用データとテストデータに分けるためのモジュール（正解率を出すため）
# from sklearn.model_selection import train_test_split
# # アヤメの花(学習するデータ)
# from sklearn.datasets import load_iris

# # アヤメの花データ(150個)
# iris = load_iris()
# # irisをDataFrameで扱う。
# df = pd.DataFrame(iris.data, columns=iris.feature_names)
# # アヤメの種別(ラベル)を追加
# df["target"] = iris.target_names[iris.target]

# # 引数で表示数を変更できます。defaultは5
# df.head()

# # 説明変数X(特徴量4つ×150)と目的変数Y(アヤメの種類×150)に分ける
# X = df.drop('target', axis=1)
# Y = df['target']

# #ここから学習用データとテスト用データに分ける。random_stateは乱数を固定
# X_train, X_test, y_train, y_test = train_test_split(X, Y, random_state=0)



# # k-近傍法（k-NN）
# from sklearn.neighbors import KNeighborsClassifier

# #k-NNインスタンス。今回は3個で多数決。3の値を変更して色々試すと〇
# model = KNeighborsClassifier(n_neighbors=3)
# #学習モデル構築。引数に訓練データの特徴量と、それに対応したラベル
# model.fit(X_train, y_train)

# # .scoreで正解率を算出。
# print("train score:",model.score(X_train,y_train))
# print("test score:",model.score(X_test,y_test))

# # 上記データ
# data = [[5.2, 3.0, 1.5, 0.6]]
# # data = pd.DataFrame(data)
# # データフレーム型に変換する際に、行の名前を指定
# data = pd.DataFrame(data,columns = ["sepal length (cm)", "sepal width (cm)", "petal length (cm)", "petal width (cm)"])

# # 構築したモデルからアヤメの種類を求める
# model.predict(data)

