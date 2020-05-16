def remove_negatives(l):
    positives = list(filter (lambda n: n >= 0, l))
    return positives

print(remove_negatives([-1,3,4,-99,0]))
