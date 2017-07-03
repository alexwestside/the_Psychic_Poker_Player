#!bin/user/python

from __future__ import print_function
import sys

stdin = ['A B 1 2']
# stdin = ['TH JH QC QD QS QH KH AH 2S 6S',
#          '2H 2S 3H 3S 3C 2D 3D 6C 9C TH',
#          '2H 2S 3H 3S 3C 2D 9C 3D 6C TH',
#          '2H AD 5H AC 7H AH 6H 9H 4H 3C',
#          'AC 2D 9C 3S KD 5S 4D KS AS 4C',
#          'KS AH 2H 3C 4H KC 2C TC 2D AS',
#          'AH 2C 9S AD 3C QH KS JS JD KD',
#          '6C 9C 8C 2D 7C 2H TC 4C 9S AH',
#          '3D 5S 2H QD TD 6S KH 9H AD QH']

solve = list()
combination = None

def init_solve_list(solve, len):
    # for i in range(0, len):
    #     solve.index([None], i)
    solve = [None] * len
    return solve


def solve_print(combination, hand, deck):
    print("Hand: ", end='')
    print(hand, end='')
    print(" Deck: ", end='')
    print(deck, end='')
    print(" Best hand: ", end='')
    print(combination)
    exit(0)


def check_straight_flush(solve, list):
    return 0

def check(solve):
    return 0

def solution(solve, hand, deck, i, j, k, l):
    while i < len(hand):
        while j < len(deck):




    # solve = "straight-flush"
    return

# for line in sys.stdin:
for line in stdin:
    line = line.split(' ')
    hand = line[0:len(line)/2]
    deck = line[len(line)/2:len(line)]
    # solve = init_solve_list(solve, len(deck))
    if check_straight_flush(solve, hand):
        solve_print(combination, hand, deck)
    if check_straight_flush(solve, deck):
        solve_print(combination, hand, deck)
    n = 1
    # solution(solve, hand, deck[0:len(deck) - n], n, 0, 0, 0)
    solution(init_solve_list(solve, len(deck)), hand, deck, 0, 0, 0, 0)