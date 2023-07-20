"""
File: best_photoshop_award.py
Name:
----------------------------------
This file creates a photoshopped image
that is going to compete for the Best
Photoshop Award for SC001.
Please put all the images you will use in the image_contest folder
and make sure to choose the right folder when loading your images.
"""
from simpleimage import SimpleImage
THRESHOLD = 1.2
BLACK = 120

def main():
    """
    上班blue想放假出去玩
    """
    fig = SimpleImage('image_contest/stitch.jpeg') # 1080x 1440
    fig.show()
    beach = SimpleImage('image_contest/beach2.jpeg')
    new_img = combine(fig, beach)
    new_img.show()

def combine(fig, beach):
    for x in range(fig.width):
        for y in range(fig.height):
            fig_pixel = fig.get_pixel(x,y)
            avg = (fig_pixel.red + fig_pixel.green + fig_pixel.blue) // 3
            total = fig_pixel.red + fig_pixel.green + fig_pixel.blue
            if fig_pixel.green > avg* THRESHOLD and total > BLACK:
                # Blue Screen
                beach_pixel = beach.get_pixel(x, y)
                fig_pixel.red = beach_pixel.red
                fig_pixel.blue = beach_pixel.blue
                fig_pixel.green = beach_pixel.green
    return fig

# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
