from brain_games.mathlib import randint

task = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def gen_question():
    return randint()


def str_question(question):
    return str(question)


def correct_answer(question):
    return {True: "yes", False: "no"}[_isprime(question)]


def is_correct_answer(question, answer):
    return correct_answer(question) == answer


def _isprime(n):
    if n == 2:
        return True
    if n < 2 or n % 2 == 0:
        return False
    for k in range(3, int(n ** 0.5) + 1, 2):
        if n % k == 0:
            return False
    return True
