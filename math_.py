def add(a,b):
    return a+b

def math(a,b, fn=add):
    return fn(a,b)

def subtract(a,b):
    return a-b

math(2,2)

math(2,2, subtract)
