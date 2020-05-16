def square(num): return num * num
print(square(9))
print(square.__name__)

square2 = lambda num: num * num
print(square2(7))
print(square2.__name__)

add = lambda a,b: a + b
print(add(3,10))
print(add.__name__)
