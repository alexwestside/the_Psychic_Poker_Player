#!bin/user/python

from __future__ import print_function
import sys
from collections import Counter

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

    def find_combination(self, solve):
        if self.straight_flush(solve) is True:
            self.make_choice(1)
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
        elif self.highest_card() is True:
            self.make_choice(9)

    def straight_flush(self, solve):
        if self.flush(solve) is True:
            if self.straight(solve) is True:
                return True
        return False

    def four_of_a_kind(self, solve):
        face = list()
        for card in solve:
            face.append(card[0])
        face = dict(Counter(face)).values()
        for i in face:
            if i == 4:
                return True
        return False

    def full_house(self, solve):
        if self.three_of_a_kind(solve) is True:
            if self.one_pair(solve) is True:
                return True
        return False

    def flush(self, solve):
        suit = list()
        for card in solve:
            suit.append(card[1])
        if len(set(suit)) != 1:
            return False
        return True

    def straight(self, solve):
        face = list()
        for card in solve:
            face.append(card[0])
        face = self.make_int_sequense(face)
        face = sorted(face)
        if face == range(face[0], face[len(face) - 1] + 1):
            return True
        return 0

    def three_of_a_kind(self, solve):
        face = list()
        for card in solve:
            face.append(card[0])
        face = dict(Counter(face)).values()
        for i in face:
            if i == 3:
                return True
        return False

    def two_pairs(self, solve):
        face = list()
        count = 0
        for card in solve:
            face.append(card[0])
        face = dict(Counter(face)).values()
        for i in face:
            if i == 2:
                count += 1
        return True if count == 2 else False

    def one_pair(self, solve):
        face = list()
        for card in solve:
            face.append(card[0])
        face = dict(Counter(face)).values()
        for i in face:
            if i == 2:
                return True
        return False

    def highest_card(self):
        return True

    def make_int_sequense(self, face):
        count = int(0)
        for i in range(0, len(face)):
            if face[i] == 'A':
                for j in range(0, len(face)):
                    if face[j] != 'A' and face[j] != 'K' and face[j] != 'Q' and face[j] != 'J' and face[j] != 'T':
                        count += int(face[j])
                if count == int(14):
                    face[i] = int(1)
                else:
                    face[i] = int(14)
            elif face[i] == 'K':
                face[i] = int(13)
            elif face[i] == 'Q':
                face[i] = int(12)
            elif face[i] == 'J':
                face[i] = int(11)
            elif face[i] == 'T':
                face[i] = int(10)
            else:
                face[i] = int(face[i])
        return face

    def solve_print(self, solve, hand, deck):
        print("Hand: ", end='')
        for n in hand: print(n + ' ', end='')
        print(" Deck: ", end='')
        for n in deck: print(n + ' ', end='')
        print(" Best hand: ", end='')
        print(solve)


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
                    res.find_combination(solve)
                    solution(hand, deck, solve, _deck[1:])
                    if res.combination.keys()[0] == 'straight-flush':
                        return
    return

for line in sys.stdin:
    res = CardsCombination()
    res.combination = {None: 0}
    line = line.strip().split(' ')
    hand = line[0:len(line) / 2]
    deck = line[len(line) / 2:len(line)]
    if (lambda x: x == True)((lambda x, y: x == True or y == True)(res.straight_flush(hand), res.straight_flush(deck))):
        res.solve_print('straight-flush', hand, deck)
        continue
    else:
        solution(hand, deck)
    res.solve_print(res.combination.keys()[0], hand, deck)