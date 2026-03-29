def add(num1, num2):
    total = num1 + num2
    return total

def average(total):
    avg = total/2
    return avg

def grade(average):
    if average >=40 and average <= 100:
        return "Pass"
    else:
        return "You did not pass"

Math = int(input("Enter Math marks: "))
Bio = int(input("Enter Biology Marks: "))
total = add(Math,Bio)
marks_average = average(total)
grades = grade(marks_average)
print("Total marks are: ", total, " and Average is: ", marks_average, " and Grade is: ", grades)
