from brain_games.mathlib import randint, is_prime

task = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def gen_question():
    return randint()


def str_question(question):
    return str(question)


def correct_answer(question):
    return {True: "yes", False: "no"}[is_prime(question)]


def is_correct_answer(question, answer):
    return correct_answer(question) == answer
