import math
from brain_games.mathlib import randint

task = "Find the greatest common divisor of given numbers."


def gen_question():
    return (randint(), randint())


def str_question(question):
    return str(question)


def correct_answer(question):
    n, m = question
    return math.gcd(n, m)


def is_correct_answer(question, answer):
    return str(correct_answer(question)) == answer
