a=int(input("Enter a"))
b=int(input("Enter b"))
c=int(input("Enter c"))
d=b*b-4*a*c
if d>=0:
    e=d**0.5
    print(d)
    print(f'({0-b}+{e})/{2*a}')
    print(f'({0-b}-{e})/{2*a}')
else:
    e=(0-d)**0.5
    print(d)
    print(f'({0-b}+{e}i)/{2*a}')
    print(f'({0-b}-{e}i)/{2*a}')
    
    
    

