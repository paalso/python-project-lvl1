from brain_games.settings import QUESTIONS_NUMBER
from brain_games.cli import get_name, print_wrong_answer_msg
from brain_games.mathlib import randint
from brain_games.even_lib import correct_answer, is_correct_answer


def game():

    print("Welcome to the Brain Games!")
    name = get_name()
    print("Hello, {}!".format(name))

    print('Answer "yes" if the number is even, otherwise answer "no".')

    correct_answers_counter = 0

    for _ in range(QUESTIONS_NUMBER):
        number = randint()
        print("Question: {}".format(number))
        answer = input("Your answer: ")

        if is_correct_answer(number, answer):
            correct_answers_counter += 1
            print("Correct!")
        else:
            print_wrong_answer_msg(answer, number, correct_answer)
            break

    if correct_answers_counter == QUESTIONS_NUMBER:
        print("Congratulations, {}!".format(name))
