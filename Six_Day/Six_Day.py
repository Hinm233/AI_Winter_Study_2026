
# numpy study

import numpy as np
from numpy.ma.extras import hstack


arr1=np.array([1,2,3,4,5])
arr2=np.array([[1,2,3],[4,5,6]])
arr3=np.array([[1,2],[3,4],[5,6]])

t1=np.array([1,0,1,1,0],dtype=bool)

t2=np.arange(1,10,dtype="int32")
t3=t1.astype(int)
print(t1.dtype)
print(t2.dtype)
print(t3)
print(t3.dtype)

arr_zero=np.zeros(4)
arr_zero1=np.zeros((2,1))
arr_zero2=np.zeros((2,4))
arr_zero_int=np.zeros((2,2),dtype=int)

arr_one1=np.ones(2)
arr_one2=np.ones((2,2))
arr_one3=np.ones((2,2),dtype=int)


arr_eye1=np.eye(4)

arr_arange=np.arange(0,10,2)
# print(arr_arange)
arr_arange1=np.arange(0,10)
# print(arr_arange1)

arr_lin1=np.linspace(0,1,4)
# rand是0~1之间的随机浮点数
arr_random=np.random.rand(2,3)
# print(arr_random)
arr_random_10=np.random.randint(1,[2,3,5])
# print(arr_random_10)
#查看维度
# print(arr2.ndim)
# 查看形状shape
# print(arr2.shape)
#查看元素总数 size
# print(arr2.size)
# 查看数据类型
# print(arr2.dtype)

# reshape()改变数组形状，核心规则：变形前后元素总数必须相等（size不变),常用于将一维数组转为二维矩阵
arr_random_1=np.arange(6)
# print(arr_random_1)
# 转为二维矩阵
arr_random_2=arr_random_1.reshape(2,3)
arr3d=arr_random_2.reshape(2,3,1)
# 自动匹配维度,eg。.reshape(2,-1)>>>2*3  .reshape(-1,2)>>>>3*2

arr_2d=arr_random_1.reshape(-1,1)

# 二维转一维数组
arr_1=arr_random_2.flatten()#返回新数组，原数组不变
arr_1_ravel=arr_random_2.ravel()#返回原数组的视图，更高效率（推荐）


arr_test_1=np.random.randint(2,10,size=10)
arr_test_2=np.random.randint(1,10,size=10)

data=np.hstack([
    arr_test_1.reshape(-1,1),
    arr_test_2.reshape(-1,1)
])

# print(data)
# print(data[:,0])
# print(data[:,1])
# print(data[0:,0])
# print(data[:1,0])

a1=np.arange(10)
a2=a1.reshape((2,5))
# print(a2)

a3=a2.reshape((1,-1))
# print(a3)


# b1=np.arange(0,10).reshape((2,5))
# b2=np.arange(10,20).reshape((2,5))
#
# print(b1,"\n",b2)

# 垂直拼接 vstack
# t3=np.vstack((b1,b2))
# t4=np.vstack((b2,b1))
# print(t3)
# print("-"*100)
# print(t4)
# 水平拼接 hstack
# print("*"*100)
# b3=np.hstack((b1,b2))
# b4=np.hstack((b2,b1))
# print(b3)
# print("*"*100)
# print(b4)

# b1=np.arange(1,13).reshape((3,4))
# b2=np.arange(13,25).reshape((3,4))
#
# b3=np.concatenate((b1,b2),axis=0)
# b4=np.concatenate((b1,b2),axis=1)
# b5=np.concatenate((b1,b2),axis=None)
# print(b3,"\n","*"*100,"\n",
#       b4,"\n","*"*100,"\n",
#       b5,"\n","*"*100)
#

# 行列交换

b1=np.arange(1,13).reshape((3,4))
# print(b1)

b2=np.arange(13,25).reshape((3,4))
# b1[[0,1]]=b1[[1,0]]
# print(b1)
print(b2)
print("-"*100)
# 交换列
b2[:,[0,2]]=b2[:,[2,0]]
print(b2)

b3=np.argmax()