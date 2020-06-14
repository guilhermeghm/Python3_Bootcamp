# Custom For Loop

#for num in [1,2,3]
#for char in "hi there"

def my_for(iterable, func):
    iterable = iter(iterable)
    while True:
        try:
            thing = next(iterable)
        except StopIteration:
            break
        else:
            func(thing)

def square(x):
    print(x*x)

my_for("hello", print)
my_for([1,2,3,4,5], square)
