def G():
    for m in range(1,8):
        for n in range(1,4):
            if m ==1 or m==4 or m==7 or n==1:
                print("*",end = " ")
            else:
                print(" ",end=" ")
        print()

G()
