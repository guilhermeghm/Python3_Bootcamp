'''
def divide(a,b):
    try:
        result = a/b
    except ZeroDivisionError:
        print("Don't divide by zero please!")
    except TypeError as err:
        print("A and B must be ints or floats")
        print(err)
    else:
        print(f"{a} divide by {b} is {result}")
'''

def divide(a,b):
    try:
        result = a/b
    except (ZeroDivisionError, TypeError) as err:
        print("Something went wrong!")
        print(err)
    else:
        print(f"{a} divide by {b} is {result}")


print(divide(1,2))
print(divide(1,0))
print(divide(1,'a'))
