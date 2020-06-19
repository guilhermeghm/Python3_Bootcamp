'''
delete_users("Grace", "Hopper") # Users deleted: 1.
delete_users("Colt", "Steele") # Users deleted: 2.
delete_users("Not", "Here") # Users deleted: 0.
'''

import csv

def delete_users(first_name, last_name):
    with open ("users.csv") as csvfile:
        csv_reader = csv.reader(csvfile)
        rows = list(csv_reader)

    changes = 0
    with open("users.csv", "w") as csvfile:
        csv_writer = csv.writer(csvfile)
        for row in rows:
            if row[0] == first_name and row[1] == last_name:
                changes +=1
            else:
                csv_writer.writerow(row)

        return "Users deleted: {}.".format(changes)
