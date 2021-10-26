from types import LambdaType
from rich import print

def find_answers(rules: list[LambdaType], top_length: int = 100) -> list[int]:
    """
    Finds all answers to the rules in the given range.
    :param rules: list of functions
    :param top_length: int
    :return: list of int
    """
    answers = []
    for i in range(top_length):
        if all(rule(i) for rule in rules):
            answers.append(i)
    return answers

GIVEN_RULES = [
    lambda x: x % 3 == 0,
    lambda x: x % 2 == 0,
    lambda x: len(str(x)) == 2,
    lambda x: abs(int(str(x)[0]) - int(str(x)[1])) == 5,
    lambda x: x % sum(int(digit) for digit in str(x)) == 0,
]

PERSONAL_RULES = [

]
if __name__ == '__main__':
    print(find_answers(GIVEN_RULES))
