import random as rd
import time as t

def random_number_range(start, end):
    return rd.randint(start, end)
    #return rd.randrange(start, end)

def random_number(number_of_random_numbers):
    random_numbers = []
    for _ in range(number_of_random_numbers):
        random_numbers.append(rd.randint(0,100000))
    return random_numbers

def random_number_range(start, end):
    return rd.choice(range(start, end))

def countdown(start, end, step):
    for i in range(start, end, step):
        print(i, ',', end='')
        t.sleep(2)
    print('Fire!')

def sum_pairs(end):
    sum = 0
    for i in range(end+1):
        if i % 2 == 0:
            sum += i
    return sum

def multiplication_table(number):
    multiplier = 1
    while multiplier <= 10:
        print(f'{multiplier} * {number} =', multiplier * number)
        multiplier += 1
