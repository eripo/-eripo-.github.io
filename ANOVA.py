import numpy as np
from scipy.stats import shapiro, anderson
from scipy.stats import f_oneway

# 各タスクの正解率データを合わせる
# data = [0.9910, 0.9925, 0.9994]

# # Shapiro-Wilk検定
# for i, task_accuracy in enumerate(data, start=1):
#     stat, p_value = shapiro(task_accuracy)
#     print(f"Shapiro-Wilk Test for Task {i}:")
#     print("Test Statistic:", stat)
#     print("P-value:", p_value)
#     print()

# # Anderson-Darling検定
# for i, task_accuracy in enumerate(data, start=1):
#     result = anderson(task_accuracy)
#     print(f"Anderson-Darling Test for Task {i}:")
#     print("Test Statistic:", result.statistic)
#     print("Critical Values:", result.critical_values)
#     print("Significance Level:", result.significance_level)
#     print()

# ANOVAの実施
f_statistic, p_value = f_oneway([0.9910], [0.9925], [0.9994])

# 結果の表示
print("F-statistic:", f_statistic)
print("P-value:", p_value)