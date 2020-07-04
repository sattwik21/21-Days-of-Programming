a=int(input("Enter the starting element of the series"))
n=int(input("Enter the number of elements"))
r=int(input("Enter the common ratio"))
s=0
for i in range(1,n+1):
    print(a*(r**(i-1)),end=" ")
    s+=a*(r**(i-1))
print(" ")
print(s)
