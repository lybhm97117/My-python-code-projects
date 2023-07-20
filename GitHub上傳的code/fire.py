"""
File: fire.py
Name: Teresa Tien
---------------------------------
This file contains a method called
highlight_fires which detects the
pixels that are recognized as fire
and highlights them for better observation.
"""
from simpleimage import SimpleImage


HURDLE_FACTOR = 1.05


def highlight_fires(filename):
    """
    :param filename: str, original image
    :return: highlight fire location in red pixel, and change other safe location in gray pixel
    """
    highlight = SimpleImage(filename)
    for pixel in highlight:
        avg = (pixel.red + pixel.green + pixel.blue) // 3
        if pixel.red > avg*HURDLE_FACTOR:
            pixel.red = 225
            pixel.green = 0
            pixel.blue = 0
        else:
            pixel.red = avg
            pixel.green = avg
            pixel.blue = avg
    return highlight


def main():
    """
    show original picture and fire_highlight picture
    """
    original_fire = SimpleImage('images/greenland-fire.png')
    original_fire.show()
    highlighted_fire = highlight_fires('images/greenland-fire.png')
    highlighted_fire.show()


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
