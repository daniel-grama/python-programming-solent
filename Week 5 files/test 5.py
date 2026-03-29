students = []
num = int(imput("How many records ?"))
for i in range(num):
    name = input("Enter the student name: ")
    age = int(input("Enter the student age: "))
    print("------------------------------------")
    alldata =  [name,age]
    student.append(alldata)
#getting data
print("All data from the list")
for i in students:
    print("Name is ", i[0])
    print("Age is ", i[0])
    print("********************************************")
    