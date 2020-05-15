'''
number_compare(1,1) # "Numbers are equal"
number_compare(1,0) # "First is greater"
number_compare(2,4) # "Second is greater"
'''

#My solution.
def number_compare(num1,num2):
    if num1 == num2:
        return "Numbers are equal"
    if num1 > num2:
        return "First is greater"
    else:
        return "Second is greater"


#Official solution:
def number_compare(a,b):
    if a > b:
        return "First is greater"
    elif b > a:
        return "Second is greater"
    return "Numbers are equal"
