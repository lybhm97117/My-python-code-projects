"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

YOUR DESCRIPTION HERE
"""

from campy.graphics.gobjects import GLabel
from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 10  # 100 frames per second
NUM_LIVES = 3  # Number of attempts


def main():
    graphics = BreakoutGraphics()
    lives = NUM_LIVES
    live_label = GLabel('Lives:' + str(lives))  # 顯示還有幾次生命的文字
    live_label.font = '-30'
    graphics.window.add(live_label, x=0, y=live_label.height)  # 文字是從左下角開始count,所以文字高度要加回去
    # Add the animation loop here!
    while True:
        if graphics.switch:  # switch = True,代表遊戲已經clicked!已經開始
            if lives > 0: # 還有命的話
                detection = graphics.detect()
                if graphics.ball.y > graphics.window.height: # 如果球碰到最底部
                    lives -= 1
                    graphics.switch = False # 開關關起來，等待下一次點擊開始
                    graphics.reset_ball() # 球移動到視窗正中間位置
                if detection is not None:  # 球有撞到物體
                    if detection == graphics.paddle: # 如果球碰到板子,則只改變球的垂直y方向
                        graphics.ball.y = graphics.paddle.y - graphics.ball.height  # 球尾巴不要碰到paddle會反彈
                        graphics.set_dy()

                    elif detection != graphics.paddle: # 如果碰到其他物件ＥＸ：上方磚塊,則把磚塊去除,同時改變球的y方向
                        graphics.window.remove(detection)
                        graphics.set_dy()
                graphics.ball.move(graphics.get_dx(), graphics.get_dy()) # 讓球按照dx, dy速度移動
                if graphics.ball.x <= 0 or graphics.ball.x + graphics.ball.width >= graphics.window.width:  # 如果球碰到視窗x邊界
                    graphics.set_dx()  # 用setter來改變private variables的x方向
                if graphics.ball.y <= 0:  # 如果球碰到視窗y上邊界
                    graphics.set_dy() # 用setter來改變private variables的y方向
            live_label.text = 'Lives: ' + str(lives)
        pause(FRAME_RATE)


if __name__ == '__main__':
    main()
