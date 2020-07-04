s=int(input('enter the number of rows:'))
for x in range(0,s):
    for y in range(s-1,x,-1):
        print(" ",end=" ")
    for z in range(x,-(x+1),-1):
        print(chr(x-abs(z)+65),end=" ")
    print()