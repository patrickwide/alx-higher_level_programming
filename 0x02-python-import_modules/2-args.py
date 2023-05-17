#!/usr/bin/python3
import sys

if __name__ == "__main__":
    num_args = len(sys.argv) - 1

    if num_args == 0:
        argument_str = "0 arguments."
    elif num_args == 1:
        argument_str = "1 argument:"
    else:
        argument_str = "{:d} arguments:".format(num_args)

    print(argument_str)

    for i, argument in enumerate(sys.argv[1:], start=1):
        print("{:d}: {:s}".format(i, argument))
