#!/usr/bin/env python3

"""
Each Blob represents a set of pixels in an image,
which connected to each other.
"""


class Blob:
    def __init__(self):
        self.__pixels = []

    def add(self, x, y):
        self.__pixels.append((x, y))

    @property
    def mass(self):
        return len(self.__pixels)

    @property
    def center(self):
        n = self.mass
        _x = _y = 0
        for x, y in self.__pixels:
            _x += x
            _y += y
        return (_x / n, _y / n)

    def distanceTo(self, other):
        x1, y1 = self.center
        x2, y2 = other.center
        return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

    def __str__(self):
        x, y = self.center
        return f"{self.mass} (".rjust(5) + f"{x:.4f}, ".rjust(10) + f"{y:.4f})".rjust(9)
