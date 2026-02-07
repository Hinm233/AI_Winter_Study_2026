import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams["font.sans-serif"]=["SimeHei"]
plt.rcParams["axes.unicode_minus"]=False
# 1. 读取CSV数据（核心：指定编码utf-8，避免中文乱码）

df=pd.read_csv("D:\\寒假学习计划_Linux\\Pandas_Project\\user_consumer.csv",encoding="utf-8")

# # 2. 初步探索数据：5个核心函数
# print("="*50, "数据前5行", "="*50)
# print(df.head())# 预览前5行，了解数据格式
# # 查看行/列数、字段类型、非空值数量（核心：发现空值/类型问题）
# print("\n" + "="*50, "数据基本信息", "="*50)
# df.info()
#
# # 仅对数值列生效：均值、最值、四分位数等
# print("\n" + "="*50, "数值字段统计特征", "="*50)
# print(df.describe())
# # 统计每列空值数量
# print("\n" + "="*50, "空值统计", "="*50)
# print(df.isnull().sum())
# # 统计重复行数量
# print("\n" + "="*50, "重复值统计", "="*50)
# print(df.duplicated().sum())
#

# 数据清洗：创建副本，避免修改原数据（新手推荐

df_clean=df.copy()
# 1. 处理重复值：删除所有重复行，保留第一次出现的（核心：subset=None表示按所有列判断）第一次出现keep="first"
df_clean=df_clean.drop_duplicates(keep="first")
# 2. 处理空值：支付金额列（数值列）用**中位数**填充（比均值更抗极端值）
# 为什么用中位数？若存在大额订单（如5000元），均值会被拉高，中位数更贴合实际
x=df["pay_amount"].median()
df_clean["pay_amount"]=df_clean["pay_amount"].fillna(x)
# 3. 日期类型转换：将order_time从字符串转为datetime类型（Pandas时间分析核心）
df_clean["order_time"]=pd.to_datetime(df_clean["order_time"])

# 新增时间衍生字段：年、月、日（后续按月份分析消费趋势）
df_clean["order_year"]=df_clean["order_time"].dt.year
df_clean["order_month"]=df_clean["order_time"].dt.month
df_clean["order_day"]=df_clean["order_time"].dt.day
# print("日期类型转换完成，新增年月日字段")
# #.unique()是pandas获取列的唯一值的常用方法
#
# print("\n商品品类唯一值：",df_clean["product_type"].unique())
# print("支付方式唯一值：",df_clean["pay_type"].unique())
#
# print("\n"+"="*50,"清洗后数据检查","="*50)
# print(f"空值数量：{df_clean.isnull().sum()}")
# print(f"重复值数量：{df_clean.duplicated().sum()}")
# df_clean.info()


# 特征工程：基于清洗后的数据创建衍生特征
df_analysis=df_clean.copy()

# 按用户分组，计算每个用户的消费频次和客单价（核心：groupby+聚合)
user_analysis=df_analysis.groupby("user_id").agg({
    "order_id":"count",
    "pay_amount":["sum","mean"]

}).reset_index()
# 重命名列
user_analysis.columns=["user_id","order_count","total_amount","avg_amount"]
# print("="*50,"用户消费特征","="*50)
# print(user_analysis.head(10).round(2))


# 按月份
month_analysis=df_analysis.groupby("order_month").agg({
    "order_id":"count",
    "pay_amount":"sum"
}).reset_index()
# print(month_analysis)
month_analysis.columns=["month","order_num","total_amount"]
# print("="*50,"月度消费特征","="*50)
# print(month_analysis.head(10).round(2))


# 按商品种类
product_analysis=df_analysis.groupby("product_type").agg({
    "order_id":"count",
    "pay_amount":"sum"
}).reset_index()
# print(product_analysis)
product_analysis.columns=["product","order_num","total_amount"]
# print("\n" + "="*50, "品类消费特征", "="*50)
# print(product_analysis.head(10).round(2))


print(df_analysis.head(10).round(2).to_string())
df_analysis=pd.merge(df_analysis,user_analysis,on="user_id",how="left")
print("="*50,"===========")
# df_analysis.info()

print("="*50,"===========")
print(df_analysis.head(10).round(2).to_string())