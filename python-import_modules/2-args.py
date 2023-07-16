#!/usr/bin/python3
if __name__ == "__main__":

    import sys

    args = sys.argv[1:]
    hueso = len(args)

    if hueso == 0:
        print("{} arguments.".format(hueso))
    elif hueso == 1:
        print("{} argument:".format(hueso))
    else:
        print("{} arguments:".format(hueso))
        for i, arg in enumerate(args, 1):
            print("{}: {}".format(i, arg))
