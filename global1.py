num=10
def change():
    global num
    num=num+10
    print("Value is : ",num)
def add():
    global num
    num=num+100
    print("Num : ",num)
change()
add()
