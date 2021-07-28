import random
import brain_games.settings as settings


def randint(number_from=settings.MIN_NUMBER, number_to=settings.MAX_NUMBER):
    return random.randint(number_from, number_to)


def randint_except_fromlist(except_nums_list,
                            number_from=settings.MIN_NUMBER,
                            number_to=settings.MAX_NUMBER):
    while True:
        n = randint(number_from, number_to)
        if n not in except_nums_list:
            return n


def is_even(number):
    return number % 2 == 0


def is_prime(n):
    if n == 2:
        return True
    if n < 2 or is_even(n):
        return False
    for k in range(3, int(n ** 0.5) + 1, 2):
        if n % k == 0:
            return False
    return True
