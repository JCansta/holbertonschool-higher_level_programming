#!/usr/bin/python3
count = 1
for i in range(ord('z'), ord('a')-1, -1):
    char = i
    if count % 2 == 0:
        char -= 32
    count += 1
    print("{:c}".format(char), end="")
