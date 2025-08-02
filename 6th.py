import random

secret = random.randint(1,100)
attempts = 0

while True:
    guess = int(input("Guess the number(1-100) : "))
    attempts +=1

    if guess < secret:
        print("to low")
    elif guess > secret:
        print("to high")
    else:
        print(f"correct. attempts: {attempts}")
        break