
def biggerradius(r1,r2,r3):
    print("The biggest of the three numbers is:",end=" ")
    print(big_3(r1,r2,r3))
    z=big_3(r1,r2,r3)
    cal(z)
    
def big_2(a,b):
    if a>b:
        return a
    else:
        return b

def big_3(a,b,c):
    x=big_2(a,b)
    z=big_2(x,c)
    return z

def cal(a):
    area=3.14*(a**2)
    circumfrence=2*3.14*a
    print("The circumfrence of the number is",circumfrence)
    print("the area of the number is",area)

choice=0

while choice!=5:
    print("1)To find the area and circumference using the biggest value")
    print("2)Returning the bigger of two numbers")
    print("3)printing the bigger of three numbers")
    print("4)Finding the area and circumfrence")
    choice=int(input("Enter the choice"))
    
    if choice==1:
        a=int(input("Enter the value:"))
        b=int(input("Enter the value:"))
        c=int(input("Enter the value:"))
        print()
        biggerradius(a,b,c)
        print()
        
    elif choice==2:
        a=int(input("Enter the value:"))
        b=int(input("Enter the value:"))
        print()
        print("The bigger of the two numbers is",big_2(a,b))
        print()
        
    elif choice==3:
        a=int(input("Enter the value:"))
        b=int(input("Enter the value:"))
        c=int(input("Enter the value:"))
        print()
        print("The bigger of the three numbers is",big_3(a,b,c))
        print()
        
    elif choice==4:
        a=int(input("Enter the raduius value:"))
        print()
        cal(a)
        print()
