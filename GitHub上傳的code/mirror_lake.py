"""
File: mirror_lake.py
Name: Teresa Tien
----------------------------------
This file reads in mt-rainier.jpg and
makes a new image that creates a mirror
lake vibe by placing an inverse image of
mt-rainier.jpg below the original one.
"""
from simpleimage import SimpleImage


def reflect(filename):
    """
    讀取原original img的每一個pixel,創造新的blank image 讓寬不變長變兩倍
    1.抓取每一個original img的pixel定義成 new_pixel的名字
    2.從blank image中抓取每一個pixel定義成upper blank -->完成上半部
    3.從blank image中抓取每一個pixel定義成lower blank (原y距離-1-y的新間隔）-->完成下半部
    """
    img = SimpleImage(filename)
    b_img = SimpleImage.blank(img.width, img.height * 2)
    for x in range(img.width):
        for y in range(img.height):
            new_pixel = img.get_pixel(x, y)
            upper_blank = b_img.get_pixel(x, y)
            lower_blank = b_img.get_pixel(x, b_img.height - 1 - y)

            upper_blank.red = new_pixel.red
            upper_blank.green = new_pixel.green
            upper_blank.blue = new_pixel.blue

            lower_blank.red = new_pixel.red
            lower_blank.green = new_pixel.green
            lower_blank.blue = new_pixel.blue
    return b_img


def main():
    """
    show original & reflected 兩張圖
    """
    original_mt = SimpleImage('images/mt-rainier.jpg')
    original_mt.show()
    reflected = reflect('images/mt-rainier.jpg')
    reflected.show()


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
