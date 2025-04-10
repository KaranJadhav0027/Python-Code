def pallindrome(n):
    rev=0
    temp=n
    while(n>0):
        rem=n%10
        rev=rev*10+rem
        n=n//10
    print("Reverse No. : ",rev)
    if(temp==rev):
        print("Pallindrome number ")
    else:
        print("Not Pallindrome number ")
pallindrome(201)
