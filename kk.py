import numpy as np
import matplotlib.pyplot as plt
x1=[1,1.2,1.4,1.46,1.65,1.89,2,2.35,2.47,2.59,2.78,2.9,3,3.29,3.48,3.69,3.91,4,4.19,4.44,4.68,4.87,5]
y1=[0,3.064,3.594,3.439,2.417,0.713,0,-1.342,-1.417,-1.306,-0.827,-0.395,0,1.04,1.392,1.273,0.496,0,-1.279,-2.978,-3.605,-2.349,0]
#输入x与y值
p=np.polyfit(x1,y1,5)#进行5次方程拟合返回系数值
a,b,c,d,e,f=p#赋予系数的值
x2=np.linspace(1,5,1000)
y2=np.polyval(p,x2)#处理x与y值
plt.plot(x1,y1,'ro:',linewidth=1.0,label='original line')
plt.plot(x2,y2,color='blue',linewidth=2.0,label='smooth line')#画图
plt.xlabel('x')
plt.ylabel('f(x)')#设置x与y轴标签
plt.legend(loc='upper right')#显示图例
plt.show()
n=int(input())
A=[]
for i in range(n):
    xun=list(map(int,input().split()))
    A.append(xun)#将各行以列表形式存入一个列表中
style=list(input().split())
dai=list(map(int,input().split()))
S=[]
for i in range(n):
    S.append(dai)#将待测样本存入n次
B=np.array(A)
C=np.array(S)#将列表转化为矩阵
D=B-C
D=D**2
result=D.sum(axis=1)#进行计算，得到一个1*n的结果矩阵
result1=list(result)
n=result1.index(min(result1))#将矩阵转化为列表形式取最小值
print(style[n])
