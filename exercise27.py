##My solution
artist = {
    "first": "Neil",
    "last": "Young",
}
full_name = artist["first"]
full_name += " "
full_name += artist["last"]
print(full_name)

##Offical solution
#Using string concatenation:
artist = {
    "first": "Neil",
    "last": "Young",
}

# concat first and last name with a space
full_name = artist["first"] + " " + artist["last"]


#Using the format() method:
artist = {
    "first": "Neil",
    "last": "Young",
}

full_name = "{} {}".format(artist["first"],artist["last"])

#Using F-String
artist = {
    "first": "Neil",
    "last": "Young",
}

full_name = f"{artist['first']} {artist['last']}"
