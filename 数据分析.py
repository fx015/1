import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pylab import mpl
import numpy as np

mpl.rcParams["font.sans-serif"] = ["SimHei"]
mpl.rcParams["axes.unicode_minus"] = False

df = pd.read_csv("C:/Users/china/Desktop/data-final.csv")

# 计算每列的缺失率
per_mis = list(df.isnull().sum() / len(df))
df_missing = pd.DataFrame({'列名': df.columns, '缺失率': per_mis})
df_missing.sort_values('缺失率', inplace=True, ascending=False)

# 删除所有包含缺失值的行
df.dropna(inplace=True)
assert not df.isnull().sum().any(), "DataFrame中仍存在缺失值"

# 过滤IPC为1的数据，并删除指定列
df = df[df['IPC'] == 1].drop(['dateload', 'lat_appx_lots_of_err', 'long_appx_lots_of_err', 'IPC', 'screenh', 'screenw'], axis=1)

def plot_counts(title, columns):
    plt.figure(figsize=(12, 10))
    for n, column in enumerate(columns, start=1):
        plt.subplot(5, 2, n)
        ax=sns.countplot(x=column, edgecolor="black", alpha=0.7, data=df)
        sns.despine()
         # 设置纵坐标的范围和刻度
        ax.set_ylim(0, 150000)
        ax.yaxis.set_ticks(np.arange(0, 150001, 25000))
        # 设置横坐标的范围
        ax.set_xlim(left=1.0)
    plt.suptitle(title,y=0.99)# 调整suptitle的位置以避免遮挡图表
    plt.tight_layout(rect=[0,0.03,1,0.95])# 调整tight_layout以留出空间给suptitle
    plt.show()
def plot_pie_charts(titles, columns_list):
    plt.figure(figsize=(18, 15))
    for i, (title, columns) in enumerate(zip(titles, columns_list), start=1):
        plt.subplot(3, 2, i)
        counts = pd.concat([df[col] for col in columns]).value_counts().sort_index()
        plt.pie(counts, labels=counts.index, autopct='%1.1f%%', startangle=140)
        plt.title(title)
    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    plt.show()
# 绘制各个维度的问题选项频率分布情况
EXT_title = "十个外向性问题选项频率分布请况"
EST_title = "十个神经质问题选项频率分布请况"
AGR_title = "十个宜人性问题选项频率分布请况"
CSN_title = "十个严谨性问题选项频率分布请况"
OPN_title = "十个开放性问题选项频率分布请况"

EXT_columns = ['EXT1', 'EXT2', 'EXT3', 'EXT4', 'EXT5', 'EXT6', 'EXT7', 'EXT8', 'EXT9', 'EXT10']
EST_columns = ['EST1', 'EST2', 'EST3', 'EST4', 'EST5', 'EST6', 'EST7', 'EST8', 'EST9', 'EST10']
AGR_columns = ['AGR1', 'AGR2', 'AGR3', 'AGR4', 'AGR5', 'AGR6', 'AGR7', 'AGR8', 'AGR9', 'AGR10']
CSN_columns = ['CSN1', 'CSN2', 'CSN3', 'CSN4', 'CSN5', 'CSN6', 'CSN7', 'CSN8', 'CSN9', 'CSN10']
OPN_columns = ['OPN1', 'OPN2', 'OPN3', 'OPN4', 'OPN5', 'OPN6', 'OPN7', 'OPN8', 'OPN9', 'OPN10']

plot_counts(EXT_title, EXT_columns)
plot_counts(EST_title, EST_columns)
plot_counts(AGR_title, AGR_columns)
plot_counts(CSN_title, CSN_columns)
plot_counts(OPN_title, OPN_columns)
# 分别绘制五个饼图对应五个维度EXT，EST，AGR，CSN，OPN的各自选项频率总体情况
titles = [EXT_title, EST_title, AGR_title, CSN_title, OPN_title]
columns_list = [EXT_columns, EST_columns, AGR_columns, CSN_columns, OPN_columns]
plot_pie_charts(titles, columns_list)


