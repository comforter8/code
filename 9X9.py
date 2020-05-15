#!/usr/bin/env python3
i = 1        
print("*" * 66)
while i < 10:
    I = 62
    print("*",end=' ')
    n = 1
    while n <= i:
        print("{}X{}={}".format(i,n,i * n),end=' ')
        n += 1
        I -= 6
    if i == 4:
        print(" " * (I - 2),end=' ')
    elif i >= 5:
        print(" " * (I - (i - 1)),end=' ')
    else:
        print(" " * I,end=' ')
    print("*")
    i += 1
print("*" * 66)
