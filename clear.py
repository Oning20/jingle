number = [1, 2, 3, 4, 5, 6,]
userEnter = input("do you want to delete  the elements? if no you can add elements ")

if userEnter == "yes":
    number.clear()
elif userEnter == "no":
    userElement = int(input("add new elements:"))
    number.append(userElement)

print(number)
