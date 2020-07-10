a=int(input("Enter any number"))
b=0
for i in range(1,a+1):
    if a%i==0 and i%2==1:
        b=b+i
print("The sum of odd factors is",b)
        
