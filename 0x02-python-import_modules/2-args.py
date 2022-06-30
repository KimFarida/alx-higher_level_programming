#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    result = len(sys.argv)
    if result <= 1:
        print("0 arguments.")
    else:
        if result == 2:
            print("{:d} argument:".format(result - 1))
        else:
            print("{:d} arguments:".format(result - 1))
        for i in range(1, result):
            print("{:d}: {}".format(i, sys.argv[i]))
