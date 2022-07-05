R=int(input("Rows= "))
C=int(input("Columns= "))

for i in range(1,R+1):
    for j in range(1,C+1):
        print(" ",i*j," ", end=" ")

    print()