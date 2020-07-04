a=int(input("Enter the first number"))
b=int(input("Enbter the last number"))
for i in range(a,b+1):
    if i>1:
        for j in range(2,i//2+2):
            if i%j==0:
                break
            else:
                if j==i//2+1:
                    print(i,end=" ")
            
        
