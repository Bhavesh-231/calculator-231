#PROGRAM FOR MINI CALCULATOR
print("list of operations")
print("1.add")
print("2.sub")
print("3.multiplication")
print("4.division==>we get quotient")
print("5.modulus==>we get remainder")
print("6.power")
i=int(input("select the operation :"))
if i==1:
    n1=int(input("enter the first number:"))
    n2=int(input("enter the second number:"))
    print(n1+n2)
elif i==2:
    n1=int(input("enter the first number:"))
    n2=int(input("enter the second number:"))
    print(n1-n2)
elif i==3:
    n1=int(input("enter the first number:"))
    n2=int(input("enter the second number:"))
    print(n1*n2)
elif i==4:
    n1=int(input("enter the first number:"))
    n2=int(input("enter the second number:"))
    print(n1/n2)
    print("we get quotient")
elif i==5:
    n1=int(input("enter the first number:"))
    n2=int(input("enter the second number:"))
    print(n1%n2)
    print("we get reminder")
elif i==6:
    n1=int(input("enter the first number:"))
    n2=int(input("enter the second number:"))
    print(n1**n2)
else:
    print("out of range")

        


      

    
