"""
File: babygraphics.py
Name: Teresa Tien
--------------------------------
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.
"""

import tkinter
import babynames
import babygraphicsgui as gui

FILENAMES = [
    'data/full/baby-1900.txt', 'data/full/baby-1910.txt',
    'data/full/baby-1920.txt', 'data/full/baby-1930.txt',
    'data/full/baby-1940.txt', 'data/full/baby-1950.txt',
    'data/full/baby-1960.txt', 'data/full/baby-1970.txt',
    'data/full/baby-1980.txt', 'data/full/baby-1990.txt',
    'data/full/baby-2000.txt', 'data/full/baby-2010.txt'
]
CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 600
YEARS = [1900, 1910, 1920, 1930, 1940, 1950,
         1960, 1970, 1980, 1990, 2000, 2010]
GRAPH_MARGIN_SIZE = 20
COLORS = ['red', 'purple', 'green', 'blue']
TEXT_DX = 2
LINE_WIDTH = 2
MAX_RANK = 1000


def get_x_coordinate(width, year_index):
    """
    Given the width of the canvas and the index of the current year
    in the YEARS list, returns the x coordinate of the vertical
    line associated with that year.

    Input:
        width (int): The width of the canvas
        year_index (int): The index where the current year is in the YEARS list
    Returns:
        x_coordinate (int): The x coordinate of the vertical line associated
                            with the current year.
    """
    x_coordinate = GRAPH_MARGIN_SIZE + (width - GRAPH_MARGIN_SIZE*2)//len(YEARS) * year_index
    return x_coordinate


def draw_fixed_lines(canvas):
    """
    Draws the fixed background lines on the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
    """
    canvas.delete('all')            # delete all existing lines from the canvas

    # ----- Write your code below this line ----- #
    # 畫第一條線,GLine規則（起點x, 起點y, 終點ｘ,終點y)
    canvas.create_line(GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE, CANVAS_WIDTH-GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE)
    # 畫第二條GLine
    canvas.create_line(GRAPH_MARGIN_SIZE, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, CANVAS_WIDTH-GRAPH_MARGIN_SIZE, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE)
    for i in range(len(YEARS)):
        # 每一點x座標位置畫長直線,GLine規則（起點x, 起點y, 終點ｘ,終點y)
        canvas.create_line(get_x_coordinate(CANVAS_WIDTH, i), 0, get_x_coordinate(CANVAS_WIDTH, i), CANVAS_HEIGHT )
        # 在交叉點位置寫上年份, GText規則(x座標, y座標, text=要輸入的文字）
        canvas.create_text(get_x_coordinate(CANVAS_WIDTH, i)+TEXT_DX, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, text=YEARS[i], anchor=tkinter.NW)


def draw_names(canvas, name_data, lookup_names):
    """
    Given a dict of baby name data and a list of name, plots
    the historical trend of those names onto the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
        name_data (dict): Dictionary holding baby name data
        lookup_names (List[str]): A list of names whose data you want to plot

    Returns:
        This function does not return any value.
    """
    draw_fixed_lines(canvas)        # draw the fixed background grid

    # ----- Write your code below this line ----- #
    color_order = 0     # 從0開始數, 每四個一個循環來重複顏色
    for name in lookup_names:
        color = COLORS[color_order]     # COLORS LIST中放入0,1,2,3,的編碼
        year_index = 0
        for i in range(len(YEARS) - 1):     # 兩點連成一線,最後一點沒有人跟他接, 所以只用做到YEARS -1
            x1 = get_x_coordinate(CANVAS_WIDTH, i)
            x2 = get_x_coordinate(CANVAS_WIDTH, i+1)
            y_dist = (CANVAS_HEIGHT - GRAPH_MARGIN_SIZE*2)/1000    # 前1000名 在height的ｙ軸中分成1000格
            if str(YEARS[i]) in name_data[name]:    # 年在名字內 （代表排名在1000內）
                y1 = int(name_data[name][str(YEARS[i])]) * y_dist   # 名字底下的year的底下代表是“排名”（每一年 排名）的y位置
                r1 = int(name_data[name][str(YEARS[i])])    # 人名＆year下面的rank
            else:   # 排名超過1000
                y1 = CANVAS_HEIGHT - GRAPH_MARGIN_SIZE*2
                r1 = ' *'
            if str(YEARS[i+1]) in name_data[name]:  # 第二個點
                y2 = int(name_data[name][str(YEARS[i+1])]) * y_dist  # 名字year後的排名（每一年 排名）的y位置
                r2 = int(name_data[name][str(YEARS[i+1])])  # 人名＆year下面的rank
            else:  # 超過1000
                y2 = CANVAS_HEIGHT - GRAPH_MARGIN_SIZE * 2
                r2 = ' *'
            canvas.create_text(x1+TEXT_DX, int(y1)-TEXT_DX*6 + GRAPH_MARGIN_SIZE, text=name+' ' + str(r1), anchor=tkinter.NW, fill=color )
            canvas.create_text(x2 + TEXT_DX, int(y2) - TEXT_DX * 6 + GRAPH_MARGIN_SIZE, text=name + ' ' + str(r2),
                               anchor=tkinter.NW, fill=color)
            canvas.create_line(x1, y1+GRAPH_MARGIN_SIZE, x2, y2+GRAPH_MARGIN_SIZE, width=LINE_WIDTH, fill=color)
        if color_order < len(COLORS)-1:     # 0,1,2 （因為顏色是4個一個循環,所以不能超過3, 不然3+1 =4 , 4/4應該要整除變0
            color_order += 1
        else: # 3
            color_order = 0     # 直接變整除是0


# main() code is provided, feel free to read through it but DO NOT MODIFY
def main():
    # Load data
    name_data = babynames.read_files(FILENAMES)

    # Create the window and the canvas
    top = tkinter.Tk()
    top.wm_title('Baby Names')
    canvas = gui.make_gui(top, CANVAS_WIDTH, CANVAS_HEIGHT, name_data, draw_names, babynames.search_names)

    # Call draw_fixed_lines() once at startup so we have the lines
    # even before the user types anything.
    draw_fixed_lines(canvas)

    # This line starts the graphical loop that is responsible for
    # processing user interactions and plotting data
    top.mainloop()


if __name__ == '__main__':
    main()
