import array as a
a=a.array('i',[])
sum=0
length=int(input("enter size of array "))
for i in range(0,length):
    n=int(input("enter %d element"%(i+1)))
    a.append(n)
print("given array elements are : ")
for i in a:
    print(i)
    sum=sum+i
print("sum=",sum)
