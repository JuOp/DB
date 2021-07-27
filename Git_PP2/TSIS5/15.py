import random
def rand_line(filename):
    lines = open(filename).readlines()
    return random.choice(lines)

filename = input()
print(rand_line(filename))