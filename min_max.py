names = ['Aria', "Samson", "Dora", "Tim",, "Ollivander"]

min(len(name) for name in names)
max(names, key=lambda n:len(n))


songs = [
    {"title": "happy birthday", "playcount": 1},
    {"title": "Survive", "playcount": 6},
    {"title": "YMCA", "playcount": 99},
    {"title": "Toxic", "playcount": 31}
]

min(songs, key=lambda s: s['playcount'])
min(songs, key=lambda s: s['playcount'])['title']
