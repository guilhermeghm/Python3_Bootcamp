#Option 1
def print_square_of_7():
    print(7**2)

print_square_of_7()

#Option 2
def square_of_7():
    print("I'm before the return!")
    return 7**2
    print("I'm after the return!")

result = square_of_7()
print(result)
