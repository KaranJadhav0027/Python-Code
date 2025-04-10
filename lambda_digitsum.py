def digitsum(n):
    sum=0
    print("n = ",n)
    while(n>0):
        rem=n%10
        sum=sum+rem
        n=n//10
    print("Digit Sum = ",sum)
    return lambda a:n
digitsum(123)
