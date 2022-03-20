for i in range(1,5):
    for j in range(1,5):
        if i==1 or i==4 or i+j==5:
            print("*",end='')
        else:
         print(" ",end='')
    print()