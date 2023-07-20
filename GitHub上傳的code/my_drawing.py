"""
File: 
Name:
----------------------
TODO:
"""

from campy.graphics.gobjects import GOval, GRect, GLine, GLabel, GPolygon, GArc
from campy.graphics.gwindow import GWindow


def main():
    """
    Title: Penguin Cub
    penguin cubs are cute and friendly. Hope I can see them in person in Antarctica one day.
    """
    window = GWindow(width=800, height=500, title='Penguin Cub')

    # draw up_head():
    up_head = GOval(250,200, x=220, y=45)
    window.add(up_head)
    up_head.filled = True
    up_head.fill_color = 'dark gray'
    up_head.color = 'dark gray'

    # draw down_body():
    down_body = GOval(300,250, x=195, y=140)
    window.add(down_body)
    down_body.filled = True
    down_body.fill_color = 'dark gray'
    down_body.color = 'dark gray'

    # draw_left_hand():
    l_hand = GPolygon()
    l_hand.add_vertex((135, 205))
    l_hand.add_vertex((240, 235))
    l_hand.add_vertex((220, 280))
    l_hand.add_vertex((105, 250))
    window.add(l_hand)
    l_hand.filled = True
    l_hand.fill_color = 'dark gray'
    l_hand.color = 'dark gray'

    # draw_right_hand():
    r_hand = GPolygon()
    r_hand.add_vertex((470, 230))
    r_hand.add_vertex((550, 210))
    r_hand.add_vertex((580, 260))
    r_hand.add_vertex((480, 280))
    window.add(r_hand)
    r_hand.filled = True
    r_hand.fill_color = 'dark gray'
    r_hand.color = 'dark gray'

    # draw_left_face():
    l_face = GOval(120, 140, x=245, y=80)
    l_face.filled = True
    l_face.fill_color = 'white'
    l_face.color = 'white'
    window.add(l_face)

    # draw_right_face():
    r_face = GOval(120, 140, x=325, y=80)
    window.add(r_face)
    r_face.filled = True
    r_face.fill_color = 'white'
    r_face.color = 'white'

    # draw_belly():
    belly = GOval(240, 220, x=225, y=140)
    window.add(belly)
    belly.filled = True
    belly.fill_color = 'white'
    belly.color = 'white'

    # draw left_foot():
    l_foot = GOval(80, 40, x=205, y=355)
    window.add(l_foot)
    l_foot.filled = True
    l_foot.fill_color = 'orange'
    l_foot.color = 'orange'

    # draw right_foot():
    r_foot = GOval(80, 40, x=400, y=355)
    window.add(r_foot)
    r_foot.filled = True
    r_foot.fill_color = 'orange'
    r_foot.color = 'orange'

    # draw left_blush():
    l_blush = GOval(40, 20, x=235, y=155)
    window.add(l_blush)
    l_blush.filled = True
    l_blush.fill_color = 'tomato'
    l_blush.color = 'tomato'

    # draw right_blush():
    r_blush = GOval(40, 20, x=415, y=155)
    window.add(r_blush)
    r_blush.filled = True
    r_blush.fill_color = 'tomato'
    r_blush.color = 'tomato'

    # draw left_eye():
    l_eye = GOval(40, 40, x=285, y=115)
    window.add(l_eye)
    l_eye.filled = True
    l_eye.fill_color = 'black'

    # draw left_eyeball():
    l_eyeball = GOval(10, 10, x=305, y=135)
    window.add(l_eyeball)
    l_eyeball.filled = True
    l_eyeball.fill_color = 'white'
    l_eyeball.color = 'white'

    # draw right_eye():
    r_eye = GOval(40, 40, x=360, y=115)
    window.add(r_eye)
    r_eye.filled = True
    r_eye.fill_color = 'black'

    # draw right_eyeball():
    r_eyeball = GOval(10, 10, x=380, y=135)
    window.add(r_eyeball)
    r_eyeball.filled = True
    r_eyeball.fill_color = 'white'
    r_eyeball.color = 'white'

    # dray beak():
    beak = GPolygon()
    beak.add_vertex((325, 180))
    beak.add_vertex((365, 180))
    beak.add_vertex((345, 200))
    window.add(beak)
    beak.filled = True
    beak.fill_color = 'orange'
    beak.color = 'orange'

if __name__ == '__main__':
    main()
