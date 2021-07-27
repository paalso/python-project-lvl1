from brain_games.mathlib import is_even, randint

task = 'Answer "yes" if the number is even, otherwise answer "no".'


def gen_question():
    return randint()


def str_question(question):
    return str(question)


def correct_answer(question):
    return {True: "yes", False: "no"}[is_even(question)]


def is_correct_answer(question, answer):
    return correct_answer(question) == answer
