'''
import pdb

first = "First"
second = "Second"
pdb.set_trace()
result = first + second
third = "Third"
result += third
print(result)
'''

def add_numbers(a, b, c, d):
    import import pdb; pdb.set_trace()

    return a + b + c + d

#If the variable have the same name of the pdb command, add p in front of the variable.

#import pdb
#pdb.set.trace()

#Also commonly on one line:
#import pdb; pdb.set_trace()

#Common PDB Commands:
# l (list)
# n (next line)
# p (print)
# c (continue - finishes debugging)
