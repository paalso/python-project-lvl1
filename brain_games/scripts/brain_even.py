#!/usr/bin/env python

import random
from brain_games.cli import get_name


def is_even(number):
    return number % 2 == 0


def is_correct_answer(number, answer):
    return (is_even(number) and answer == "yes") \
        or (not is_even(number) and answer == "no")


def main():
    questions_number = 3
    random_number_from = 1
    random_number_to = 1000

    print("Welcome to the Brain Games!")
    name = get_name()
    print("Hello, {}!".format(name))

    print('Answer "yes" if the number is even, otherwise answer "no".')

    correct_answers_counter = 0

    for _ in range(questions_number):
        number = random.randint(random_number_from, random_number_to)
        print("Question: {}".format(number))
        answer = input("Your answer: ")

        if is_correct_answer(number, answer):
            correct_answers_counter += 1
            print("Correct!")

    if correct_answers_counter == questions_number:
        print("Congratulations, {}!".format(name))


if __name__ == '__main__':
    main()
