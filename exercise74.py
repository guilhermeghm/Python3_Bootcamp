import keyword

#My solution:
def contains_keyword(*args):
    for i in args:
        if keyword.iskeyword(i):
            return True
    return False

#Official solution:
def contains_keyword(*args):
    for item in args:
        if keyword.iskeyword(item): return True
    return False

print(contains_keyword("hello", "goodbye"))
print(contains_keyword("def", "lol"))
print(contains_keyword("orca", "shark", "return"))
