import random
from brain_games.mathlib import randint

task = "What is the result of the expression?"


def gen_question():
    return (randint(), random.choice("+-*"), randint())


def str_question(question):
    operand1, operation, operand2 = question
    return str("{} {} {}".format(operand1, operation, operand2))


def correct_answer(question):
    return eval(str_question(question))


def is_correct_answer(question, answer):
    return str(correct_answer(question)) == answer
