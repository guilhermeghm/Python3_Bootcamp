#BAD!
#with open("fighters.csv") as file:
#   data = file.read()

#Using reader (as dict)
from csv import reader
with open("fighters.csv") as file:
    csv_reader = reader(file)
    next(csv_reader) #This remove the file header
    for fighter in csv_reader:
        print(f"{fighter[0]} is from {fighter[1]}")
        #each row is a list!
        #print(row)

#Using reader (as list)
from csv import reader
with open("fighters.csv") as file:
    csv_reader = reader(file)
    data = list(csv_reader) #This remove the file header
    print(data)


#Using reader with OrderedDict
from csv import DictReader
with open("fighters.csv") as file:
    csv_reader = DictReader(file)
    for row in csv_reader:
        #each ron is an OrderedDict!
        print(row['Name'])
        print(row) #To print everything.
