import random
import brain_games.settings as settings


def randint(number_from=settings.MIN_NUMBER, number_to=settings.MAX_NUMBER):
    return random.randint(number_from, number_to)


def is_even(number):
    return number % 2 == 0
