# -*- coding: utf-8 -*-
"""
Created on Sun Jul  9 15:46:09 2017

@author: lenovo
"""

from numpy import *
import numpy as np
################矩阵的创建
a1 = array([1,2,3])
a1=mat(a1)
#3*3 全0，默认浮点数
data1 = mat(zeros((3,3)))
#3*3 全1，默认浮点数
data2 = mat(ones((2,4)))
#3*3 全1，设置参数为int
data3 = mat(ones((2,4)),dtype=int)
#2*2 随机生成浮点数
data4 = mat(random.rand(2,2))
#3*3 前两个设置上下界，为int
data5 = mat(random.randint(0,10,(3,3)))
#9*9 对角线为1的对角矩阵
data6 = mat(eye(9,9,dtype = int))
a2 =[1,2,3]
#对角线为诶1,2,3的对角矩阵
a2 = mat(diag(a2))
#print(a2)

################矩阵乘法
a1 = mat([1,2])
a2 = mat([[1],[2]])
a3 = a1*a2
#print(a3)

################矩阵对应元素相乘
a1 = mat([1,1])
a2 = mat([2,2])
a3 = multiply(a1,a2)
#print(a3)

################矩阵点乘
a3 = a1*10
#print(a3)

################矩阵求逆
a1 = mat(eye(2,2))*0.5
a2 = a1.I
#print(a2)

#################矩阵转置
a1 = mat([[1,1],[0,0]])
a2=a1.T
#print(a2)

a1 = mat([[1,1],[2,3],[4,2]])
################计算每一列，每一行的和
a2=a1.sum(axis=0)  #列和
a3=a1.sum(axis=1)  #行和
a4=sum(a1[0,:]) #第0行所有列的和
a5=sum(a1[:,0]) #第0列所有行的和
#print(a2)
#print(a3)
#print(a4)
#print(a5)

#################计算最大，最小值和索引
a3 = a1.max() #所有元素的最大值，是数值
a2 = max(a1[:,0]) #第0列的最大值，是1*1的矩阵
a4=a1[0,:].max() #第0行的最大值，是数值
#print(a3)
#print(a2)
#print(a4)

a5 = np.max(a1,0)#计算所有列的最大值，得到矩阵
a6 = np.max(a1,1)#计算所有行的最大值，得到矩阵
#print(a5)
#print(a6)

a7 = np.argmax(a1,0)
a8 = np.argmax(a1[2,:])
#print(a7) #计算所有列最大值的索引 矩阵
#print(a8) #计算第2行最大值对应索引 数值

#################矩阵的分隔
a1 = mat(ones((3,3)))
a2=a1[1:,1:]
#print(a2) #分隔出第一行以后的行和第一列以后的列

##################矩阵的合并（保证两个矩阵在同样的方向拥有同样的维度）
a1 = mat(ones((2,2)))
a2 = mat(eye(2))
a3 = vstack((a1,a2)) #按列合并，增加行数
a4 = hstack((a1,a2)) #按行合并，增加列数
#print(a3) 
#print(a4)

###############类型转化
a=array([[1],[2],[3]])
dimension=a.ndim
m,n=a.shape
number=a.size  #元素总个数
str=a.dtype  #元素的类型

#print(dimension)
#print(m,n)
#print(number)
#print(str)


a1=[[1,2],[3,2],[5,2]]#列表
a2=array(a1)#将列表转换成二维数组
a3=mat(a1)#将列表转化成矩阵
a4=array(a3)#将矩阵转换成数组
a5=a3.tolist()#将矩阵转换成列表
a6=a2.tolist()#将数组转换成列表
#print(a1)
#print(a2)
#print(a3)
#print(a4)
#print(a5)
#print(a6)

a1=[1,2,3]
a2=array(a1)
a3=mat(a1)
a4=a2.tolist()#这里得到的是[1,2,3]
a5=a3.tolist()#这里得到的是[[1,2,3]]
a6=(a4 == a5)#a6=False
a7=(a4 == a5[0])#a7=True,a5[0]=[1,2,3]
#print(a1)
#print(a2)
#print(a3)
#print(a4)
#print(a5)
#print(a6)
#print(a7)

##################矩阵与数值
dataMat=mat([1,2,3])
val=dataMat[0,1]#这个时候获取的就是矩阵的元素的数值，而不再是矩阵的类型
print(val)