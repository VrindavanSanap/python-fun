#!/usr/bin/python3

import collections
from random import choice

Peice = collections.namedtuple("Peice", ["color", "name"])

class Chess_set:
    colors = ["White", "Black"]
    names = ['King', 'Queen', 'Rook', 'Bishop', 'Knight', 'Pawn']

    def __init__(self):
        self._peices = [Peice(c, n) for c in self.colors for n in self.names]
    
    def __len__(self):
        return len(self._peices)
    
    def __getitem__(self, position):
        return self._peices[position]

def rank_peice(peice):
    return Chess_set.names.index(peice.name) +  Chess_set.colors.index(peice.color) * 8

black_rook = Peice("Black", "Rook")
white_pawn = Peice("White", "Pawn")

a = rank_peice(white_pawn)
b = rank_peice(black_rook)
print(a, b)
peices = Chess_set()
print(sorted(peices,key = rank_peice) )
