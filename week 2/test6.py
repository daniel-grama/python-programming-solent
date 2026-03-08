grade = int(input("what's your grade?: "))
if grade < 40:
    print("Fail")
elif grade >=40 and grade < 50:
    print("D")
elif grade >= 50 and grade <60:
    print("C")
elif grade >= 60 and grade < 70:
    print("B")
elif grade >= 70:
    print("A")