from numpy.random import randint


red = (255, 0, 0)
black = (0, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
gray200 = (200, 200, 200)

def random_color():
    return randint(0, 255, size=3)
