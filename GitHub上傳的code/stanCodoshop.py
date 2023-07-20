"""
File: stanCodoshop.py
Name: Teresa Tien
----------------------------------------------
SC101_Assignment3 Adapted from Nick Parlante's
Ghost assignment by Jerry Liao.
"""

import os
import sys
from simpleimage import SimpleImage


def get_pixel_dist(pixel, red, green, blue):
    """
    Returns a value that refers to the "color distance" between a pixel and a mean RGB value.

    Input:
        pixel (Pixel): the pixel with RGB values to be compared
        red (int): the average red value of the pixels to be compared
        green (int): the average green value of the pixels to be compared
        blue (int): the average blue value of the pixels to be compared

    Returns:
        dist (float): the "color distance" of a pixel to the average RGB value of the pixels to be compared.
    """
    dist = ((red-pixel.red)**2 + (green-pixel.green)**2 + (blue-pixel.blue)**2)**0.5
    return dist


def get_average(pixels):
    """
    Given a list of pixels, finds their average red, blue, and green values.

    Input:
        pixels (List[Pixel]): a list of pixels to be averaged

    Returns:
        rgb (List[int]): a list of average red, green, and blue values of the pixels
                        (returns in order: [red, green, blue])
    """
    # red = 0
    # green = 0
    # blue = 0
    # for pixel in pixels:
    #     red += pixel.red
    #     green += pixel.green
    #     blue += pixel.blue
    #     list = [red//len(pixels), green//len(pixels), blue//len(pixels)]
    # return list -->要特別注意不能取名list (因為已經被python命名有其他用途了 所以要取其他名字）
    # 以下是更好的寫法
    ave_red = sum(pixel.red for pixel in pixels)
    ave_green = sum(pixel.green for pixel in pixels)
    ave_blue = sum(pixel.blue for pixel in pixels)
    ave_lst = [ave_red // len(pixels), ave_green//len(pixels), ave_blue//len(pixels)]
    return ave_lst


def get_best_pixel(pixels):
    """
    Given a list of pixels, returns the pixel with the smallest "color distance", which has the closest color to the average.

    Input:
        pixels (List[Pixel]): a list of pixels to be compared
    Returns:
        best (Pixel): the pixel which has the closest color to the average
    """
    # dic = {}    # build a new dictionary
    # i = 0
    # for pixel in pixels:    # pixels == List[Pixel]
    #     dic[i] = get_pixel_dist(pixel, get_average(pixels)[0], get_average(pixels)[1], get_average(pixels)[2])  #
    #     # 使用get_pixel_dist傳遞“每一個pixel像素“, average red, average g, and average b
    #     i += 1
    # min_dis_pair = min(dic.items(), key=lambda t: t[1])     # 從這個dic字典的鍵值中,使用lambda參數作為key的參數值（value), lambda t:t[
    # # 1]代表於每個項目 t[0]，取出索引 t[1](第二個數） 的元素作為比較值, min是返回最小值
    # best_pixel_index = min_dis_pair[0]  # 取pixel的那個編碼(key),非value(RBG值）
    # return pixels[best_pixel_index]
    # 以下是更好的寫法
    ave_pixel = get_average(pixels)
    best_pixel = []
    for pixel in pixels:    # loop over each pixels and find the pixel closet to the average
        dist = get_pixel_dist(pixel, ave_pixel[0], ave_pixel[1], ave_pixel[2])
        best_pixel.append((dist, pixel))
    return min(best_pixel, key=lambda t: t[0][1])


def solve(images):
    """
    Given a list of image objects, compute and display a Ghost solution image
    based on these images. There will be at least 3 images and they will all
    be the same size.

    Input:
        images (List[SimpleImage]): list of images to be processed
    """
    width = images[0].width
    height = images[0].height
    result = SimpleImage.blank(width, height)
    
    # ----- YOUR CODE STARTS HERE ----- #
    # Write code to populate image and create the 'ghost' effect
    for x in range(width):
        for y in range(height):
            pixels = []     # 遊遍整個image的xy位址 每個點都放一個空pixel好在之後把想要的圖pixel填進去
            for i in range(len(images)):
                image_pixel = images[i].get_pixel(x, y)  # 每一張圖的每一個點都取xy的值 放入image_pixel中
                pixels.append(image_pixel)
            you_are_the_best_pixel = get_best_pixel(pixels)     # 在這個pixels list當中都取與RGB的平均值最近的那個pixel,
            # 取名叫you_are_the_best
            result_pixel = result.get_pixel(x, y)    # 在result image中取每個xy像素值
            result_pixel.red = you_are_the_best_pixel.red   # 把這張result image的ＲＧＢ都改成最接近平均值RGB的點
            result_pixel.green = you_are_the_best_pixel.green
            result_pixel.blue = you_are_the_best_pixel.blue
    # ----- YOUR CODE ENDS HERE ----- #

    print("Displaying image!")
    result.show()


def jpgs_in_dir(dir):
    """
    (provided, DO NOT MODIFY)
    Given the name of a directory, returns a list of the .jpg filenames
    within it.

    Input:
        dir (string): name of directory
    Returns:
        filenames(List[string]): names of jpg files in directory
    """
    filenames = []
    for filename in os.listdir(dir):
        if filename.endswith('.jpg'):
            filenames.append(os.path.join(dir, filename))
    return filenames


def load_images(dir):
    """
    (provided, DO NOT MODIFY)
    Given a directory name, reads all the .jpg files within it into memory and
    returns them in a list. Prints the filenames out as it goes.

    Input:
        dir (string): name of directory
    Returns:
        images (List[SimpleImages]): list of images in directory
    """
    images = []
    jpgs = jpgs_in_dir(dir)
    for filename in jpgs:
        print("Loading", filename)
        image = SimpleImage(filename)
        images.append(image)
    return images


def main():
    # (provided, DO NOT MODIFY)
    args = sys.argv[1:]
    # We just take 1 argument, the folder containing all the images.
    # The load_images() capability is provided above.
    images = load_images(args[0])
    solve(images)


if __name__ == '__main__':
    main()
