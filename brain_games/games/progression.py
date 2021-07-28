import random
from brain_games.mathlib import randint, randint_except_fromlist

task = "What number is missing in the progression?"

_progression_size = 10
_min_diff = -10
_max_diff = 10


def gen_question():
    size = _progression_size + randint(-2, 2)
    init_num = randint()
    differance = randint_except_fromlist([0], _min_diff, _max_diff)
    progression = [str(init_num + k * differance) for k in range(size)]

    id_to_hide = random.randint(0, size - 1)
    answer = progression[id_to_hide]
    progression[id_to_hide] = ".."

    return (progression, answer)


def str_question(question):
    progression, answer = question
    return " ".join(progression)


def correct_answer(question):
    progression, answer = question
    return answer


def is_correct_answer(question, answer):
    return str(correct_answer(question)) == answer
