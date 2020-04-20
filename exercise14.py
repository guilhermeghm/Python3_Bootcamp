from random import randint  # use randint(a, b) to generate a random number between a and b

number = 0 # store random number in here, each time through
i = 0  # i should be incremented by one each iteration


while number != 5:
    number = randint(1,10)
    i += i + 1
    print(f"This is the number {number}")
    print(f"This is the loop control: {i}")
