def Words(S):
    L=0

    for i in range(0,len(S)):
        if (S[i] == " "):
            L=L+1
    print(L+1)

S=input("Enter a sentence: ")
Words(S)