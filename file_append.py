file=open("Nalini.txt","a")
file.write("\n hello students !! ")
file.close()

file=open("Nalini.txt","r")
print("The updated file is : ")
print(file.read())
file.close()
