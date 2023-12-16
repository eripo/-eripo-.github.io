from statsmodels.stats.outliers_influence import variance_inflation_factor

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

from sklearn.preprocessing import StandardScaler,MinMaxScaler

import seaborn as sns


# CSVファイルからデータを読み込む
# df = pd.read_csv( 'Data/all_fm_Initial.csv' )
# df = pd.read_csv( 'Data/all_pm_Initial.csv' )
# df = pd.read_csv( 'Data/all_fm_Final.csv' )
df = pd.read_csv( 'Data/all_pm_Final.csv' )
# df = pd.read_csv( 'Data/all_mm_Initial.csv' )
# df = pd.read_csv( 'Data/all_mm_Final.csv' )
# df = pd.read_csv( 'Data/all_mm_Final.csv' , dtype={'1/5_accelerationR_median': float} )


df1 = df.dropna(how='any')
print("######################")
print(df1)
print( df1.corr() ) 
print("######################")
# # 'Mode'列を数値型に変換（例: ワンホットエンコーディング）
# df1 = pd.get_dummies(df1, columns=['Mode'], drop_first=True)
# ワンホットエンコーディング
df_encoded = pd.get_dummies(df1, columns=['Mode'], drop_first=True)


df_dummies = pd.get_dummies(df1['Mode'], prefix='Mode')
df1 = pd.concat([df1, df_dummies], axis=1)

df1 = df1.drop('Mode',axis=1)

print(df1)
print( df1.corr() )


# 要らない列を削除する
# df2 = df1.drop(['Mode'], axis=1)
# # Initial向け
# df2 = df.drop(['gapX', 'gapY', 'gap', 'accelerationX', 'accelerationY', 'acceleration', 'msec', 'Mode'], axis=1)
# # Mid向け
# df2 = df.drop(['gapX', 'gapY', 'gap', 'msec', 'Mode'], axis=1)
# Final向け
# df2 = df.drop(['accelerationX_min', 'accelerationX_max', 'accelerationX_mean', 'accelerationX_median', 'accelerationY_min', 'accelerationY_max', 'accelerationY_mean', 'accelerationY_median', 'acceleration_min', 'acceleration_max', 'acceleration_mean', 'acceleration_median', 'Mode'], axis=1)

# cols = df1.select_dtypes(include=[np.number]).columns
# print(cols[0:])
# print(cols[1:])
# # 目的変数と説明変数を選択する
# X = df1[cols[0:]]
# y = df1['Mode']  # 目的変数
# print(X)

#標準化のクラスを生成
stdsc = StandardScaler()
df_standardized = pd.DataFrame(stdsc.fit_transform(df_encoded), columns=df_encoded.columns)
# X_stdsc = stdsc.fit_transform(X)
print(df_standardized)



# 相関行列を計算
correlation_matrix = df_standardized.corr()

# 相関係数のヒートマップを表示
print(correlation_matrix)
# CSVファイルに出力
# correlation_matrix.to_csv('correlation_matrix_Initial.csv', index=False)
correlation_matrix.to_csv('correlation_matrix_pm_Final.csv', index=False)
print('####################')

plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5)
plt.show()





 
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