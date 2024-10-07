name = ["sayber", "micco","tantan","elfred"]

user = input("you want to alphabetical or reverse? sort or reverse:")

if user == "sort":
    name.sort()
    print(name)
elif user == "reverse":
    name.reverse()
    print(name)