

import random

def generate_random_list(n, min, max):
    l = []
    for i in range(n):
        e = random.randint(min, max)
        l.append(e)
    return l