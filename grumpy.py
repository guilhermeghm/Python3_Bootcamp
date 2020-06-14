class GrumpyDict(dict):
    def __repr__(self):
        print("None of your business")
        return super().__repr__()

    def __missing__(self, key):
        print(f"You want {key}? Well it ain't here!")

    def __setitem__(self, key, value):
        print("You want to change the Dictonary?")
        print("Ok Fine...")
        super().__setitem__(key, value)

    def __contains__(self, item):
        print("No it ain't in here!")
        return False

data = GrumpyDict({"first": "Tom", "animal": "cat"})
print(data)
data['city'] = 'Tokyo'
print(data)
'city' in data
