def digit():
    n=int(input("Enter any number : "))
    rem1=n%10
    while(n>0):
        rem2=n%10
        n=int(n/10)
    sum=rem2+rem1
    print("Sum of first and last digit is : ",sum)
digit()   
