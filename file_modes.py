"""
with open("haiku.txt", "a") as file:
    file.write("Here's one more haiku\n")
    file.write("What about the older one?\n")
    file.write("Let's check the old one\n")


with open("haiku.txt", "a") as file:
    file.seek(0)
    file.write(" :)\n")
"""

with open("haiku.txt", "r+") as file:
    file.write("Added Using R+ =)")
    file.seek(10)
    file.write( ":(")
