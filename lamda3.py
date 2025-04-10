def add(a,b):
    return lambda a:a+b
sum=add(2,3)
print("Sum = ",sum(0))
