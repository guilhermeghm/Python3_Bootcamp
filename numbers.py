#Option 1
print("This is option 1:")
for n in range(1,21):
    if n == 4 or n == 13:
        print(f"{n} is unlucky!")
    elif n % 2 == 0:
        print(f"{n} is even")
    else:
        print(f"{n} is odd")

#Option 2
print("\n")
print("This is option 2:")
for n in range(1,21):
    if n == 4 or n == 13:
        state = "unlucky!"
    elif n % 2 == 0:
        state = "even"
    else:
        state = "odd"
    print(f"{n} is {state}")
