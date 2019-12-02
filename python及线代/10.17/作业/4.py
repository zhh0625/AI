import numpy as np
A=np.random.randn(200,500)
B=np.random.randn(500,500)
def fun(l):
    return np.dot(A,np.dot(B,1*np.eye(500)))

res1=A+A
res2=np.dot(A,A.T)
res3=np.dot(A.T,A)
res4=np.dot(A,B)
i=int(input("lambda:"))
res5=fun(l)