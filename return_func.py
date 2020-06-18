from random import choice
#We can return funcs from other funcs

def make_laugh_func():
    def get_laugh():
        l = choice(('HAHAHAHA', 'lol', 'tehehe'))
        return l

    return get_laugh

laugh = make_laugh_func()
print(laugh())
