#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    arglen = len(argv)
    print("{} argument{}{}".format(
        arglen - 1,
        's' if arglen != 2 else '',
        '' if arglen == 1 else ':'
        ))
    for i in range(1, arglen):
        print("{}:{}".format(i, argv[i]))
