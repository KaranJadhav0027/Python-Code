n=int(input("enter no of elements "))
list1=[]
for i in range(n):
    num=int(input("enter no. "))
    list1.append(num)
for i in list1:
    if(i%2==0):
        print(i)
