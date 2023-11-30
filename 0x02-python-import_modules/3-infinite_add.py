#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    arguments = sys.argv[1:]
    res = 0
    for i in arguments:
        res += int(i)
        print("{}".format(res))
