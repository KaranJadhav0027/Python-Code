def student(rno,name,m1,m2,m3):
   print("Roll number : ",rno)
   print("Name : ",name)
   print("Java : ",m1)
   print("TCS : ",m2)
   print("OS : ",m3)
   if(m1<35 or m2<35 or m3<35):
        print("Result is fail")
   else:
        total=m1+m2+m3
        per=total/3
        print("Total : ",total)
        print("Percentage : ",per)
        if(per>75):
            print("Distinction")
        elif(60<per<75):
            print("First class")
        elif(50<per<60):
            print("Second class")
        elif(35<per<50):
            print("Pass class")
student(1,'Nalini',56,33,54)
