# 1) Import the random function and generate both a random number between 0 and 1 as well as a random number between 1 and 10.
import random
import datetime
import time


iterations = list(range(1,6))


def random_0_to_1():
    return random.random()


def random_1_to_10():
    return random.uniform(1, 10)

print('\n#1.- RANDOM FUNCTIONS')

print('\n    Random numbers between 0.0 and 1.0:')
for i in iterations:
    print(8 * ' ' + 'iteration {:2}:     {:<25}'.format(i, random_0_to_1()))

print('\n    Random numbers between 1.0 and 10.0:')
for i in iterations:
    print(8 * ' ' + 'iteration {:2}:     {:<25}'.format(i, random_1_to_10()))

print('\n')

# 2) Use the datetime library together with the random number to generate a random, unique value.
print('\n#2.- RANDOM with DATETIME FUNCTIONS')

for i in iterations:
    i_seed = datetime.datetime.now().microsecond
    random.seed(i_seed)
    i_random = random_0_to_1()
    print(8 * ' ' + 'iteration {:2} (seed={:6}):     {:<25}'.format(i, i_seed, i_random))
    time.sleep(i_random)

print('\n')