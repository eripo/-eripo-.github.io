from statsmodels.stats.outliers_influence import variance_inflation_factor

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
 
#データをインポート
from sklearn.datasets import load_boston

import pandas as pd
from statsmodels.stats.outliers_influence import variance_inflation_factor

# CSVファイルからデータを読み込む
# df = pd.read_csv('Data/Initial (5).csv')
# df = pd.read_csv('Data/Mid (5).csv')
df = pd.read_csv('Data/Final (5).csv')

df.dropna()

# 要らない列を削除する
# # Initial向け
# df2 = df.drop(['gapX', 'gapY', 'gap', 'accelerationX', 'accelerationY', 'acceleration', 'msec', 'Mode'], axis=1)
# # Mid向け
# df2 = df.drop(['gapX', 'gapY', 'gap', 'msec', 'Mode'], axis=1)
# Final向け
df2 = df.drop(['accelerationX_min', 'accelerationX_max', 'accelerationX_mean', 'accelerationX_median', 'accelerationY_min', 'accelerationY_max', 'accelerationY_mean', 'accelerationY_median', 'acceleration_min', 'acceleration_max', 'acceleration_mean', 'acceleration_median', 'Mode'], axis=1)

cols = df2.select_dtypes(include=[np.number]).columns
print(cols[0:])
# print(cols[1:])
# 目的変数と説明変数を選択する
X = df2[cols[0:]]
y = df['Mode']  # 目的変数

# VIFを計算するためのデータフレームを作成する
vif_data = X.copy()

# VIFを計算する
vif = pd.DataFrame()
vif["VIF Factor"] = [variance_inflation_factor(vif_data.values, i) for i in range(vif_data.shape[1])]
vif["features"] = vif_data.columns

# VIFの値を出力する
print(vif)




 
# # 標本データを取得
# learn_data = df.drop(['Mode'], axis=1)
# learn_data.dropna()
# print(learn_data);
 
# # 正解データを取得
# learn_label = df['Mode']
# data_y = pd.DataFrame(dataset.target,columns=['target'])
# data_y.dropna()
# print(data_y);

# #vifを計算する
# vif = pd.DataFrame()
# vif["VIF Factor"] = [variance_inflation_factor(data_x.values, i) for i in range(data_x.shape[1])]
# vif["features"] = data_x.columns
 
# #vifを計算結果を出力する
# print(vif)
 
# #vifをグラフ化する
# plt.plot(vif["VIF Factor"])