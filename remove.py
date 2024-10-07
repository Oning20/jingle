numbers = ("gwapo", "pogi", "handsome")

kuan = input("Do you want to delete it by index or by name?" " " "if by index type INDEX " " " "if by name type NAME:")
if kuan == "INDEX":
    names = int(input("type a num:"))
    numbers.pop(names)
 
elif kuan == "NAME":
    names = input("type a name you want to remove:")
    names.remove(numbers)

print(numbers)
