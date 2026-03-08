math = int(input("Enter math marks: "))
biology = int(input("Enter biology marks: "))
db = int(input("Enter chemistry marks: "))
total = math + biology + db
average = total / 3
print("Total marks: ", total, "Average marks: ", average)
if average < 40 and average >= 0:
    print("Fail")
elif average >= 40 and average < 50:
    print("Pass")
elif average >= 50 and average < 60:
    print("Merit")
elif average >= 60 and average <= 100:
    print("Distinction")

