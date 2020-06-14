class GrumpyDict(dict):
    def __repr__(self):
        print("None of your business")
        return super().__repr__()

    def __missing__(self, key):
        print(f"You want {key}? Well it ain't here!")

data = GrumpyDict({"first": "Tom", "animal": "cat"})
print(data)
data['city']
