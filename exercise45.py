'''
last_element([1,2,3]) # 3
last_element([]) # None
'''

#My solution
def last_element(list):
    if len(list) == 0:
        return None
    return list.pop()


#Official solution
def last_element(l):
    if l:
        return l[-1]
    return None
