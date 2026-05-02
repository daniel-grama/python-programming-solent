import random
secret_number = random.randint(1, 10)
guess = int(input("Guess the number: "))
while guess != secret_number:
    if guess >secret_number:
        print("Too High")
    else:
        print("Too Low")
    guess = int(input("Guess Again: "))
print("Correct! you guessed the number.")