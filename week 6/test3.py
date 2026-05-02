names = ["Sharjeel", "John", "Piotr"]
option = int(input("How many names: "))
for i in range(option):
 othernames = input("Enter the name")
 names.append(othernames)
for i in names:
    print(i)