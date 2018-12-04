n1=0
n2=1
n3=0
x=int(input("ENTER THE NUMBER OF TERMS IN SERIES="))
if x==1:
    print("FIBONNACI SERIES:")
    print(n1)
elif x==2:
    print("FIBONNACI SERIES:")
    print(n1)
    print(n2)
else:
    print("FIBONNACI SERIES:")
    print(n1)
    print(n2)
    while x>2:
        n3=n1+n2
        print(n3)
        n1=n2
        n2=n3
        x-=1
