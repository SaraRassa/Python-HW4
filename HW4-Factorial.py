import math

n=int(input("Enter a number: "))
for i in range(1,n+1):
    if math.factorial(i)==n:
        print("Yes","\n",n,"=" ,i,"!")
        break
if math.factorial(i)!=n:
    print("NO")