'''
Created on Dec 2, 2016

@author: Jeremy
'''
from itertools import combinations, combinations_with_replacement, permutations,\
    repeat, product, count
from random import random, sample

if __name__ == '__main__':
    pass

answer = {0,1,2,3}
size = 4
x=6

def perm_creation(x,size):
    x = range(0,x)
    return [p for p in product(x, repeat=size)]

def generate_guess(perm):
    return sample(perm,1)

def get_response(answer,guess, x):
    accountArray = [0] * size 
    response = {0,0}
    for i in guess:
        if answer[i].__eq__(guess[i]):
            response[0] +=1
        else:
            accountArray[guess[i]] +=1
    for i in guess:
        if accountArray[guess[i]] != 0:
            response[1] += accountArray[guess[i]]
            accountArray[guess[i]] = 0
    return response
            
def find_answer(perm,answer,size,x):
    guess = generate_guess(perm)
    response = get_response(guess,answer,x)
    if response == [4,0]:
        return guess
    new_perm = [];
    for element in perm:
        if get_response(answer,element,x) == response:
            new_perm.extend(element)
    find_answer(new_perm,answer,size,x)        
        
    
find_answer(perm_creation(x,size), answer,size,x)
    
            
        
    
    
    

