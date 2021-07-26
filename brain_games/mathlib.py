import random
import brain_games.settings as settings


def randint(number_from=settings.RANDOM_FROM, number_to=settings.RANDOM_TO):
    return random.randint(number_from, number_to)


def is_even(number):
    return number % 2 == 0
