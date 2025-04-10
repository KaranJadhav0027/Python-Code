n=int(input("Enter no of elements "))
list1=[]
for i in range(n):
    num=int(input("enter no. "))
    list1.append(num)
print("list is ",list1)
print("Sum of list is ",sum(list1))
avrg=sum(list1)/len(list1)
print("Average of list is ",avrg)
