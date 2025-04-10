try:
    a=int(input("Enter a : "))
    b=int(input("Enter b : "))
    c=a/b
    print("Sum = %d"%c)
except Exception:
    print("Can't divide by zero !!")
    print(Exception)
else:
    print("Hi..I am else block")
