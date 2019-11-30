# import gc
from time import sleep
import _thread
import buttons
import defines
import rgb
import system

# colors
colors = [0x00FFFF00, 0xFF00FF00, 0xFFFF0000, 0xFF000000, 0x00FF0000, 0x0000FF00, 0xFFFFFF00]
color = 0
# buttons
UP, DOWN, LEFT, RIGHT = defines.BTN_UP, defines.BTN_DOWN, defines.BTN_LEFT, defines.BTN_RIGHT
A, B = defines.BTN_A, defines.BTN_B


def input_up(pressed):
    if pressed:
        global color
        color = (color + 1) % (len(colors))


def input_down(pressed):
    if pressed:
        global color
        color = (color - 1) % (len(colors))


def input_left(pressed):
    if pressed:
        pass


def input_right(pressed):
    if pressed:
        pass


def input_B(pressed):
    if pressed:
        rgb.clear()
        rgb.text("Bye!")
        sleep(0.5)
        system.reboot()


def input_A(pressed):
    pass


# init
buttons.register(UP, input_up)
buttons.register(DOWN, input_down)
buttons.register(LEFT, input_left)
buttons.register(RIGHT, input_right)
buttons.register(B, input_B)
buttons.register(A, input_A)

rgb.framerate(30)

eyes = [
    [  # dark iris, light pupil
        0, 1, 1, 1, 1, 1, 1, 0, 0,
        1, 0, 0, 0, 0, 0, 0, 1, 0,
        1, 0, 0, 0, 0, 0, 0, 1, 0,
        1, 0, 0, 1, 1, 0, 0, 1, 0,
        1, 0, 0, 1, 1, 0, 0, 1, 0,
        1, 0, 0, 0, 0, 0, 0, 1, 0,
        1, 0, 0, 0, 0, 0, 0, 1, 0,
        0, 1, 1, 1, 1, 1, 1, 0, 0,
    ],
    [  # 1 light iris, no pupil
        0, 1, 1, 1, 1, 1, 1, 0, 0,
        1, 1, 1, 1, 1, 1, 1, 1, 0,
        1, 1, 1, 1, 1, 1, 1, 1, 0,
        1, 1, 1, 1, 1, 1, 1, 1, 0,
        1, 1, 1, 1, 1, 1, 1, 1, 0,
        1, 1, 1, 1, 1, 1, 1, 1, 0,
        1, 1, 1, 1, 1, 1, 1, 1, 0,
        0, 1, 1, 1, 1, 1, 1, 0, 0,
    ], [  # 2 blink start 1
        0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 1, 1, 1, 1, 1, 1, 0, 0,
        1, 1, 1, 1, 1, 1, 1, 1, 0,
        1, 1, 1, 1, 1, 1, 1, 1, 0,
        1, 1, 1, 1, 1, 1, 1, 1, 0,
        1, 1, 1, 1, 1, 1, 1, 1, 0,
        0, 1, 1, 1, 1, 1, 1, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0,
    ], [  # 3 blink start 2
        0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 1, 1, 1, 1, 1, 1, 0, 0,
        1, 1, 1, 1, 1, 1, 1, 1, 0,
        1, 1, 1, 1, 1, 1, 1, 1, 0,
        0, 1, 1, 1, 1, 1, 1, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0,
    ], [  # 4 blink start 3
        0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 1, 1, 1, 1, 1, 1, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0,
    ], [  # 5 heart
        0, 1, 1, 0, 0, 0, 1, 1, 0,
        1, 1, 1, 1, 0, 1, 1, 1, 1,
        1, 1, 1, 1, 1, 1, 1, 1, 1,
        0, 1, 1, 1, 1, 1, 1, 1, 0,
        0, 0, 1, 1, 1, 1, 1, 0, 0,
        0, 0, 0, 1, 1, 1, 0, 0, 0,
        0, 0, 0, 0, 1, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0,
    ]
]
pupils = [
    [  # 0 no pupil
        1, 1, 1, 1, 1, 1, 1, 1, 1,
        1, 1, 1, 1, 1, 1, 1, 1, 1,
        1, 1, 1, 1, 1, 1, 1, 1, 1,
        1, 1, 1, 1, 1, 1, 1, 1, 1,
        1, 1, 1, 1, 1, 1, 1, 1, 1,
        1, 1, 1, 1, 1, 1, 1, 1, 1,
        1, 1, 1, 1, 1, 1, 1, 1, 1,
        1, 1, 1, 1, 1, 1, 1, 1, 1,
    ],
    [  # 1: 4x4 pupil
        1, 1, 1, 1, 1, 1, 1, 1, 1,
        1, 0, 0, 1, 1, 1, 1, 1, 1,
        1, 0, 0, 1, 1, 1, 1, 1, 1,
        1, 1, 1, 1, 1, 1, 1, 1, 1,
        1, 1, 1, 1, 1, 1, 1, 1, 1,
        1, 1, 1, 1, 1, 1, 1, 1, 1,
        1, 1, 1, 1, 1, 1, 1, 1, 1,
        1, 1, 1, 1, 1, 1, 1, 1, 1,
    ],

]
count = 0
location = [0, 1, 2, 3, 4, 9, 10, 11, 12, 13, 18, 19, 20, 21, 22, 27, 28, 29, 30, 31, 36, 37, 38, 39, 40]
pos = 11

# patterns: eye, pupil, location
sequences = [
    [  # sequence for blinking
        [1, 1, 12],
        [2, 1, 12],
        [3, 1, 12],
        [4, 0, 0],
        [3, 1, 12],
        [2, 1, 12],
        [1, 1, 12],
    ], [
        # sequence for looking
        [1, 1, 12],
        [1, 1, 11],
        [1, 1, 10],
        [1, 1, 11],
        [1, 1, 12],
        [1, 1, 13],
        [1, 1, 14],
        [1, 1, 13],
    ], [
        # sequence for steady
        [1, 1, 12],
    ],[
        # sequence for heart
        [5, 0, 12],
    ]
]
# sequences:  right, left, time, #steps
actions = [
    [1, 1, 0.2, len(sequences[1])],
    [0, 0, 0.1, len(sequences[0])],
    [1, 1, 0.2, len(sequences[1])],
    [2, 0, 0.1, len(sequences[0])],
    [3, 3, 1, 1],
]

action = 0
while True:
    step = 0
    while True:
        print('{}:{}'.format(action, step))

        sequence = sequences[actions[action][0]]
        pattern = sequence[step % len(sequence)]
        pupil = [1] * location[pattern[2]] + pupils[pattern[1]]
        map_r = [colors[color] * e * p for e, p in zip(eyes[pattern[0]], pupil)]

        sequence = sequences[actions[action][1]]
        pattern = sequence[step % len(sequence)]
        pupil = [1] * location[pattern[2]] + pupils[pattern[1]]
        map_l = [colors[color] * e * p for e, p in zip(eyes[pattern[0]], pupil)]

        rgb.clear()
        rgb.image(map_r, (0, 0), (9, 8))
        rgb.image(map_l, (23, 0), (9, 8))

        sleep(actions[action][2])
        step = (step + 1)  # next step in sequence
        if step > actions[action][3]:
            break  # next sequence
    action = (action + 1) % len(actions)