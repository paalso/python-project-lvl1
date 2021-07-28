import importlib
import prompt
from brain_games.settings import QUESTIONS_NUMBER


def get_name():
    name = prompt.string('May I have your name? ')
    return name


def print_wrong_answer_msg(name, answer, question, correct_answer):
    print("'{}' is wrong answer ;(. Correct answer was '{}'."
          .format(answer, correct_answer(question)))
    print("Let's try again, {}!".format(name))


# "even", "calc", "gcd", "progression", "prime"
def run_game(game_name, questions_number=QUESTIONS_NUMBER):

    game_lib = importlib.import_module(
        "brain_games.games.{}".format(game_name))

    print("Welcome to the Brain Games!")
    name = get_name()
    print("Hello, {}!".format(name))
    print(game_lib.task)
    correct_answers_counter = 0

    for _ in range(questions_number):
        question = game_lib.gen_question()
        print("Question: {}".format(game_lib.str_question(question)))
        answer = input("Your answer: ")

        if game_lib.is_correct_answer(question, answer):
            correct_answers_counter += 1
            print("Correct!")
        else:
            print_wrong_answer_msg(
                name, answer, question, game_lib.correct_answer)
            break

    if correct_answers_counter == questions_number:
        print("Congratulations, {}!".format(name))
