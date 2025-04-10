f=open("Nalini.txt","w")
s=input("Enter content to be written in the file : ")
f.write(s)
f.close()
print("Now reading the file ")
f=open("Nalini.txt","r")

for str in f:
    print(str)
f.close()
