import prompt


def welcome_user():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print("Hello, {}!".format(name))


def get_name():
    name = prompt.string('May I have your name? ')
    return name


def print_wrong_answer_msg(answer, number, correct_answer):
    print("'{}' is wrong answer ;(. Correct answer was '{}'."
          .format(answer, correct_answer(number)))
    print("Let's try again, Bill!")
