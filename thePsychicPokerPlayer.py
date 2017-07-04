#!bin/user/python

from __future__ import print_function
import sys


# stdin = ['A B C 1 2 3']
stdin = ['TH JH QC QD QS QH KH AH 2S 6S']
#          '2H 2S 3H 3S 3C 2D 3D 6C 9C TH',
#          '2H 2S 3H 3S 3C 2D 9C 3D 6C TH',
#          '2H AD 5H AC 7H AH 6H 9H 4H 3C',
#          'AC 2D 9C 3S KD 5S 4D KS AS 4C',
#          'KS AH 2H 3C 4H KC 2C TC 2D AS',
#          'AH 2C 9S AD 3C QH KS JS JD KD',
#          '6C 9C 8C 2D 7C 2H TC 4C 9S AH',
#          '3D 5S 2H QD TD 6S KH 9H AD QH']

combination = None
fp = open('./test.txt', 'a')

class CardsCombination:
    comb_1 = 'straight-flush'
    comb_2 = 'four-of-a-kind'
    comb_3 = 'full-house'
    comb_4 = 'flush'
    comb_5 = 'straight'
    comb_6 = 'three-of-a-kind'
    comb_7 = 'two-pairs'
    comb_8 = 'one-pair'
    comb_9 = 'highest-card'
    combination = None

    def find_combination(self):
        if self.straight_flush() == 1:
            pass
        elif self.four_of_a_kind() == 1:
            pass
        elif self.full_house() == 1:
            pass
        elif self.flush() == 1:
            pass
        elif self.straight() == 1:
            pass
        elif self.three_of_a_kind() == 1:
            pass
        elif self.two_pairs() == 1:
            pass
        elif self.one_pair() == 1:
            pass
        elif self.highest_card() == 1:
            pass

    def straight_flush(self):
        return (1)

    def four_of_a_kind(self):
        return (1)

    def full_house(self):
        return (1)

    def flush(self):
        return (1)

    def straight(self):
        return (1)

    def three_of_a_kind(self):
        return (1)

    def two_pairs(self):
        return (1)

    def one_pair(self):
        return (1)

    def highest_card(self):
        return (1)
    pass

    def solve_print(self, hand, deck):
        print("Hand: ", end='')
        print(hand, end='')
        print(" Deck: ", end='')
        print(deck, end='')
        print(" Best hand: ", end='')
        print(combination)
        exit(0)

def check(solve):
    return 0

def solution(hand, deck, _hand=None, _deck=None):
    if _hand is None:
        _hand = [n for n in hand]
        _deck = [n for n in deck]
        solution(hand, deck, _hand, _deck)
    else:
        if (len(_deck) == 0):
            return
        else:
            for i in range(len(hand)):
                solve = [n for n in _hand]
                if solve[i] not in deck:
                    solve[i] = _deck[0]
                    # print(solve, file=fp)
                    # print(solve)
                    check(solve)
                solution(hand, deck, solve, _deck[1:])
    return

# for line in sys.stdin:
for line in stdin:
    line = line.split(' ')
    hand = line[0:len(line)/2]
    deck = line[len(line)/2:len(line)]
    solution(hand, deck)
