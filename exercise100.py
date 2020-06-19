'''
print_users() # None
# prints to the console:
# Colt Steele
'''

from csv import DictReader
def print_users():
    with open("users.csv") as file:
        csv_reader = DictReader(file)
        for row in csv_reader:
            print(row['First Name'] + " " + row['Last Name'])

#Official solution
import csv

def print_users():
    with open("users.csv") as csvfile:
        csv_reader = csv.DictReader(csvfile)
        for row in csv_reader:
            print("{} {}".format(row['First Name'], row['Last Name']))

print_users()
