
import math

def Quadratic(a,b,c):
    d= b*b - 4*a*c
    if d<0:
        print("No answer!")
    elif d==0:
        x= (-b / a)
        print("x= ",x)
    else:
        x1=(-b + math.sqrt(d))/(2*a)
        x2=(-b - math.sqrt(d))/(2*a)
        print("x1= ",x1, "\nx2= ",x2)

a=float(input("a= "))
b=float(input("b= "))
c=float(input("c= "))
Quadratic(a,b,c)

    

