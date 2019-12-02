# 1. 以字典为基础建立一个通讯录，向字典中添加和删除通讯人（名字、电话、email、工作单位等），查询某个人的信息，然后输出通讯录中所有人的信息
# 代码：
# class addresslist():
#     def __init__(self):
#         self.name=input("please input name:")
#         self.list=ast.literal_eval(input("please input [telephone,email,workaddress]:"))
#         self.dict={self.name:self.list}
#     def add(self):
#         self.dict.update({self.name:self.list})
#     def delete1(self,name):
#         del self.dict[name]
#
#
# 2. 编写程序，计算圆的周长、面积和球的表面积、体积
# 代码：
# import math
# a=int(input("a number is:"))
# c=2*math.pi*a
# s1=2*math.pi*(a**2)
# v=4/3*math.pi*(a**3)
# s2=4*math.pi*(a**2)
# print("圆的周长:",c)
# print("圆的面积:",s1)
# print("球的体积:",v)
# print("球的面积:",s2)
#
# 3. 编写程序，实现华氏温度和摄氏温度的转换
# 代码：
# temp=input("a temperature is:")
# if temp[-1] in ['F','f']:
#     c=(eval(temp[:-1])-32)/1.8
#     print("转换为摄氏温度:",c)
# elif temp[-1] in ['C','c']:
#     f=(eval(temp[:-1])*1.8)+32
#     print("转化为华氏温度:",f)
# else:
#     print("输入错误")
#
#
# 4. 创建文件data.txt,文件共100000行，每行存放一个1～100之间的整数
# 代码：
# import random
# f=open("data.txt","w")
# for i in range(0,100000):
#     f.write(str(random.randint(1,100))+"\n")
# f.close()
# f=open("data.txt","r").readlines()
# for line in f:
#     print(line,end="")
#
# 5. 写一个程序，从input.txt中读取之前输入的数据，存入列表中，再加上行号打印显示；格式如下
# #第一行： xxxx
# #第二行： xxxx
# 代码：
# with open(r"hello.txt","r") as f:
#     lines = f.readlines()
#     c=1
#     # print(lines)
#     for i in lines:
#         # print(i)
#         print("#第{}行{}".format(c,i))
#         c=c+1
#
# 6.编写一个程序，提示用户输入两个数字，再将它们相加并打印结果。
# 在用户输入的任何一个值不是数字时都捕获ValueError异常，并打印一条友好的错误消息。
#代码：
try:
    a=int(input("a number is:"))
    b=int(input("a number is:"))
    print("the sum is:",a+b)
except:
    print("please input a number:")
