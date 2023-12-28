from statsmodels.stats.outliers_influence import variance_inflation_factor

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
 
#データをインポート
# from sklearn.datasets import load_boston

import pandas as pd
from statsmodels.stats.outliers_influence import variance_inflation_factor

# CSVファイルからデータを読み込む
# df = pd.read_csv( 'Data/all_fm_Initial.csv' )
# df = pd.read_csv( 'Data/all_pm_Initial.csv' )
# df = pd.read_csv( 'Data/all_fm_Final.csv' )
# df = pd.read_csv( 'Data/all_pm_Final.csv' )
# df = pd.read_csv( 'Data/all_mm_Initial.csv' )
df = pd.read_csv( 'Data/all_mm_Final.csv' )

df1 = df.dropna(how='any')

# mm_Initial向け
# 全部（msec除く）
# X1 = df1[['pressure0','intervalTime','gapX','gapY','gap','gapRX','gapRY','gapR','velX','velY','vel','velRX','velRY','velR','accelerationX','accelerationY','acceleration','accelerationRX','accelerationRY','accelerationR','posX','posY','Mode']]
# 目的変数との相関絶対値0.05以上残し
# X1 = df1[['pressure0','intervalTime','gapX','gapY','gap','gapRX','gapRY','gapR','velX','velY','vel','velRX','velRY','velR','accelerationX','acceleration','accelerationRX','accelerationR','posX','posY','Mode']]
# VIF10未満(ここで5未満になったので5未満はなし．) *** 採用！！！！！ ***
# X1 = df1[['pressure0','intervalTime','gapX','gapY','gap','accelerationRX','posX','posY','Mode']]


# 目的変数との相関絶対値0.15以上残し
# X1 = df1[['intervalTime','gapX','gapY','gap','gapRX','gapRY','gapR','velX','vel','velRX','velR','acceleration','accelerationR','posX','posY','Mode']]
# VIF10未満　***採用！！！！***
# X1 = df1[['intervalTime', 'gapX', 'gap', 'gapRY', 'accelerationR', 'posX','posY','Mode']]
# ****************************

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
# X1 = df1[['intervalTime', 'gapY', 'gapR', 'velRX', 'accelerationR', 'posX','posY','Mode']]
# ****************************

## pm_Initial向け ##
# 全部（msec除く）
# X1 = df1[['pressure0','intervalTime','gapX','gapY','gap','gapRX','gapRY','gapR','velX','velY','vel','velRX','velRY','velR','accelerationX','accelerationY','acceleration','accelerationRX','accelerationRY','accelerationR','posX','posY','Mode']]
# 目的変数との相関絶対値0.05以上残し
# 消すものなかった（全部（msec除く）のときと一緒）
# VIF10未満　***採用！！！！***
# X1 = df1[['pressure0','intervalTime','gapX','gap','gapRY','posX','posY','Mode']]


# 目的変数との相関絶対値0.15以上残し
# X1 = df1[['pressure0','intervalTime','gapX','gapY','gap','gapRX','gapRY','gapR','velX','velY','vel','velRX','velRY','velR','accelerationX','accelerationY','acceleration','accelerationRX','accelerationRY','accelerationR','posX','posY','Mode']]
# VIF10未満　***採用！！！！***
# X1 = df1[['pressure0', 'intervalTime', 'gapX', 'gap', 'gapRY', 'posX', 'posY','Mode']]
# ****************************

