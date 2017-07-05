#!bin/user/python

from __future__ import print_function
from collections import Counter
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

fp = open('./test.txt', 'a')

class CardsCombination:
    combination = {None: 0}
    combinations = {1: {'straight-flush': 1},
                    2: {'four-of-a-kind': 2},
                    3: {'full-house': 3},
                    4: {'flush': 4},
                    5: {'straight': 5},
                    6: {'three-of-a-kind': 6},
                    7: {'two-pairs': 7},
                    8: {'one-pair': 8},
                    9: {'highest-card': 9}}

    def make_choice(self, id):
        if self.combination.keys()[0] == None:
            self.combination.clear()
            self.combination.update(self.combinations.get(id))
        else:
            if self.combination.values()[0] > self.combinations.get(id).values()[0]:
                self.combination.clear()
                self.combination.update(self.combinations.get(id))

    def find_combination(self, solve, hand, deck):
        if self.straight_flush(solve) is True:
            self.solve_print(self.combinations.get(1).values()[0], hand, deck)
        elif self.four_of_a_kind(solve) is True:
            self.make_choice(2)
        elif self.full_house(solve) is True:
            self.make_choice(3)
        elif self.flush(solve) is True:
            self.make_choice(4)
        elif self.straight(solve) is True:
            self.make_choice(5)
        elif self.three_of_a_kind(solve) is True:
            self.make_choice(6)
        elif self.two_pairs(solve) is True:
            self.make_choice(7)
        elif self.one_pair(solve) is True:
            self.make_choice(8)
        elif self.highest_card(solve) is True:
            self.make_choice(9)

    def straight_flush(self, solve):
        s = solve
        return 0

    def four_of_a_kind(self, solve):
        return 0

    def full_house(self, solve):
        return 0

    def flush(self, solve):
        suit = list()
        for card in solve:
            suit.append(card[1])
        if len(set(suit)) != 1:
            return 0
        return 0

    def straight(self, solve):
        return 0

    def three_of_a_kind(self, solve):
        return 0

    def two_pairs(self, solve):
        return 0

    def one_pair(self, solve):
        face = list()
        count = 0
        for card in solve:
            face.append(card[0])
        face = dict(Counter(face)).values()
        for i in face:
            if i == 2:
                count += 1
        return 8 if count == 2 else 0

    def highest_card(self, solve):
        return 9
    pass

    def solve_print(self, solve, hand, deck):
        print("Hand: ", end='')
        print(hand, end='')
        print(" Deck: ", end='')
        print(deck, end='')
        print(" Best hand: ", end='')
        print(solve)
        exit(0)

res = CardsCombination()

# def check(solve, hand, deck):
#     res = CardsCombination()
#     res.find_combination(solve, hand, deck)


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
                    # check(solve, hand, deck)
                    res.find_combination(solve, hand, deck)
                solution(hand, deck, solve, _deck[1:])
    return

# for line in sys.stdin:
for line in stdin:
    line = line.split(' ')
    hand = line[0:len(line)/2]
    deck = line[len(line)/2:len(line)]
    solution(hand, deck)
    res.solve_print(res.combination.values()[0], hand, deck)
