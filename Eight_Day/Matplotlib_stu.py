# import matplotlib.pyplot as plt
# import numpy as np
#
#
# plt.rcParams["font.sans-serif"]=["SimHei"]
# plt.rcParams["axes.unicode_minus"]=False
# x=np.linspace(0,10,100)
# y1=x**2
# y2=x*3
# # 画纸张plt.figure()
#
# plt.figure()
# plt.subplot(1,2,1)
# plt.plot(x,y1,color="red")
#
# plt.title("y=x**2折线图")
#
# plt.grid()
#
# plt.subplot(1,2,2)
# plt.plot(x,y2,color="blue")
# plt.title("Y=3x")
# plt.grid()
#
# # plt.tight_layout()
# plt.show()
# import numpy as np
# import matplotlib.pyplot as plt
#
# plt.rcParams["font.sans-serif"]=["SimHei"]
# plt.rcParams["axes.unicode_minus"]=False
#
# x=np.arange(0,10)
# y=x*2
# plt.figure()
#
# plt.subplot(2,2,1)
# plt.plot(x,y,marker="o",ms=2,color="r",ls=":")
# plt.title("One_plt")
# plt.xlabel("one_X")
# plt.ylabel("one_Y")
# plt.grid()
#
# x=np.array([4,2,5,10,9])
# y=np.array([1,4,2,5,1])
# plt.subplot(2,2,2)
# plt.plot(x,y,color="k")
# plt.title("One_plt")
# plt.grid()
#
# x=np.arange(0,4*np.pi,0.1)
# y=np.sin(x)
#
# plt.subplot(2,2,3)
# plt.plot(x,y,color="g")
# plt.title("One_plt")
# plt.grid()
#
# x=np.linspace(0,10)
# y=x**2
#
# plt.subplot(2,2,4)
# plt.plot(x,y,color="y")
# plt.title("One_plt")
# plt.grid()
#
# plt.suptitle("4X4图")
#
# plt.show()
import matplotlib.pyplot as plt
import numpy as np


plt.rcParams["font.sans-serif"]=["SimHei"]
plt.rcParams["axes.unicode_minus"]=False
# 创建一些测试数据 -- 图1
x = np.linspace(0, 2*np.pi, 400)
y = np.sin(x**2)


plt.plot(x,y)
plt.title("图一")

fig,ax=plt.subplots()
ax.plot(x,y)
ax.set_title("图二")

f,(ax1,ax2)=plt.subplots(1,2,sharey=True)
ax1.plot(x,y)
ax1.set_title("图三")
ax2.scatter(x,y)




plt.show()