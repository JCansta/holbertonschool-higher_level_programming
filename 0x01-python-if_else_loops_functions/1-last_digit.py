#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number > 0:
    last = number % 10
    check = 0
elif number < 0:
    last = -number % 10
    last = -last
    check = 1

if last > 5:
    print("Last digit of {:d} is {:d} and is greater than 5"
          .format(number, last))
elif last is 0:
    print("Last digit of {:d} is {:d} and is 0".format(number, last))
else:
    print("Last digit of {:d} is {:d} and is less than 6 and not 0"
          .format(number, last))
