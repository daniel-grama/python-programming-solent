names = {"Sharjeel", "Sharjeel", "Marry"}
setnames = int(input("How many names: ?"))
for i in range(setnames):
    newnames = input("Enter the new name: ")
    names.add(newnames) 
for i in names:
    print (i)