## fm_Final向け ##
# 全部（msec除く）
# X1 = df1[['velX_min','velX_max','velX_mean','velX_median','velX_first','velX_last','velY_min','velY_max','velY_mean','velY_median','velY_first','velY_last','vel_min','vel_max','vel_mean','vel_median','vel_first','vel_last','velRX_min','velRX_max','velRX_mean','velRX_median','velRX_first','velRX_last','velRY_min','velRY_max','velRY_mean','velRY_median','velRY_first','velRY_last','velR_min','velR_max','velR_mean','velR_median','velR_first','velR_last','accelerationX_min','accelerationX_max','accelerationX_mean','accelerationX_median','accelerationX_first','accelerationX_last','1/5_accelerationX_mean','1/5_accelerationX_median','2/5_accelerationX_mean','2/5_accelerationX_median','4/5_accelerationX_mean','4/5_accelerationX_median','accelerationY_min','accelerationY_max','accelerationY_mean','accelerationY_median','accelerationY_first','accelerationY_last','1/5_accelerationY_mean','1/5_accelerationY_median','2/5_accelerationY_mean','2/5_accelerationY_median','4/5_accelerationY_mean','4/5_accelerationY_median','acceleration_min','acceleration_max','acceleration_mean','acceleration_median','acceleration_first','acceleration_last','1/5_acceleration_mean','1/5_acceleration_median','2/5_acceleration_mean','2/5_acceleration_median','4/5_acceleration_mean','4/5_acceleration_median','accelerationRX_min','accelerationRX_max','accelerationRX_mean','accelerationRX_median','accelerationRX_first','accelerationRX_last','1/5_accelerationRX_mean','1/5_accelerationRX_median','2/5_accelerationRX_mean','2/5_accelerationRX_median','4/5_accelerationRX_mean','4/5_accelerationRX_median','accelerationRY_min','accelerationRY_max','accelerationRY_mean','accelerationRY_median','accelerationRY_first','accelerationRY_last','1/5_accelerationRY_mean','1/5_accelerationRY_median','2/5_accelerationRY_mean','2/5_accelerationRY_median','4/5_accelerationRY_mean','4/5_accelerationRY_median','accelerationR_min','accelerationR_max','accelerationR_mean','accelerationR_median','accelerationR_first','accelerationR_last','1/5_accelerationR_mean','1/5_accelerationR_median','2/5_accelerationR_mean','2/5_accelerationR_median','4/5_accelerationR_mean','4/5_accelerationR_median','pressure_min','pressure_max','pressure_mean','pressure_median','pressure_first','pressure_last','dragTime','widthX','widthY','widthRX','widthRY','Mode']]
# 目的変数との相関絶対値0.1以上残し
# X1 = df1[['velX_min','velX_max','velX_mean','velX_median','velX_first','velX_last','velY_max','velY_last','vel_max','vel_mean','vel_median','vel_first','vel_last','velRX_min','velRX_max','velRX_mean','velRX_median','velRX_first','velRX_last','velRY_max','velRY_last','velR_max','velR_mean','velR_median','velR_first','velR_last','accelerationX_min','accelerationX_max','accelerationX_first','accelerationX_last','1/5_accelerationX_mean','1/5_accelerationX_median','2/5_accelerationX_mean','accelerationY_min','accelerationY_max','accelerationY_last','1/5_accelerationY_mean','acceleration_min','acceleration_max','acceleration_mean','acceleration_median','acceleration_first','2/5_acceleration_mean','4/5_acceleration_mean','accelerationRX_min','accelerationRX_max','accelerationRX_first','accelerationRX_last','1/5_accelerationRX_mean','1/5_accelerationRX_median','2/5_accelerationRX_mean','accelerationRY_last','accelerationR_min','accelerationR_max','accelerationR_median','accelerationR_first','2/5_accelerationR_mean','4/5_accelerationR_mean','dragTime','widthX','widthY','widthRX','Mode']]
# VIF10未満　***採用！！！！***
# X1 = df1[['velX_min','velX_max','velRX_median','velRX_last','velRY_max','velRY_last','velR_median','velR_last','2/5_accelerationX_mean','accelerationY_min','accelerationY_max','1/5_accelerationY_mean','2/5_acceleration_mean','accelerationRX_min','accelerationRX_max','accelerationRX_last','1/5_accelerationRX_mean','1/5_accelerationRX_median','accelerationRY_last','accelerationR_max','accelerationR_median','accelerationR_first','4/5_accelerationR_mean','dragTime','widthX','widthY','Mode']]


# 目的変数との相関絶対値0.3以上残し
# X1 = df1[['velX_min','velX_mean','vel_max','vel_mean','vel_median','vel_last','velRX_min','velRX_mean','velR_max','velR_mean','velR_median','velR_last','accelerationX_max','acceleration_max','widthX','widthRX','Mode']]
# VIF10未満　***採用！！！！***
# X1 = df1[['velRX_min', 'velRX_mean', 'velR_mean', 'velR_median', 'velR_last','accelerationX_max', 'acceleration_max', 'widthRX','Mode']]
# ****************************

