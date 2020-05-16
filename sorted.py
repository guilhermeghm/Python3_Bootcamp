users = [
    {"username": "samuel", "tweets": ["I love cake", "I love pie"]},
    {"username": "katie", "tweets": ["I love cat"]},
    {"username": "jeff", "tweets": []},
    {"username": "bob123", "tweets": []},
    {"username": "doggo_luvr", "tweets": ["dogs are the best", "I'm hungry"]},
    {"username": "guitar_gal", "tweets": []}
]

#By username
sorted(users,key=lambda user: user['username'])

#By the number of tweets
sorted(users,key=lambda user: len(user['tweets']))

#In a reverse order
sorted(users,key=lambda user: len(user['tweets']), reverse=True)
