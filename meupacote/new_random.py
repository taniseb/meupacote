import random

def n_random(n):
    randomlist = []
    for i in range(0,n):
        i = random.randint(1,30)
        randomlist.append(i)
    return randomlist
