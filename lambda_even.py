def even(n):
    if(n%2==0):
        x=print("Even number")
    else:
        x=print("Odd number ")
    return lambda a:x
even(1)
