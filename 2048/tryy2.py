__author__ = 'Jasiu'
import random


class Hex:
    def __init__(self):
        self.grid = [[Tile() for i in range(size)] for j in range(size)]
        self.addRandomTile()
        self.addRandomTile()