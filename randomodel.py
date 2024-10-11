import random
from count import count

max = count()


def randmod(max):
    n = random.randint(1, max)
    print(n)
    return n


ranm = randmod(max)