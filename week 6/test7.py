grades = {}

name = input("Enter your name: ")

subjects = ["Math", "Biology", "Geography"]

for subject in subjects:
    grade = int(input("Enter your " + subject + " grade: "))

    while grade < 0 or grade > 100:
        print("Incorrect input, please try again!")
        grade = int(input("Enter your " + subject + " grade: "))

    grades[subject] = grade

# calculate total
total = 0
for subject in grades:
    total = total + grades[subject]

# calculate average
average = total / len(grades)

# grading
if average >= 70:
    grade_letter = "A"
elif average >= 60:
    grade_letter = "B"
elif average >= 50:
    grade_letter = "C"
elif average >= 40:
    grade_letter = "D"
else:
    grade_letter = "F"

# pass / fail
if average >= 40:
    result = "Pass"
else:
    result = "Fail"

# output
print()
print("--- Report ---")
print("Name:", name)

for subject in grades:
    print(subject + ":", grades[subject])

print("Average:", average)
print("Grade:", grade_letter)
print("Result:", result)