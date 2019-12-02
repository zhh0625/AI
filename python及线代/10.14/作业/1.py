# 1. 下面两段代码输出的结果相同么？请解释原因
#  ① x=4，y=5，print（x+y） ② x='4',y='5', print(x+y)
#
#  答：一是整数间加法运算,结果为 9 ；二是字符串之间的拼接操作，结果为 45。
#
# 2.  ‘10/3'，‘10//3’和'10%3'结果相同么？请说明原因
#
# 答：结果分别为：3.333  ，3  ，1。其中，/是除法运算，//所得结果向下取整，也叫地板除，%是取余运算。
#
# 3. a = 3，str(a*3) + str(a)*3的输出是什么?
#
# 答：输出结果为9333。str(a*3)得到的是字符串类型的 9，str(a)*3表示字符串 3 重复3次，加号是字符串拼接。
#
# 4. my_string = 'this is my string', 如何查看这个字符串长度
#
# 答：查看字符串长度用len(str)函数。即len(my_string)
#
# 5. 使用 while 来计算 1 到 100 的总和
# 代码：
# i=1
# sum=0
# while i<=100:
#     sum=sum+i
#     i=i+1
# print(sum)
#
# 6. 输入一年份，判断该年份是否是闰年并输出结果
# 代码：
# year=int(input("a particular year is:))
# a=year%4
# if a==0
#     print("the result is:","是闰年")
# else:
#     print("the result is:","不是闰年")
#
# 7.使用while, 完成以下图形的输出
#
# *
# * *
# * * *
# * * * *
# * * * * *
# * * * *
# * * *
# * *
# *
# 代码：
# n=1
# j=4
# while n<=9:
#     if n<=5:
#         print("*"*n)
#     else:
# 	print("*"*j)
# 	j-=1
#     n+=1
#
#
# 8. 输入两个数，比较大小后，从小到大升序打印
# 代码：
# a=int(input("a number is:"))
# b=int(input("the another:"))
# if a<b:
#     print(a,b)
# else:
#     print(b,a)
#
# 9. 有1、2、3、4个数字，能组成多少个互不相同且无重复数字的三位数？都是多少？
# 代码：
# i=0
# for a in range(1,5):
#     for b in range(1,5):
#         for c in range(1,5):
#             if a!=b and a!=c and b!=c:
#                 print("%d%d%d"%(a,b,c))
#                 i+=1
# print("能组成",i,"个互不相同且无重复数字的三位数")
#
# 10. 一个整数，它加上100后是一个完全平方数，再加上168又是一个完全平方数，请问该数是多少？
# 代码：
# for i in range(1,85):
#     for j in range(1,85):
#         if i%2==0 and j%2==0 or i%2!=0 and j%2!=0:
#             if i**2-j**2==168:
#                 print(j**2-100)
#
# 11. 求200以内能被17整除的最大正整数
# 代码：
# for i in range(200,1,-1):
#     if i%17==0:
#         print(i)
#         break
#
# 12. 输入一个正整数n，对其进行因式分解并输出。
# 例如：输入18，输出18=2*3*3
# 代码：
# import random
# x=int(input("输入一个正整数:"))
# a=list()
# for i in range(2,x+1):
#     while 1:
#         if x%i==0:
#             a.append(i)
#             x/=i
#         else:
#             break
# flag=0
# for i in a:
#     if flag==0:
#         print (i,end='')
#         flag=1
#     else:
#         print('*',i,end='')
#
# 13. 一球从100米高度自由落下，每次落地后反跳回原高度的一半，再落下，
# 求他在第10次落地时，共经过多少米？第10次反弹多高？
# 代码：
# h=100
# h_sum=100
# for i in range(1,11):
#     h=h/2
#     h_sum+=h*2
# print("共经过",h_sum,"米")
# print("第十次反弹",h,"米")
#
# 14. 编写代码，实现求100-200里面所有的素数
# 代码：
# a=[]
# for i in range(100,201):
#     b=0
#     for j in range(2,i-1):
#         if i%j==0:
#             b+=1
#     if b==0:
#         a.append(i)
# print(a)
#
# 15. d={‘a’:1,’b’:2,’c’:3}请打印出key、value对
#代码：
d={'a':1,'b':2,'c':3}
for key in d:
    print(key,d[key])