import math

a=int(input("a= "))
b=int(input("b= "))
A=[]
B=[]
CD=[]

for i in range(1,a+1):
    if (a % i)==0:
        A.append(i)

for j in range(1,b+1):
    if (b % j)==0:
        B.append(j)

for n in A:
    if n in B:
        CD.append(n)
GCD=max(CD) #Greatest Common Divisor
print("GCD ",a,",",b,"= ",max(CD))

LCM=((abs(a)*abs(b)) / GCD )   #Least Common Multiple
print("LCM ",a,",",b,"= ",LCM)