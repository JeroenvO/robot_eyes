# import gc
from time import sleep
import _thread
import buttons
import defines
import rgb
import system
from .hcsr04 import HCSR04

# colors
colors = [0x00FFFF00, 0xFF00FF00, 0xFFFF0000, 0xFF000000, 0x00FF0000, 0x0000FF00, 0xFFFFFF00]
color = 3
# buttons
UP, DOWN, LEFT, RIGHT = defines.BTN_UP, defines.BTN_DOWN, defines.BTN_LEFT, defines.BTN_RIGHT
A, B = defines.BTN_A, defines.BTN_B
action_i = 0
pause = False


def input_up(pressed):
    if pressed:
        global color
        color = (color + 1) % len(colors)


def input_down(pressed):
    if pressed:
        global color
        color = (color - 1) % len(colors)


def input_left(pressed):
    global action_i, actions
    if pressed:
        action_i = (action_i + 1) % len(actions)
        pass


def input_right(pressed):
    global action_i, actions
    if pressed:
        action_i = (action_i - 1) % len(actions)
        pass


def input_B(pressed):
    if pressed:
        rgb.clear()
        rgb.text("Bye!")
        sleep(0.5)
        system.reboot()


def input_A(pressed):
    global pause
    if pressed:
        pause = not pause


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
    ], [  # 6 small heart
        0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 1, 0, 0, 0, 1, 0, 0,
        0, 1, 1, 1, 0, 1, 1, 1, 0,
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
    [  # 1: 2x2 pupil
        1, 1, 1, 1, 1, 1, 1, 1, 1,
        1, 0, 0, 1, 1, 1, 1, 1, 1,
        1, 0, 0, 1, 1, 1, 1, 1, 1,
        1, 1, 1, 1, 1, 1, 1, 1, 1,
        1, 1, 1, 1, 1, 1, 1, 1, 1,
        1, 1, 1, 1, 1, 1, 1, 1, 1,
        1, 1, 1, 1, 1, 1, 1, 1, 1,
        1, 1, 1, 1, 1, 1, 1, 1, 1,
    ], [  # 2: 3x3 pupil
        1, 1, 1, 1, 1, 1, 1, 1, 1,
        1, 0, 0, 0, 1, 1, 1, 1, 1,
        1, 0, 0, 0, 1, 1, 1, 1, 1,
        1, 0, 0, 0, 1, 1, 1, 1, 1,
        1, 1, 1, 1, 1, 1, 1, 1, 1,
        1, 1, 1, 1, 1, 1, 1, 1, 1,
        1, 1, 1, 1, 1, 1, 1, 1, 1,
        1, 1, 1, 1, 1, 1, 1, 1, 1,
    ], [  # 3: 4x4 pupil, corners
        1, 1, 1, 1, 1, 1, 1, 1, 1,
        1, 1, 0, 0, 1, 1, 1, 1, 1,
        1, 0, 0, 0, 0, 1, 1, 1, 1,
        1, 0, 0, 0, 0, 1, 1, 1, 1,
        1, 1, 0, 0, 1, 1, 1, 1, 1,
        1, 1, 1, 1, 1, 1, 1, 1, 1,
        1, 1, 1, 1, 1, 1, 1, 1, 1,
        1, 1, 1, 1, 1, 1, 1, 1, 1,
    ],

]


# For small pupil locations:
# 0  1  2  3  4
# 5  6  7  8  9
# 10 11 12 13 14
# 15 16 17 18 19
# 20 21 22 23 24

#           0  1  2  3  4  5  6  7   8   9   10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25
location = [0, 1, 2, 3, 4, 9, 10, 11, 12, 13, 18, 19, 20, 21, 22, 27, 28, 29, 30, 31, 36, 37, 38, 39, 40]

