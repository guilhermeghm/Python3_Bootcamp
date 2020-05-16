# Implement your is_all_strings function below:

#My solution:
def is_all_strings(mylist):
    return all(((type(s) == str) for s in mylist))

#Official solution:
def is_all_strings(lst):
    return all(type(l) == str for l in lst)

#Or
def is_all_strings(lst):
    return all([type(l) == str for l in lst])


print(is_all_strings(['a','b','c']))
print(is_all_strings([2, 'a','b','c']))
