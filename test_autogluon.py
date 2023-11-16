from autogluon.tabular import TabularDataset, TabularPredictor
import pandas as pd
from sklearn.metrics import classification_report
import seaborn as sns #視覚化ライブラリ
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
import japanize_matplotlib

###########################################################################################
# 学習用データとテストデータが分かれている場合 #############################
# 1ファイルを8:2分割する場合 #############################
# データの読み込み
# train_data = TabularDataset('Data/Mid (5).csv')  # トレーニングデータのパス
# test_data = TabularDataset('Data/Mid(1).csv')  # テストデータのパス
# df2 = pd.read_csv( 'Data/Final(1).csv' )
# test_data = df2.drop(['Mode'], axis=1)

# 1ファイルを8:2分割する場合 #############################
# df = pd.read_csv( 'Data/all_fm_initial.csv' )
df = pd.read_csv( 'Data/all_pm_Final.csv' )
print(df)
df1 = df.dropna(how='any')
print(df1)
train_data, test_data = train_test_split(df1, test_size=0.2, random_state=10)
print('訓練データ数：{}, テストデータ数：{}'.format(len(train_data), len(test_data)))
###########################################################################################


# 分類モデルのトレーニング
predictor = TabularPredictor(label='Mode').fit(train_data)

# テストデータで予測を実行
y_pred = predictor.predict(test_data)

print("Predictions:  \n", y_pred)

y_test = test_data['Mode']  # values to predict
perf = predictor.evaluate_predictions(y_true=y_test, y_pred=y_pred, auxiliary_metrics=True)

report = classification_report(y_test, y_pred, output_dict=True)
print("Classification Report: \n", report)

# 
feature_importance = predictor.feature_importance(test_data)
print("Feature Importance: \n", feature_importance)

predictor.leaderboard(test_data)




# グラフのサイズやスタイルを設定
plt.figure(figsize=(8.3, 4))
sns.set_style('whitegrid')  # グリッドを表示するスタイル
sns.set(font='IPAexGothic')  # 日本語フォントを設定

# 特徴量の重要度を棒グラフで表示
sns.barplot(y=feature_importance.index, x='importance', data=feature_importance)

# グラフを表示
plt.show()


# df = pd.read_csv( 'Data/Final (5).csv' )
# # train_data = df.drop(['Mode'], axis=1)
# train_data = df
# subsample_size = 500  # subsample subset of data for faster demo, try setting this to much larger values
# train_data = train_data.sample(n=subsample_size, random_state=0)
# train_data.head()

# label = 'Mode'
# print("Summary of class variable: \n", train_data[label].describe())

# save_path = 'agModels-predictClass'  # specifies folder to store trained models
# predictor = TabularPredictor(label=label, path=save_path).fit(train_data)


# df2 = pd.read_csv( 'Data/Final(1).csv' )
# test_data = df2.drop(['Mode'], axis=1)
# y_test = test_data[label]  # values to predict
# # test_data_nolab = test_data.drop(columns=[label])  # delete label column to prove we're not cheating
# test_data.head()

# # predictor = TabularPredictor.load(save_path)  # unnecessary, just demonstrates how to load previously-trained predictor from file
# y_pred = predictor.predict(test_data)
# print("Predictions:  \n", y_pred)

# perf = predictor.evaluate_predictions(y_true=y_test, y_pred=y_pred, auxiliary_metrics=True)

# predictor.leaderboard(test_data)