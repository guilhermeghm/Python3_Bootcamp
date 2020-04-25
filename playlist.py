playlist = {
    'title': 'patagonia bus',
    'author': 'Colt Steele',
    'songs': [
        {'title': 'song1', 'artist': ['blue'], 'duration': 2.5},
        {'title': 'song2', 'artist': ['kitty', 'djcat'], 'duration': 5.25},
        {'title': 'meomeow', 'artist': ['garfield'], 'duration': 2.00}
    ]
}

total_legth = 0
for song in playlist['songs']:
    total_legth += song['duration']

print(total_legth)
