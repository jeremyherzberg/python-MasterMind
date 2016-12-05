from itertools import combinations, combinations_with_replacement, permutations,\
    repeat, product, count
from random import random, sample

ANSWER = [0, 1, 2, 3]
SIZE = 4
NUM_OF_CHOICES = 6


def perm_creation(num_of_choices, array_size):
    range_of_choices = range(0, num_of_choices)
    return [p for p in product(range_of_choices, repeat=array_size)]


def generate_guess(perm):
    return sample(perm, 1)

def get_response(answer_run, guess, num_of_choices):
    account_array = [0] * num_of_choices
    response = [0, 0]
    for element in guess:
        if answer_run[guess.index(element)].__eq__(element):
            response[0] += 1
        else:
            account_array[element] += 1
    for ele in guess:
        if account_array[guess.index(ele)].__gt__(0):
            response[1] += 1
            account_array[guess.index(ele)] -= 1
    return response


def find_answer(perm, answer, arraySize, num_of_choices):
    guess = generate_guess(perm)
    print(len(perm))
    response = get_response(answer, guess, num_of_choices)
    if response.__eq__([4, 0]):
        return guess
    new_perm = []
    for element in perm:
        if get_response(answer, element, num_of_choices).__eq__(response):
            new_perm.append(element)
    call_perm = list(new_perm)
    find_answer(call_perm, answer, arraySize, num_of_choices)


find_answer(perm_creation(NUM_OF_CHOICES, SIZE), ANSWER, SIZE, NUM_OF_CHOICES)
