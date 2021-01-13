import random

print("*****************************")
print("Welcome to the guessing game!")
print("*****************************")

chances = 0
points = 1000

while chances == 0:
    print("Choose level:\n(1) easy\n(2) intermediate\n(3) hard")
    level = int(input("Hit 1, 2 or 3:"))

    if level == 1:
        chances = 15
    elif level == 2:
        chances = 10
    elif level == 3:
        chances = 5
    else:
        print("MUST be 1, 2 or 3. Try again:")

secret_number = random.randrange(1, 101)

for guesses in range(0, chances):

    print("You have {} tries".format(chances))
    guess = int(input("Insert your number (1-100): "))
    print("You entered ", guess)

    chances = chances - 1

    if guess < 1 or guess > 100:
        print('MUST be 1-100!')
        continue

    hit = guess == secret_number
    high = guess > secret_number
    low = guess < secret_number

    if hit:
        print("Gotcha! That's the answer of the Universe! You got {} points".format(points))
        break
    else:
        if high:
            print("You missed! Too high.")
        elif low:
            print("You missed! Too low.")
        points = points - abs(guess)

print('Game Over, and thank you for the fish')
