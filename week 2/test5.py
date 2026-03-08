age = int(input("What's your age? "))
if age < 18:
    print("Minor discount")
elif age >= 18 and age < 65:
    print("Normal price")
elif age >= 65:
    print("Senior discount")