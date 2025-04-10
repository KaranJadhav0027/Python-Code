n=int(input("Enter any number "))
sum=0
temp=n
while(n>0):
    rem=n%10
    sum=int(sum+(rem*rem*rem))
    n=n//10
print("Addition = ",sum)
if(temp==sum):
    print("Armstrong number ")
else:
    print("Not Armstrong number ")
