n=int(input("Enter any number "))
rev=0
temp=n
while(n>0):
    rem=n%10
    rev=rev*10+rem
    n=n//10
print(" reverse number = ",rev)
if(temp==rev):
    print("pallindrom number ")
else:
    print("Not pallindrom number ")
