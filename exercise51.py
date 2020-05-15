'''
frequency([1,2,3,4,4,4], 4) # 3
frequency([True, False, True, True], False) # 1
'''

#My solution:
def frequency(list,value):
    count = 0
    for i in list:
        if i == value:
            count += 1
    return count


#Official solution:
def frequency(collection, searchTerm):
    return collection.count(searchTerm)
