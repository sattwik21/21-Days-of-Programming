a=int(input("Enter the length of the string"))
b=list(map(int, input().split()))[:a]
b.sort()
i=len(b)-1
while i>=0:
    if b[i]>b[i-1]:
        print(b[i-1])
        break
    else:
        i=i-1
        
