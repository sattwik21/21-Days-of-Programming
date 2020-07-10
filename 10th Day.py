a=list(map(int, input("Enter a string\n").split()))
b=a[0]
a[0]=a[len(a)-1]
a[len(a)-1]=b
print("The new string is\n",a)
