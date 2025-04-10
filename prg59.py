n=int(input("enter no. of elements "))
list1=[]
L=0
for i in range(n):
    num=int(input("enter no : "))
    list1.append(num)
    if(num>L):
        L=num
print("Largest number = ",L)
    
