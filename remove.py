name = ["gwapo", "pogi", "handsome"]
print(name)

kuan = input("Do you want to delete it by index or by name?" " " "if by index type index " " " "if by name type names :")

if kuan == "index":
    name.pop(int(input("select num :")))
    print(name)

elif kuan == "names":
 name.remove(input("select name :"))
 print(name)
