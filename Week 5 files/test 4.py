students = []
name = input("Enter your name")
age = input("Enter your age")
data = [name,age]
students.append(data)
print("**********All Data from the student list**********")
for i in students:
    print("Name is ", i[0])
    print("Age is ", i[1])
    