## pm_Final向け ##
# 全部
# X1 = df1[['velX_min','velX_max','velX_mean','velX_median','velX_first','velX_last','velY_min','velY_max','velY_mean','velY_median','velY_first','velY_last','vel_min','vel_max','vel_mean','vel_median','vel_first','vel_last','velRX_min','velRX_max','velRX_mean','velRX_median','velRX_first','velRX_last','velRY_min','velRY_max','velRY_mean','velRY_median','velRY_first','velRY_last','velR_min','velR_max','velR_mean','velR_median','velR_first','velR_last','accelerationX_min','accelerationX_max','accelerationX_mean','accelerationX_median','accelerationX_first','accelerationX_last','1/5_accelerationX_mean','1/5_accelerationX_median','2/5_accelerationX_mean','2/5_accelerationX_median','4/5_accelerationX_mean','4/5_accelerationX_median','accelerationY_min','accelerationY_max','accelerationY_mean','accelerationY_median','accelerationY_first','accelerationY_last','1/5_accelerationY_mean','1/5_accelerationY_median','2/5_accelerationY_mean','2/5_accelerationY_median','4/5_accelerationY_mean','4/5_accelerationY_median','acceleration_min','acceleration_max','acceleration_mean','acceleration_median','acceleration_first','acceleration_last','1/5_acceleration_mean','1/5_acceleration_median','2/5_acceleration_mean','2/5_acceleration_median','4/5_acceleration_mean','4/5_acceleration_median','accelerationRX_min','accelerationRX_max','accelerationRX_mean','accelerationRX_median','accelerationRX_first','accelerationRX_last','1/5_accelerationRX_mean','1/5_accelerationRX_median','2/5_accelerationRX_mean','2/5_accelerationRX_median','4/5_accelerationRX_mean','4/5_accelerationRX_median','accelerationRY_min','accelerationRY_max','accelerationRY_mean','accelerationRY_median','accelerationRY_first','accelerationRY_last','1/5_accelerationRY_mean','1/5_accelerationRY_median','2/5_accelerationRY_mean','2/5_accelerationRY_median','4/5_accelerationRY_mean','4/5_accelerationRY_median','accelerationR_min','accelerationR_max','accelerationR_mean','accelerationR_median','accelerationR_first','accelerationR_last','1/5_accelerationR_mean','1/5_accelerationR_median','2/5_accelerationR_mean','2/5_accelerationR_median','4/5_accelerationR_mean','4/5_accelerationR_median','pressure_min','pressure_max','pressure_mean','pressure_median','pressure_first','pressure_last','dragTime','widthX','widthY','widthRX','widthRY','Mode']]
# 目的変数との相関絶対値0.1以上残し
# X1 = df1[['velX_min','velX_max','velX_mean','velX_median','velX_first','velX_last','velY_max','velY_mean','velY_median','velY_first','velY_last','vel_max','vel_mean','vel_median','vel_first','vel_last','velRX_min','velRX_max','velRX_mean','velRX_median','velRX_first','velRX_last','velRY_mean','velRY_median','velRY_first','velRY_last','velR_max','velR_mean','velR_median','velR_first','velR_last','accelerationX_min','accelerationX_max','accelerationX_mean','accelerationX_median','accelerationX_first','accelerationY_min','accelerationY_max','accelerationY_mean','accelerationY_median','accelerationY_first','2/5_accelerationY_mean','4/5_accelerationY_mean','4/5_accelerationY_median','acceleration_min','acceleration_max','acceleration_mean','acceleration_median','acceleration_first','4/5_acceleration_mean','4/5_acceleration_median','accelerationRX_min','accelerationRX_max','accelerationRX_mean','accelerationRX_median','accelerationRX_first','accelerationRY_max','accelerationRY_mean','accelerationRY_median','accelerationRY_first','2/5_accelerationRY_mean','4/5_accelerationRY_mean','4/5_accelerationRY_median','accelerationR_min','accelerationR_max','accelerationR_mean','accelerationR_median','accelerationR_first','4/5_accelerationR_mean','4/5_accelerationR_median','pressure_first','dragTime','widthX','widthY','widthRX','Mode']]
# VIF10未満　***採用！！！！***
# X1 = df1[['velX_max','vel_median','velRX_min','velRX_median','velRX_last','velRY_mean','velRY_median','velRY_last','velR_last','accelerationX_mean','accelerationY_max','accelerationY_mean','acceleration_mean','accelerationRX_median','accelerationRX_first','accelerationRY_median','accelerationRY_first','2/5_accelerationRY_mean','4/5_accelerationRY_mean','4/5_accelerationRY_median','accelerationR_median','accelerationR_first','4/5_accelerationR_mean','4/5_accelerationR_median','pressure_first','dragTime','widthY','widthRX','Mode']]


