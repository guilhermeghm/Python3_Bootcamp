'''
triple_and_filter([1,2,3,4]) # [12]
triple_and_filter([6,8,10,12]) # [24,36]
'''
#My solution
def triple_and_filter(lst):
    return list(3 * (n) for n in lst if n % 4 == 0)


#Official solution
def triple_and_filter(lst):
    return list(filter(lambda x: x % 4 == 0, map(lambda x: x*3, lst)))


print(triple_and_filter([1,2,3,4])) # [12]
print(triple_and_filter([6,8,10,12])) # [24,36]
