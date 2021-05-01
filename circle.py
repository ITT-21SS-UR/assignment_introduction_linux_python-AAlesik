import turtle
import math
import sys

MAX_ARGS = 1
MAX_DEG = 360
PRECISION = 10
# used for calculating drawprecision supsteps: PRECISION/MAX_DEG
SP_PRECISION = 20
# Spiralprecision -> the greater the less precise ;)

degree_pos = 0
radius = 0


def main():
    init_args_handler()
    start_pos()
    set_style()
    draw_cir()
    draw_spir()
    print("Success!!")
    turtle.done()


def draw_cir():
    # draws Circle with the calculated relative radius...
    global degree_pos
    turtle.begin_fill()
    while True:
        degree_pos += PRECISION
        if degree_pos > MAX_DEG:
            turtle.setpos(math.cos(math.radians(MAX_DEG)) * radius, math.sin(math.radians(MAX_DEG)) * radius)
            turtle.end_fill()
            break
        turtle.setpos(math.cos(math.radians(degree_pos)) * radius, math.sin(math.radians(degree_pos)) * radius)
        # calculates next position with radius and sin/cos
    pass


def draw_spir():
    # draws spiral relative to the circle...
    global degree_pos
    turtle.pensize(int(radius / 80))
    sp_rad = radius
    while True:
        sp_rad -= 0.01 * SP_PRECISION * radius * PRECISION / MAX_DEG
        # calculate temporal radius relative to the size...
        if sp_rad < 0:
            break
        turtle.setpos(math.cos(math.radians(degree_pos)) * sp_rad, math.sin(math.radians(degree_pos)) * sp_rad)
        degree_pos += PRECISION
    pass


def set_style():  # getting look
    turtle.pensize(int(radius / 40))
    turtle.color('grey', 'darkgrey')
    return


def start_pos():
    # give turtle i's start postion
    turtle.penup()
    turtle.fd(radius)
    turtle.pendown()
    return


def init_args_handler():
    # how to handle the possible arguments (Dialogtree u.a)
    global radius
    if (len(sys.argv) - 1) != MAX_ARGS:
        exception_handler("noArgs")
    try:
        radius = int(sys.argv[1])
    except ValueError:
        exception_handler("UnInput")
    return


def exception_handler(case):
    # exiting earlier due to .. reasons
    print(dialog(case))
    sys.exit()
    pass


def dialog(case):
    # inspired from this website: https://data-flair.training/blogs/python-switch-case/
    switch = {
        # a simple dialog manager
        "noArgs": "Please provide a number as an argument!",
        "UnInput": "There is something wrong with the numbers..."
    }
    return switch.get(case)


if __name__ == "__main__":
    main()
