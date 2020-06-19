with open("haiku.txt", "w") as file:
    file.write("Writing file is great\n")
    file.write("Here's another line of text\n")
    file.write("Closing now, goodbye!")


with open("lol.txt", "w") as file:
    file.write("haha" * 10000)
