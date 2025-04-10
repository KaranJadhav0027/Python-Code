def param(age):
    if(age<0):
        raise ValueError()
    if(age%2==0):
        print("Age is even")
    else:
        print("Age is odd")
try:
    n=int(input("Enter your age : "))
    param(n)
except ValueError:
    print("Only positive integers are allowed ")
except:     #can not handle this except block...
    print("Something wrong ")
    
