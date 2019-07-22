for i in range(8):
    for j in range(8):
        if i==0 or i==7 or j==7-i:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()