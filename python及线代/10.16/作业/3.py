# 1、创建一个长度为10的一维全为0的ndarray对象，然后让第5个元素等于1
# 代码：
# import numpy as f
# a=f.zeros(10,dtype=int)
# print(a)
# print('\n')
# a[4]=1
# print(a)
#
# 2. 创建一个5*3随机矩阵和一个3*2随机矩阵，求矩阵积
# 代码：
# import numpy as f
# a=f.arange(15).reshape(5,3)
# b=f.arange(6).reshape(3,2)
# print(a)
# print('\n')
# print(b)
# print('\n')
# print(f.dot(a,b))
#
# 3. 实现冒泡排序法
# 代码：
# import numpy as f
# a=[12,34,32,54,32,76,3,45,40]
# b=len(a)
# print(b)
# for i in range(b-1):
#     print(i)
#     for j in range(b-1-i):
#         if a[j]>a[j+1]:
#             a[j],a[j+1]=a[j+1],a[j]
# print(a)
#
# 4. 找到数组[1,2,0,0,4,0]中0元素的位置索引
# 代码：
# a=[1,2,0,0,4,0]
# b=[i for i,x in enumerate(a) if x==0]
# print(b)
#
# 5. 创建一个 10x10 的随机数组并找到它的最大值和最小值
# 代码：
# import numpy as f
# a=f.random.randint(0,100,100).reshape(10,10)
# print(a)
# print(f.max(a))
# print(f.min(a))
#
# 6. 求解方程：3x1+3.2x2=118.4        3.5x1+3.6x2=135.2
#代码：
import numpy as f
a=f.array([[3,3.2],[3.5,3.6]])
b=f.array([118.4,135.2])
s=f.linalg.solve(a,b)
print(s)
