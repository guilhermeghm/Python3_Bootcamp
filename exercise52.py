'''
multiply_even_numbers([2,3,4,5,6]) # 48
'''

#My solution.
def multiply_even_numbers(list):
    list = [i for i in list if i % 2 == 0]
    total = 1
    for x in list:
        total *= x
    return total

#Official solution:
def multiply_even_numbers(lst):
    total = 1
    for val in lst:
        if val % 2 == 0:
            total = total * val
    return total