# 目的変数との相関絶対値0.3以上残し
# X1 = df1[['velX_min','velX_mean','velX_median','velX_last','velY_last','vel_max','vel_mean','vel_median','vel_first','vel_last','velRX_min','velRX_mean','velRX_median','velRX_last','velRY_last','velR_max','velR_mean','velR_median','velR_first','velR_last','accelerationX_min','accelerationX_max','acceleration_min','acceleration_max','acceleration_mean','acceleration_median','acceleration_first','accelerationRX_min','accelerationRX_max','accelerationR_min','accelerationR_max','accelerationR_mean','accelerationR_median','accelerationR_first','widthX','widthRX','Mode']]
# VIF10未満
# X1 = df1[['vel_median', 'velRX_mean', 'velRX_median', 'velRX_last', 'velRY_last','velR_last', 'acceleration_max', 'acceleration_mean','accelerationRX_max', 'accelerationR_min', 'accelerationR_median','accelerationR_first', 'widthRX','Mode']]
# ****************************

## mm_Final向け ##

# 目的変数との相関絶対値0.3以上残し
X1 = df1[['velX_min','velX_mean','velX_median','vel_max','vel_mean','vel_median','vel_last','velRX_min','velRX_mean','velRX_median','velR_max','velR_mean','velR_median','velR_last','acceleration_median','accelerationR_median','widthX','widthRX','Mode']]
# VIF10未満　***採用！！！！***
# X1 = df1[['vel_max', 'velRX_min', 'velRX_mean', 'velRX_median', 'velR_median','velR_last', 'accelerationR_median', 'widthRX','Mode']]

# ****************************


# mm_Final向け
# 目的変数との相関0.3以上残し
# X1 = df1[['velX_min','velX_mean','velX_median','vel_max','vel_mean','vel_median','vel_last','velRX_min','velRX_mean','velRX_median','velR_max','velR_mean','velR_median','velR_last','acceleration_median','accelerationR_median','widthX','widthRX','Mode']]
# VIF10未満
# X1 = df1[['vel_max','velRX_min','velRX_mean','velRX_median','velR_median','velR_last','accelerationR_median','widthRX','Mode']]
# VIF5未満
# X1 = df1[['velRX_min','velRX_median','velR_median','velR_last','accelerationR_median','widthRX','Mode']]

# 目的変数との相関係数絶対値0.1以上残し
# X1 = df1[['velX_min','velX_max','velX_mean','velX_median','velX_first','velX_last','velY_max','velY_mean','velY_last','vel_max','vel_mean','vel_median','vel_first','vel_last','velRX_min','velRX_max','velRX_mean','velRX_median','velRX_first','velRX_last','velRY_max','velRY_last','velR_max','velR_mean','velR_median','velR_first','velR_last','accelerationX_min','accelerationX_max','accelerationX_first','accelerationY_min','accelerationY_max','acceleration_min','acceleration_max','acceleration_median','acceleration_first','2/5_acceleration_mean','accelerationRX_min','accelerationRX_max','accelerationRX_first','accelerationR_min','accelerationR_max','accelerationR_median','accelerationR_first','dragTime','widthX','widthY','widthRX','Mode']]
# VIF10未満 *** 採用！！！！！ ***
# X1 = df1[['velX_min','velX_max','velX_first','velX_last','velY_mean','vel_median','velRX_median','velRY_max','velRY_last','velR_last','accelerationY_min','accelerationY_max','acceleration_max','2/5_acceleration_mean','accelerationRX_min','accelerationRX_max','accelerationR_median','accelerationR_first','dragTime','widthY','widthRX','Mode']]
# VIF5未満
# X1 = df1[['velX_max','velX_last','velY_mean','vel_median','velRX_median','velRY_last','velR_last','accelerationY_min','accelerationY_max','acceleration_max','2/5_acceleration_mean','accelerationRX_min','accelerationRX_max','accelerationR_median','accelerationR_first','dragTime','widthY','widthRX','Mode']]
# VIF10未満かつ特徴量15個以下になるまで目的変数との相関が小さいものから削除
# X1 = df1[['velX_min','velX_max','velX_first','velX_last','vel_median','velRX_median','velRY_last','velR_last','accelerationY_max','acceleration_max','accelerationRX_min','accelerationRX_max','accelerationR_median','accelerationR_first','widthRX','Mode']]
# VIF10未満かつ特徴量10個以下になるまで目的変数との相関が小さいものから削除
# X1 = df1[['velX_min','velX_max','vel_median','velRX_median','velRY_last','velR_last','acceleration_max','accelerationRX_max','accelerationR_median','widthRX','Mode']]

