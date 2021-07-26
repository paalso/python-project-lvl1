from brain_games.mathlib import is_even


def correct_answer(number):
    return {True: "yes", False: "no"}[is_even(number)]


def is_correct_answer(number, answer):
    return (is_even(number) and answer == "yes") \
        or (not is_even(number) and answer == "no")
