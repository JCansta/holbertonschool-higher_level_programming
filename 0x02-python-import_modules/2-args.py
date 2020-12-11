#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    leng = len(sys.argv)
    strn = "argument"
    num = 0
    if leng != 2:
        strn += "s"
    if leng > 0 and leng != 1:
        print("{} {}:".format(leng - 1, strn))
        for i in sys.argv[1:]:
            print("{}: {}".format(num + 1, i))
            num += 1
    else:
        print("{} {}.".format(leng - 1, strn))
