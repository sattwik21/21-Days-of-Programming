def frequency(b,j):
    temp=0
    while(b>0):
        if(b % 10 == j):
            temp+=1
        b=int(b/10)
    print("the frequency of " + str(j)+" = "+str(temp))
a=int(input("Enetr a number"))
for i in range (0,10):
    frequency(a,i)
