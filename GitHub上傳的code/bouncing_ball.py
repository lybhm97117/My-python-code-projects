"""
File: bouncing_ball.py
Name: Teresa Tien
-------------------------
This program simulates a bouncing ball at (START_X, START_Y)
that has VX as x velocity, vy as y velocity, and 1 as GRAVITY.
Each bounce reduces y velocity to REDUCE of itself.
The bouncing process starts when the mouse is clicked for the
first time, and it ends when the ball horizontally bounces out
of the window. The ball will move back to (START_X, START_Y)
at the end of each process. The bouncing process can only be
executed 3 times.
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked

VX = 3          # 球的水平速度
DELAY = 10      # 動畫停格多少毫秒(ms)
GRAVITY = 1     # 重力加速度;每一圈 while loop 垂直速度要加上的數值
SIZE = 20       # 球的直徑
REDUCE = 0.9    # 每一次反彈時，在垂直速度所剩之比例
START_X = 30    # 球的起始 x 座標
START_Y = 40    # 球的起始 y 座標

VY = 0          # 初始值是停著 Ｙ速度是0
COUNT = 0       # Count times that the ball rolls out of the right side of the window
window = GWindow(800, 500, title='bouncing_ball.py')
ball = GOval(SIZE, SIZE)
switch = False  # 設一個開關,他default是閉著的(False), 當今天有on_mouseclick動作時後 會把開關變成True 開始做bouncing動作, 如果超出右邊視窗 switch又會轉變為
# false 然後不做下一次bouncing 直到再一次on_mouseclick在把開關打開


def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """
    ball.filled = True
    window.add(ball, START_X, START_Y)
    global COUNT, switch    # 全域變數代表這邊定義了後 牽一髮動全身 在其他def function也會跟著被變動數值
    while True:
        onmouseclicked(start)   # start是個函數代表開關要打開
        if switch is True:
            vx = VX
            vy = VY
            while True:
                ball.move(vx, vy)  # let the ball moves in VX velocity in the X direction, and in VY velocity in the
                # Y direction
                vy += GRAVITY  # VY velocity grows by gravity
                if ball.y >= window.height - SIZE:  # means the ball touches the ground
                    ball.y = window.height - SIZE   # means if the ball is under the ground and start to move
                    # in the opposite direction, we might have chances not to see the ball, so we need to make sure
                    # at least the ball touches the ground
                    vy = -vy * REDUCE  # then the ball needs to move in the opposite direction

                if ball.x > window.width:
                    ball.x = START_X
                    ball.y = START_Y
                    COUNT += 1
                    switch = False  # finished bouncing, then turn off the switch until the next time when
                    # user click the mouse, then the swtich will turn on again
                    break   # 直接跳出整坨if switch is True迴圈 進到if count ==3
                pause(DELAY)

        if COUNT == 3:
            break
        pause(DELAY)


def start(mouse):
    """
    turn on switch
    """
    global switch
    switch = True






if __name__ == "__main__":
    main()
