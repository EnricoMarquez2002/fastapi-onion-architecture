import random
import string
from random import randint


def number_order(number_of_letters):
    letter = ''.join(random.choice(string.ascii_letters) for x in range(number_of_letters))
    letter = letter.upper()
    for x in range(1):
        value = randint(1000,1999)

    return f'{letter}-{value}'


