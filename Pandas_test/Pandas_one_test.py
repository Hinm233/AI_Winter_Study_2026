# import pandas as pd
# import numpy as np
#
# series=pd.Series([1,2,3,4],name="A")
#
# # print(series)
#
# serier_index=["A","B","C","D"]
#
# series2=pd.Series([1,2,3,4],index=serier_index,name="A-D")
# # print(series2)
#
# # dic={"A":1,"B":2,"C":3}
# #
# # s1=pd.Series(data=dic)
# # print(s1)
#
# s1=pd.Series(["Google","BaiDu","Amazon"],index=["x","y","z"])
# print(s1["x"])
# print(s1["y"])
# print(s1["z"])

# import pandas as pd

# s1_list=[1,2,3,5,4,6]
# index_s1=["a","b","c","d","e","f"]
# s1=pd.Series(s1_list,index=index_s1)
# # print(s1)
#
# print("s1的数据类型：",s1.dtype)
# print("返回s1的形状（行数）",s1.shape)
# print("累计去和:",s1.cumsum())
#
# # loc通过标签来选择数据
# print(s1.loc["b"])
# # iloc通过位置来选择数据
# print(s1.iloc[0])
#
# # print(s1.rank())
#
# print(s1.sort_values())
#
# print(s1)

# s=pd.Series([1,2,3,4],index=["a",'b',"c","d"])
# index=s.index
# value=s.values
# stats=s.describe()
# max_index=s.idxmax()
# min_index=s.idxmin()
#
# print(index)
# print(value)
# print(stats)
# print(max_index)
# print(min_index)
# import pandas as pd

# df=pd.DataFrame({
#     "姓名": ["张三", "李四", "王五"],
#     "年龄": [20, 25, 30],
#     "城市": ["北京", "上海", "广州"]
# },index=["用户1","用户2","用户3"])
#
# print(df)
# print("-"*100)
# print(df.index)
# print("-"*100)
# print(df.values)
# print("-"*100)
# print(df.columns)
# print("-"*100)
# print(df.dtypes)
# print("-"*100)
# print(df.shape)
# print("-"*100)
# print(df.ndim)
# print("-"*100)

# 创建DataFrame
# data=[["Google",10],["Runoob",12],["wiki",13]]
# df = pd.DataFrame(data,columns=["Site","Age"])
#
# print(df)
# df["Site"]=df["Site"].astype(str)
# df["Age"]=df["Age"].astype(float)
#
# print(df)

# data={
#     "Site":["Google","Runook","wiki"],
#     "Age":[10,12,13]
# }
#
# df=pd.DataFrame(data)
# df["Age"]=df["Age"].astype(float)
# print(df)

# import numpy as np
# import pandas as pd
#
# data=np.array([
#     ["Google",10],
#     ["Runoob",12],
#     ["Wiki",13]
# ])
# df=pd.DataFrame(data,index=["A","B","C"],columns=["Site","Age"])
# print(df)
#
# import pandas as pd
#
# data={
#     "calories":[420,380,390],
#     "duration":[50,40,45]
# }
# df=pd.DataFrame(data)
# print(df)
# print(df.loc[0])
# print(df.loc[1])

# import pandas as pd
# data={
#     "Name":['Alice', 'Bob', 'Charlie', 'David'],
#     "Age":[25, 30, 35, 40],
#     "City":['New York', 'Los Angeles', 'Chicago', 'Houston']
# }
#
# df=pd.DataFrame(data)
#
# print(df)
#
# print("*"*1000)
# # print(df.head(1))
# # print("*"*1000)
# # print(df.tail(2))
# # print("*"*1000)
# # print(df.info())
# # print(df.describe())
# # print(df.shape)
#
# print("*"*1000)
# # print(df.columns)
#
# print("*"*1000)
#
# # print(df.index)

import pandas as pd

# df = pd.read_csv("D:\\.idea\\nba.csv",sep=";",
#                  header=0,names=["A","B","C"],dtype={"A":int,"B":float})
# print(df)

df=pd.read_csv("D:\\.idea\\nba.csv")
print(df)