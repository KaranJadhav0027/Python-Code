def add():
    sum=a+b
    print("a : ",a)
    print("b : ",b)
    print("Addition : ",sum)
def subtract():
    sub=a-b
    print("a : ",a)
    print("b : ",b)
    print("Subtraction : ",sub)
def multiply():
    multi=a*b
    print("a : ",a)
    print("b : ",b)
    print("Multiplication : ",multi)
def division():
    div=a/b
    print("a : ",a)
    print("b : ",b)
    print("Division : ",div)
def remainder():
    rem=a%b
    print("a : ",a)
    print("b : ",b)
    print("Remainder : ",rem)
a=int(input("Enter first number : "))
b=int(input("Enter second number : "))
ch=0
while(ch<=5):
    print("1:Addition")
    print("2:Subtraction")
    print("3:Multiplication")
    print("4:Division")
    print("5:Remainder")
    ch=int(input("Enter your choice : "))
    if ch==1:
        add()
    elif ch==2:
        subtract()
    elif ch==3:
        multiply()
    elif ch==4:
        division()
    elif ch==5:
        remainder()
    else:
        print("Enter only 1 to 5 choice !!!")
