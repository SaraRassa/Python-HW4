from tkinter.tix import ROW


def CheckerBoard(r,c):

    for j in range(r):
        if j%2==0:
            for i in range(c):
                if i%2==0:
                    print("*",end="")
                else:
                    print("#",end="")
        else:
            for i in range(c):
                if i%2==0:
                    print("#",end="")
                else:
                    print("*",end="")
        print()

r=int(input("Number of rows: "))
c=int(input("Number of columns: "))
CheckerBoard(r,c)