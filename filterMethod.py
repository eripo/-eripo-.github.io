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
import seaborn as sns


import csv

from sklearn.neighbors import KNeighborsClassifier

df = pd.read_csv( 'Data/all_fm_Initial.csv' )
df1 = df.dropna(how='any')

# print(df)
X = df1.drop(['Mode'], axis=1)
y = df1['Mode']


df3 = pd.concat([y,X], axis=1)

#
# 相関関係+ヒートマップ
#
# 相関係数
cor = df3.corr()
# ヒートマップ
sns.heatmap(cor, annot=True)
plt.show()