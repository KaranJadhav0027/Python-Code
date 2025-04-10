import array as a
a=a.array('i',[])
L=0
length=int(input("Enter the size of array "))
for i in range(0,length):
    n=int(input("enter %d element : "%(i+1)))
    a.append(n)
print("Given array elements are : ")
for i in a:
    print(i)
    if(i>L):
        L=i
print("largest number = ",L)
