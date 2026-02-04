# import pandas as pd

# df = pd.read_csv("D:\\.idea\\property-data.csv")
# print(df["NUM_BEDROOMS"])
#
# print(df["NUM_BEDROOMS"].isnull())

# missing_values=["n/a","na","--"]
# df=pd.read_csv("D:\\.idea\\property-data.csv",na_values=missing_values)
# print(df["NUM_BEDROOMS"])
# print(df["NUM_BEDROOMS"].isnull())

# df=pd.read_csv("D:\\.idea\\property-data.csv")
# #
# new_df=df.dropna()
#
# print(df.to_string())
# print("*"*100)
#
# print(new_df.to_strin())

# df.dropna(subset=["ST_NUM"],inplace=True)
# print(df.to_string())

import pandas as pd

df=pd.read_csv("D:\\.idea\\property-data.csv")
print(df.to_string())
# df.fillna(12,inplace=True)
# print(df.to_string())
# df["PID"].fillna(123,inplace=True)
# print("*"*100)
# print(df.to_string())
# df["NUM_BEDROOMS"].fillna(2,inplace=True)
# print(df.to_string())
# x=df["NUM_BEDROOMS"].mean()
# df["NUM_BEDROOMS"].fillna(x,inplace=True)
# print(df.to_string())
# print(df["ST_NUM"].dtypes)
# x=df["ST_NUM"].mean()
# df["ST_NUM"].fillna(x,inplace=True)
# print(df.to_string())

# x=df["ST_NUM"].median()
# df["ST_NUM"].fillna(x,inplace=True)
# print(df.to_string())

# mode()计算众数
# x = df["ST_NUM"].mode()[0]
#
# df["ST_NUM"].fillna(x, inplace = True)
#
# print(df.to_string())