# 全部
# X1 = df1[['velX_min','velX_max','velX_mean','velX_median','velX_first','velX_last','velY_min','velY_max','velY_mean','velY_median','velY_first','velY_last','vel_min','vel_max','vel_mean','vel_median','vel_first','vel_last','velRX_min','velRX_max','velRX_mean','velRX_median','velRX_first','velRX_last','velRY_min','velRY_max','velRY_mean','velRY_median','velRY_first','velRY_last','velR_min','velR_max','velR_mean','velR_median','velR_first','velR_last','accelerationX_min','accelerationX_max','accelerationX_mean','accelerationX_median','accelerationX_first','accelerationX_last','1/5_accelerationX_mean','1/5_accelerationX_median','2/5_accelerationX_mean','2/5_accelerationX_median','4/5_accelerationX_mean','4/5_accelerationX_median','accelerationY_min','accelerationY_max','accelerationY_mean','accelerationY_median','accelerationY_first','accelerationY_last','1/5_accelerationY_mean','1/5_accelerationY_median','2/5_accelerationY_mean','2/5_accelerationY_median','4/5_accelerationY_mean','4/5_accelerationY_median','acceleration_min','acceleration_max','acceleration_mean','acceleration_median','acceleration_first','acceleration_last','1/5_acceleration_mean','1/5_acceleration_median','2/5_acceleration_mean','2/5_acceleration_median','4/5_acceleration_mean','4/5_acceleration_median','accelerationRX_min','accelerationRX_max','accelerationRX_mean','accelerationRX_median','accelerationRX_first','accelerationRX_last','1/5_accelerationRX_mean','1/5_accelerationRX_median','2/5_accelerationRX_mean','2/5_accelerationRX_median','4/5_accelerationRX_mean','4/5_accelerationRX_median','accelerationRY_min','accelerationRY_max','accelerationRY_mean','accelerationRY_median','accelerationRY_first','accelerationRY_last','1/5_accelerationRY_mean','1/5_accelerationRY_median','2/5_accelerationRY_mean','2/5_accelerationRY_median','4/5_accelerationRY_mean','4/5_accelerationRY_median','accelerationR_min','accelerationR_max','accelerationR_mean','accelerationR_median','accelerationR_first','accelerationR_last','1/5_accelerationR_mean','1/5_accelerationR_median','2/5_accelerationR_mean','2/5_accelerationR_median','4/5_accelerationR_mean','4/5_accelerationR_median','pressure_min','pressure_max','pressure_mean','pressure_median','pressure_first','pressure_last','dragTime','widthX','widthY','widthRX','widthRY','Mode']]
# widthX削除前
# X1 = df1[['velX_max','velX_first','velY_min','velY_max','velY_median','velY_first','velY_last','vel_median','vel_first','velRX_min','velRX_max','velRX_mean','velRX_median','velRX_last','velRY_min','velRY_max','velRY_mean','velRY_median','velRY_last','velR_min','velR_max','velR_mean','velR_last','accelerationX_max','accelerationX_mean','accelerationX_last','1/5_accelerationX_median','accelerationY_min','accelerationY_max','accelerationY_median','accelerationY_last','1/5_accelerationY_mean','1/5_accelerationY_median','2/5_accelerationY_mean','2/5_accelerationY_median','4/5_accelerationY_mean','acceleration_mean','acceleration_last','1/5_acceleration_mean','accelerationRX_min','accelerationRX_max','accelerationRX_median','accelerationRX_last','1/5_accelerationRX_mean','1/5_accelerationRX_median','2/5_accelerationRX_mean','2/5_accelerationRX_median','4/5_accelerationRX_mean','4/5_accelerationRX_median','accelerationRY_min','accelerationRY_max','accelerationRY_mean','accelerationRY_median','accelerationRY_first','accelerationRY_last','1/5_accelerationRY_mean','1/5_accelerationRY_median','2/5_accelerationRY_mean','2/5_accelerationRY_median','4/5_accelerationRY_median','accelerationR_min','accelerationR_max','accelerationR_median','accelerationR_first','accelerationR_last','1/5_accelerationR_mean','1/5_accelerationR_median','2/5_accelerationR_mean','2/5_accelerationR_median','4/5_accelerationR_mean','4/5_accelerationR_median','pressure_max','pressure_first','pressure_last','dragTime','widthX','widthY','widthRX','widthRY','Mode']]
# VIF10未満
# X1 = df1[['velX_max','velX_first','velY_min','velY_max','velY_median','velY_first','vel_median','velRX_min','velRX_median','velRX_last','velRY_mean','velRY_last','velR_min','velR_last','accelerationX_mean','accelerationY_median','acceleration_mean','1/5_acceleration_mean','accelerationRX_min','accelerationRX_max','accelerationRX_median','accelerationRX_last','1/5_accelerationRX_mean','1/5_accelerationRX_median','2/5_accelerationRX_median','4/5_accelerationRX_median','accelerationRY_min','accelerationRY_max','accelerationRY_first','accelerationRY_last','1/5_accelerationRY_mean','1/5_accelerationRY_median','2/5_accelerationRY_mean','2/5_accelerationRY_median','4/5_accelerationRY_median','accelerationR_max','accelerationR_median','accelerationR_last','1/5_accelerationR_median','2/5_accelerationR_median','4/5_accelerationR_median','pressure_last','dragTime','widthRX','widthRY','Mode']]
# VIF5未満
# X1 = df1[['velX_max','velX_first','velY_min','velY_max','velY_median','velY_first','velRX_median','velRX_last','velRY_last','velR_min','velR_last','accelerationX_mean','accelerationY_median','acceleration_mean','1/5_acceleration_mean','accelerationRX_median','accelerationRX_last','1/5_accelerationRX_mean','1/5_accelerationRX_median','2/5_accelerationRX_median','4/5_accelerationRX_median','accelerationRY_min','accelerationRY_max','1/5_accelerationRY_median','2/5_accelerationRY_mean','2/5_accelerationRY_median','4/5_accelerationRY_median','accelerationR_max','accelerationR_median','accelerationR_last','1/5_accelerationR_median','2/5_accelerationR_median','pressure_last','dragTime','widthRX','Mode']]


