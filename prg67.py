import array as a
a=a.array('i',[])
Length=int(input("enter the size of array "))
for i in range(0,Length):
    n=int(input("enter %d elements "%(i+1)))
    a.append(n)
print("given array elements are : ")
for i in a:
    print(i)
