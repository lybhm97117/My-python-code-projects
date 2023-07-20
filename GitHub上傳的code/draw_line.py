"""
File: draw_line.py
Name: Teresa Tien
-------------------------
This program creates lines on an instance of GWindow class.
There is a circle indicating the user’s first click. A line
appears at the condition where the circle disappears as the
user clicks on the canvas for the second time.
"""

from campy.graphics.gobjects import GOval, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked

# 在def main/def function之外的變數 只代表在兩邊都可以使用但不代表是global全域變數（global代表一邊改了所有數值跟著變）
SIZE = 10  # radius of circle
COUNT = 1  # count how many click that the user produce, if odd, then draw circle; if even, then draw line
window = GWindow(width=800, height=400, title='Draw Lines')
circle = GOval(SIZE, SIZE)
x = 0
y = 0


def main():
    """
    This program creates lines on an instance of GWindow class.
    There is a circle indicating the user’s first click. A line appears
    at the condition where the circle disappears as the user clicks
    on the canvas for the second time.
    """
    onmouseclicked(circle_and_line)


def circle_and_line(mouse):
    """
    draw circle and line
    """
    global COUNT, circle, x, y  # 宣告這幾個變數是全域變數,在其他def main/def function都可以被使用
    if COUNT % 2 != 0:  # odd, then draw a circle
        window.add(circle, x=mouse.x-SIZE/2, y=mouse.y-SIZE/2)
        x = mouse.x
        y = mouse.y  # 記錄現在滑鼠在x&y的位置
    elif COUNT % 2 == 0:  # even, then draw a line and remove the original circle
        line = GLine(x, y, mouse.x, mouse.y)  # 從原先circle座標的ｘｙ開始畫線 畫到新的滑鼠的mouse.x &y位置停止
        window.add(line)
        window.remove(circle)
    COUNT += 1



if __name__ == "__main__":
    main()