df2 = X1.drop(['Mode'],axis=1)

################# 特徴量VIF10未満まで削除 ########################
cols = df2.select_dtypes(include=[np.number]).columns
print(cols[0:])
# print(cols[1:])
# 目的変数と説明変数を選択する
X = df2[cols[0:]]


def calculate_vif(data_frame):
    vif_data = pd.DataFrame()
    vif_data["Variable"] = data_frame.columns
    vif_data["VIF"] = [variance_inflation_factor(data_frame.values, i) for i in range(data_frame.shape[1])]
    return vif_data

def remove_max_vif_variable(data_frame):
    vif_data = calculate_vif(data_frame)
    max_vif_variable = vif_data.sort_values(by='VIF', ascending=False).iloc[0]['Variable']
    data_frame = data_frame.drop(columns=[max_vif_variable])
    print(f"Removed variable with max VIF: {max_vif_variable}")
    return data_frame

while True:
    vif_data = calculate_vif(X)
    max_vif = vif_data['VIF'].max()

    if max_vif > 10:
        X = remove_max_vif_variable(X)
    else:
        break

print("Final Variables after VIF pruning:")
print(X.columns)
#################################################################


# cols = df2.select_dtypes(include=[np.number]).columns
# print(cols[0:])
# # print(cols[1:])
# # 目的変数と説明変数を選択する
# X = df2[cols[0:]]
# y = df['Mode']  # 目的変数

# # VIFを計算するためのデータフレームを作成する
# vif_data = X.copy()

# # VIFを計算する
# vif = pd.DataFrame()
# vif["VIF Factor"] = [variance_inflation_factor(vif_data.values, i) for i in range(vif_data.shape[1])]
# vif["features"] = vif_data.columns

# # VIFの値を出力する
# print(vif)
# # 最大のVIFを持つ行を取得
# max_vif_row = vif.loc[vif["VIF Factor"].idxmax()]

# # 結果を出力
# # print("最大のVIFを持つ行:")
# print(max_vif_row)
# # print(max(vif["VIF Factor"]))








 
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