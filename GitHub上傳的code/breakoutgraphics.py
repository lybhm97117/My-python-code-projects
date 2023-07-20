"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao.

YOUR DESCRIPTION HERE
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5  # Space between bricks (in pixels). This space is used for horizontal and vertical spacing
BRICK_WIDTH = 40  # Width of a brick (in pixels)
BRICK_HEIGHT = 15  # Height of a brick (in pixels)
BRICK_ROWS = 10  # Number of rows of bricks
BRICK_COLS = 10  # Number of columns of bricks
BRICK_OFFSET = 50  # Vertical offset of the topmost brick from the window top (in pixels)
BALL_RADIUS = 10  # Radius of the ball (in pixels)
PADDLE_WIDTH = 75  # Width of the paddle (in pixels)
PADDLE_HEIGHT = 15  # Height of the paddle (in pixels)
PADDLE_OFFSET = 50  # Vertical offset of the paddle from the window bottom (in pixels)
INITIAL_Y_SPEED = 7  # Initial vertical speed for the ball
MAX_X_SPEED = 5  # Maximum initial horizontal speed for the ball


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, title='Breakout'):
        self.brick_offset = brick_offset
        self.paddle_offset = paddle_offset
        self.paddle_width = paddle_width
        self.paddle_height = paddle_height
        self.brick_rows = brick_rows
        self.brick_cols = brick_cols
        self.brick_spacing = brick_spacing
        self.ball_radius = ball_radius
        self.brick_width = BRICK_WIDTH
        self.brick_height = BRICK_HEIGHT



        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)
        self.window_width = window_width
        self.window_height = window_height


        # Create a paddle
        self.paddle = GRect(paddle_width, paddle_height)
        self.paddle.filled = True
        self.paddle.fill_color = 'black'
        self.window.add(self.paddle, x=(window_width - paddle_width) / 2,
                        y=window_height - paddle_offset - paddle_height)

        # Center a filled ball in the graphical window
        self.ball = GOval(ball_radius * 2, ball_radius * 2)
        self.ball.filled = True
        self.ball.fill_color = 'black'
        self.window.add(self.ball, x=(window_width - (ball_radius * 2)) / 2, y=(window_height - (ball_radius * 2)) / 2)

        # Default initial velocity for the ball
        self.__dx = 0
        self.__dy = 0
        self.ball_fall_direction()

        # Initialize our mouse listeners
        self.switch = False
        onmouseclicked(self.switch_button)
        onmousemoved(self.move_paddle)

        # Draw bricks
        for i in range(brick_rows):
            for j in range(brick_cols):
                self.brick = GRect(brick_width, brick_height)
                self.brick.filled = True
                if i % 10 <= 1:
                    self.brick.fill_color = 'red'
                elif i % 10 <= 3:
                    self.brick.fill_color = 'orange'
                elif i % 10 <= 5:
                    self.brick.fill_color = 'yellow'
                elif i % 10 <= 7:
                    self.brick.fill_color = 'green'
                elif i % 10 <= 9:
                    self.brick.fill_color = 'blue'
                self.window.add(self.brick, x=(brick_width + brick_spacing) * j,
                                y=((brick_height + brick_spacing) * i + brick_offset))

    def move_paddle(self, mouse):
        """
        mouse可移動的範圍必須限縮在視窗兩邊各自- paddle/2的 範圍， 因為paddle是以左上角來數座標, 且在這限定範圍內滑鼠需至中, 所以最多只能算到paddle/2的左右範圍,超過範圍則不動作（所以沒有else)
        """
        if self.paddle.width / 2 <= mouse.x <= self.window.width - self.paddle.width / 2: # 在這個區間滑鼠才需要致中
            self.paddle.x = mouse.x - self.paddle.width / 2

    def ball_fall_direction(self):
        """
        點擊時決定球落下的方向
        """
        self.__dy = INITIAL_Y_SPEED
        self.__dx = random.randint(1, MAX_X_SPEED)
        if random.random() > 0.5:
            self.__dx = -self.__dx

    def switch_button(self,mouse):
        """
        記錄開關開啟/關閉, 點擊滑鼠後開關開,之後後球就會亂撞,直到球掉下去後,開關自動關閉，再次點擊開關才會再打開
        """
        self.switch = True

    def get_dx(self):
        return self.__dx

    def get_dy(self):
        return self.__dy

    def set_dx(self):
        self.__dx = -self.__dx

    def set_dy(self):
        self.__dy = -self.__dy

    def detect(self):
        """
        檢測.get_object_at(x座標, y座標) 探測該點是否有物件,有物件的話(代表有碰撞）,回傳not None,並判斷物體是paddle/brick.並且就不跑另一個頂點做檢測
        沒有碰到物件的話,繼續下一個頂點做檢測是否有物件（代表有碰撞）,4個點都是None代表無碰撞產生
        :return:
        """
        for i in range(0, 3, 2): # (i= 0,2)
            for j in range(0, 3, 2): # (j= 0,2)
                obj= self.window.get_object_at(self.ball.x+j*self.ball_radius, self.ball.y+i*self.ball_radius)
                if obj is not None: # 不是沒有空的值（代表有東西=有碰撞！)
                    return obj

    def reset_ball(self):
        """
        把球放回視窗正中心的起始點
        :return:
        """
        x = (self.window_width - (self.ball_radius * 2)) / 2
        y = (self.window_height - (self.ball_radius * 2)) / 2
        self.ball.x = x
        self.ball.y = y

