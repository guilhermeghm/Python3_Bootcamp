def colorize(text, color):
    colors = ("cyan", "yellow", "blue", "green", "magenta")
    if type(color) is not str:
        raise TypeError("Color must be instance of str")
    if type(text) is not str:
        raise TypeError("Text must be instance of str")
    if color not in colors:
        raise ValueError("Color is invalid color")
    print(f"Printed {text} in {color}")

colorize("hello", "red")
colorize(20, "red")
