score = int(input("Enter your score (0-100): "))
if score < 0 or score > 100:
    print("Invalid")
elif score >= 40:
    print("Pass")
else:
    print("Fail")