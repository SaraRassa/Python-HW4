def WordLenght(S):
    L=len(S)

    for i in range(0,len(S)):
        if (S[i] == " "):
            L=L-1
    print(L)

S=input("Enter a sentence: ")
WordLenght(S)