# patterns: eye, pupil, location
sequences = [
    [  # 0 sequence for opening
        [4, 0, 0],
        [3, 1, 12],
        [2, 1, 12],
        [1, 1, 12],
    ], [
        # 1 sequence for looking
        [1, 1, 12],
        [1, 1, 11],
        [1, 1, 10],
        [1, 1, 11],
        [1, 1, 12],
        [1, 1, 13],
        [1, 1, 14],
        [1, 1, 13],
    ], [
        # 2 sequence for steady
        [1, 1, 12],
    ], [
        # 3 sequence for heart
        [6, 0, 12],
        [5, 0, 12],
        [6, 0, 12],
    ], [
        # 4 sequence for very open
        [1, 3, 6],
    ], [
        # 5 sequence for rolling continuously
        [1, 1, 5],
        [1, 1, 1],
        [1, 1, 2],
        [1, 1, 3],
        [1, 1, 9],
        [1, 1, 14],
        [1, 1, 19],
        [1, 1, 23],
        [1, 1, 22],
        [1, 1, 21],
        [1, 1, 15],
        [1, 1, 10],
    ],[ # 6 closing
        [1, 1, 12],
        [2, 1, 12],
        [3, 1, 12],
        [4, 0, 0],
    ], [ #7 closed
        [4, 0, 0],
    ]
]
# actions:  right, left, time, #steps
actions = [
    [2, 2, 0.5, 1],  # normal  (needed as after opening the first one is skipped)
    [1, 1, 0.2, len(sequences[1])],  # looking
    [6, 6, 0.1, len(sequences[6])],  # closing two eye
    [7, 7, 0.1, len(sequences[7])],  # blinking two eye
    [0, 0, 0.1, len(sequences[0])],  # opening two eye
    [1, 1, 0.2, len(sequences[1])],  # looking
    [4, 4, 0.8, len(sequences[4])],  # wide open eyes
    [2, 2, 0.5, 1],  # normal
    [2, 6, 0.1, len(sequences[0])],  # blink one eye
    [2, 7, 0.1, len(sequences[0])],  # blink one eye
    [2, 0, 0.1, len(sequences[0])],  # blink one eye
    [3, 3, 0.5, 2 * len(sequences[3])],  # heart
    [2, 2, 0.5, 1],  # normal
    [5, 5, 0.1, 3*len(sequences[5])],  # rolliing
    [2, 2, 0.5, 1],  # normal
]

sensor = HCSR04(trigger_pin=4, echo_pin=5)
closed = False
while True:
    step_i = 0
    distance = sensor.distance_mm()
    # print('d: {}, {}'.format(distance, closed))
    if 0 < distance < 100:
        action_i = 0
        if closed:
            action = [7, 7, 0.1, 1]  # closed
        else:
            action = [6, 6, 0.1, len(sequences[6])]  # closing
        closed = True
    else:
        if closed:
            action_i = 0
            closed = False
            action = [0, 0, 0.1, len(sequences[0])]  # opening
        else:
            action = actions[action_i]

    while True:
        distance = sensor.distance_mm()
        if 0 < distance < 100 and closed == False:  # abort action
            step_i = 0
            action_i = 0
            break

        sequence = sequences[action[0]]
        pattern = sequence[step_i % len(sequence)]
        pupil = [1] * location[pattern[2]] + pupils[pattern[1]]
        map_r = [colors[color] * e * p for e, p in zip(eyes[pattern[0]], pupil)]

        sequence = sequences[action[1]]
        pattern = sequence[step_i % len(sequence)]
        pupil = [1] * location[pattern[2]] + pupils[pattern[1]]
        map_l = [colors[color] * e * p for e, p in zip(eyes[pattern[0]], pupil)]

        rgb.clear()
        rgb.image(map_r, (0, 0), (9, 8))
        rgb.image(map_l, (23, 0), (9, 8))

        if not pause:
            sleep(action[2])
            step_i = (step_i + 1)  # next step in sequence
            if step_i >= action[3]:
                break  # next sequence
        else:
            sleep(0.5)  # busy waiting.
    action_i = (action_i + 1) % len(actions)
