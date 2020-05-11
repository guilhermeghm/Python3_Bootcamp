#Define a function called generate_evens
#It should return a list of even numbers between 1 and 50(not including 50)

#My solution
def generate_evens():
    even =[]
    for num in range(1,50):
        if num % 2 == 0:
            even.append(num)
    print(even)
    print(type(even))
    return even

generate_evens()


#Official answers
#Using a list comprehension:
def generate_evens():
    return [x for x in range(1,50) if x%2 == 0]


#using a loop:
def generate_evens():
    result = []
    for x in range(1,50):
        if x % 2 == 0:
            result.append(x)
    return result
