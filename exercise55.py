# flesh out intersection pleaseeeee

#My solution
def intersection(list1, list2):
    return [i for i in list1 if i in list2]


#Official solutions
def intersection(l1, l2):
    in_common = []
    for val in l1:
        if val in l2:
            in_common.append(val)
    return in_common

#Or
def intersection(l1, l2):
    return [val for val in l1 if val in l2]

#Or
def intersection(list1, list2):
    return [val for val in set(list1) & set(list2)]
