import random
import os

r = random.randint(1, 100)
c = 0

while True:
    print ("Please input a number between 1 and 100")
    t = int(input())
    c = c + 1
    if (t == r):
        print ("Right! you takes", c, "times to get the right answer.")
        break
    elif (t < r):
        print (t, "is too low")
    else:
        print (t, "is too big")

os.system("pause")