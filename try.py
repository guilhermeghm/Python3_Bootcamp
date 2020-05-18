# The Basic Syntax:
# try:
# except:

'''
try:
    foobar
except:
    print("Problem")
print("After the try")
'''

def get(d, key):
    try:
        return d[key]
    except KeyError:
        return None

d = {"name": "Ricky"}
print(get(d, "city"))
