users = [
    {"username": "samuel", "tweets": ["I love cake", "I love pie"]},
    {"username": "katie", "tweets": ["I love cat"]},
    {"username": "jeff", "tweets": []},
    {"username": "bob123", "tweets": []},
    {"username": "doggo_luvr", "tweets": ["dogs are the best", "I'm hungry"]},
    {"username": "guitar_gal", "tweets": []}
]

#Extract inactive users using filter:
inactive_users = list(filter(lambda u: len(u['tweets']) == 0, users))

#Extract inactive users using filter in a simpler way:
inactive_users = list(filter(lambda u: not u['tweets'],  users))

#Extract inactive users using list comprehension:
inactive_users2 = [user for user in users if not user["tweets"]]

#Extract usernames of inactive users w/ map and filter:
usernames = list(map(lambda user: user["username"].upper(),
    filter(lambda u: not u['tweets'], users)))

#Extract usernames of inactive users w/ list comprehension:
usernames2= [user["username"].upper() for user in users if not user["tweets"]]


print(inactive_users)
print(usernames2)
