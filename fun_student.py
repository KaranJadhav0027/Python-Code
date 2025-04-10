def student():
    rno=int(input("Enter any roll number : "))
    name=input("Enter any name : ")
    m1=int(input("Enter marks : "))
    m2=int(input("Enter marks : "))
    m3=int(input("Enter marks : "))
    print("Roll No. : ",rno)
    print("Name : ",name)
    print("Java : ",m1)
    print("TCS : ",m2)
    print("OS : ",m3)
    if(m1<35 or m2<35 or m3<35):
        print("Result is fail !!!")
    else:
        total=m1+m2+m3
        per=total/3
        print("Total : ",total)
        print("Percentage : ",per)
        if(per>75):
            print("Result is Distinction ")
        elif(60<per<75):
            print("Result is first class ")
        elif(50<per<60):
            print("Result is second class ")
        elif(35<per<50):
            print("Result is pass class ")
student()
