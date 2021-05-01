import os
import sys
import statistics

MAX_ARGS = 1

calcstring = ""


def main():
    init_args_handler()
    calc(string_list(calcstring))


def string_list(c_string):  # string to float number list...
    s_list = c_string.replace(",", ".").split(" ")
    s_list = list(map(float, s_list))
    return s_list


def calc(s_list):          # math & final print
    if len(s_list) == 1:
        mean = s_list[0]
        median = s_list[0]
        stdev = 0
    else:
        mean = statistics.mean(s_list)
        median = statistics.median(s_list)
        stdev = statistics.stdev(s_list)
    print(dialog("mean"), mean)
    print(dialog("median"), median)
    print(dialog("stdev"), stdev, "\n")


def init_args_handler():    # how to handle the possible arguments (Dialogtree u.a)
    global calcstring
    argslen = len(sys.argv) - 1
    if argslen > MAX_ARGS:
        exception_handler("tooMuchArgs")
    if argslen == MAX_ARGS:
        if not (os.path.isfile(sys.argv[1])):
            exception_handler("noFile")
    if argslen < MAX_ARGS:
        calcstring = input(dialog("plWri"))
        if calcstring == "":
            exception_handler("noInput")
        print()
    else:
        with open(sys.argv[1]) as file:
            calcstring = file.readline()    # > Calculates only first line (savety reasons)
            print("Input: ", calcstring)
    return


def exception_handler(case):    # exiting earlier due to .. reasons
    print(dialog(case))
    sys.exit()
    pass


def dialog(case):               # inspired from this website: https://data-flair.training/blogs/python-switch-case/
    switch = {                  # a simple dialog manager
        "tooMuchArgs": "Please provide a filepath as an argument!",
        "noFile": "Couldn't open file!",
        "plWri": "Please wright manually an amount of numbers:\n",
        "noInput": "No input readable... Shutting down...",
        "mean": "mean:\t\t\t",
        "median": "median:\t\t\t",
        "stdev": "standard deviation:\t",
        "UnInput": "There is something with the numbers..."
    }
    return switch.get(case)


if __name__ == "__main__":
    main()
