#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    arguments = sys.argv[1:]
    res = sum(int(i) for i in arguments)
    print(res)
